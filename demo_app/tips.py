import os
import string

import termcolor


def get_template_dir_path():
    template_dir_path = None

    if not template_dir_path:
        # os.path.dirnameを使うことで上の階層にパスを移せる
        # 今回はconsole.pyからroboterディレクトリまで行きたかったのでこうなっている
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


class NoTemplateError(Exception):
    """No Template Error"""

def find_template(temp_file):
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError(f'Could not find {temp_file}')
    return temp_file_path


def get_template(temp_file_path):
    template = find_template(temp_file_path)
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        splitter = '=' * 60
        sep = os.linesep
        # 改行文字を削除
        contents = contents.rstrip(sep)
        contents = f'{splitter}{sep}{contents}{sep}{splitter}{sep}'
        contents = termcolor.colored(contents)
        return string.Template(contents)


def hello():
    # whileにすることで名前を入力せずにEnterを押してしまった時ループするようになっている
    while True:
        template = get_template('hello.txt')
        user_name = input(template.substitute({'robot_name': 'Roboko'}))

        if user_name:
            print(user_name.title())
            break


hello()
