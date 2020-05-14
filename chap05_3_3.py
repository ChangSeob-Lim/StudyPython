import random

hanguls = list("민경수진욱상은채섭철건예영")

with open("./data/result.txt", "w") as f:
    # f.write("{}, {}, {}\n".format("이름", "키", "몸무게"))
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        height = random.randrange(150, 200)
        weight = random.randrange(40, 100)

        f.write("{}, {}, {}\n".format(name, height, weight))

print("파일생성이 완료되었습니다.")