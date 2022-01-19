import csv

# csvファイル書き込み
with open('test.csv', 'w') as csv_file:
    # ヘッダー書き込み
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # 列の書き込み
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})


# csvファイル読み込み
with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])
        # =>
        # A 1
        # B 2

# エクセルで開く方法
# open <csvファイル名>
