#readlined은 문자를 덩어리 채로 가지고 온다.
inFp = None
inStr = ""

inFp = open("C:/Users/USER/Desktop/test/test.md", "r", encoding = "utf-8")

while 1:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr, end = "")

# inStr = inFp.readline()
# print(inStr, end = "")
#
# inStr = inFp.readline()
# print(inStr, end = "")
#
# inStr = inFp.readline()
# print(inStr, end = "")

inFp.close()
