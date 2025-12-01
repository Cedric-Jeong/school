outFp = None
outStr = ""

outFp = open("C:/Users/USER/Desktop/test/test.md", "w", encoding = "utf-8")

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("파일을 저장했습니다.")
