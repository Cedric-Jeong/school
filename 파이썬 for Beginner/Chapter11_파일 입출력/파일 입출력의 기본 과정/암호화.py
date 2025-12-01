inFp, outFp = None, None
inStr, outStr = "", ""
secu = 0

secuYM = input("1. 암호화 2. 암호 해석: ")
inFname = input("입력 파일명을 입력하세요: ")
outFname = input("출력 파일명을 입력하세요: ")

if secuYM == "1":
    secu = 100
elif secuYM == "2":
    secu = -100

inFp = open(inFname, "r", encoding = "UTF-8")
outFp = open(outFname, "w", encoding = "UTF-8")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break

    outStr =""
    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum += secu
        ch2 = chr(chNum)
        outStr += ch2
    outFp.write(outStr)

outFp.close()
inFp.close()
print("변환 완료")
