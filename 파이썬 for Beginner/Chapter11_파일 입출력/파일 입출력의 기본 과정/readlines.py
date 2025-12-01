#readlines은 문자 덩어리를 리스트로 묶어서 가지고 온다.
inFp = None
inStr = ""

inFp = open("C:/Users/USER/Desktop/test/test.md", "r", encoding = "utf-8")

inFplist = inFp.readlines()

print(inFplist)

# for i in inFplist:
#     print(i, end = "")

inFp.close()
