import json

student = {
    '학생 리스트': [
        {
            '번호': 1,
            '학과': '컴퓨터 공학과',
            '학년': 4,
            '이름': 'Cedric',
            '역할': '학생'
        },
        {
            '번호': 2,
            '학과': '컴퓨터 공학과',
            '학년': 1,
            '이름': '정주영',
            '역할': '학생'
        },
    ]
}

file = open('json_sample1.json', 'w', encoding = 'utf-8')
json.dump(student, file, indent = "\t", ensure_ascii = False)
file.close()

file = open('json_sample1.json', 'r', encoding = 'utf-8')
st = json.load(file)
file.close()
