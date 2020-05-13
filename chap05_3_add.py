f = open("./data/basic.txt", "w") # 파일 열기
f.write("Hello Python Programming...!") # 파일 쓰기
f.close() # 파일 닫기

f1 = open("./data/basic.txt", "a")
f1.write("\nAdded documents")
f1.close()

with open("./data/test.txt", "a") as f3:
    f3.write("\nwith sentence documents")

with open("./data/test.txt", "r") as f4:
    content = f4.read()

print(content)