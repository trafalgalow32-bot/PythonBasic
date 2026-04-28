# file_csv.py

# csv - 쉼표로 구분된 데이터 (comma seperated)

import csv

with open("file/test1.csv", "r", encoding="utf-8") as f:
    # data = f.read()
    # print(data)
    data = csv.reader(f)
    print(data)

    for row in data:
        print(row)