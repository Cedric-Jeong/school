import csv

f = open("csv_sample1.csv", "w", encoding="utf-8", newline="")
field = ['번호', '학과', '학년', '이름', '역할']
writer = csv.DictWriter(f, fieldnames=field)

writer.writeheader()
writer.writerow({'번호': '1', '학과': '컴퓨터학부', '학년': '1', '이름': '정주영', '역할': '학생'})

f.close()
