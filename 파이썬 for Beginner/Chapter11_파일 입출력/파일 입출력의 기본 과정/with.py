with open("test.md", "r", encoding = "UTF-8") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
