import cv2
import mediapipe as mp
import streamlit as st
import numpy as np
import time

img_path = 'image/'
movie_path = 'movie/'

def sidebar_parm():
    col1, col2 = st.sidebar.columns(2)
    button_run = col1.button('Run')
    button_stop = col2.button('Stop')
    mode = st.sidebar.selectbox("モードの選択", ['Use movie file', 'Use WebCam'])
    fps_val = st.sidebar.slider("フレームレート", 1, 100, 30)

    uploaded_movie_file = None
    if mode == 'Use movie file':
        uploaded_movie_file = st.sidebar.file_uploader("動画ファイルアップロード", type="mp4")
        if uploaded_movie_file:
            st.sidebar.video(uploaded_movie_file)

    uploaded_image_file = None
    uploaded_image_file = st.sidebar.file_uploader("背景用画像ファイルアップロード", type=["jpg", "jpeg", "png"])
    if uploaded_image_file:
        st.sidebar.image(uploaded_image_file)

    return button_run, button_stop, mode, fps_val, uploaded_movie_file, uploaded_image_file, uploaded_image_file


def read_image_movie(img_path, uploaded_image_file, movie_path, uploaded_movie_file, mode):
    img_file_path = img_path + uploaded_image_file.name
    mv_file_path = None
    cap_file = None

    org_bg_image = cv2.imread(img_file_path)

    if mode == "Use movie file":
        mv_file_path = movie_path + uploaded_movie_file.name
        cap_file = cv2.VideoCapture(mv_file_path)
    else:
        cap_file = cv2.VideoCapture(0)

    return org_bg_image, cap_file


def created_virtual_bg(button_stop, org_bg_image, cap_file, mp_selfie_segmentation, mode, fps_val):
    image_container = st.empty()
    with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as mp_selfie_segmentation:
        while cap_file.isOpened():
            success, image = cap_file.read()

            if not success:
                break

            if button_stop:
                break

            if mode == "Use movie file":
                image = cv2.resize(image, dsize=None, fx=0.2, fy=0.2)
            else:
                image = cv2.flip(image, 1)

            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height = rgb_image.shape[0]
            width = rgb_image.shape[1]

            results = mp_selfie_segmentation.process(rgb_image)

            condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.6

            bg_image = cv2.resize(org_bg_image, dsize=(width, height))
            rgb_bg_image = cv2.cvtColor(bg_image, cv2.COLOR_BGR2RGB)
            output_image = np.where(condition, rgb_image, rgb_bg_image)

            time.sleep(1 / fps_val)

            image_container.image(output_image)

    cap_file.release()

    return 0




if __name__ == '__main__':
    st.sidebar.title('各種設定')
    button_run, button_stop, mode, fps_val, uploaded_movie_file, uploaded_image_file, uploaded_image_file = sidebar_parm()

    st.title("バーチャル背景動画作成アプリ")

    if button_run:
        if mode == 'Use movie file' and uploaded_movie_file is None:
            st.text("動画ファイルをアップロードしてください")
        elif uploaded_image_file is None:
            st.text("バーチャル背景画像をアップロードしてください")
        else:
            mp_selfie_segmentation = mp.solutions.selfie_segmentation
            org_bg_image, cap_file = read_image_movie(img_path, uploaded_image_file, movie_path, uploaded_movie_file, mode)
            created_virtual_bg(button_stop, org_bg_image, cap_file, mp_selfie_segmentation, mode, fps_val)
