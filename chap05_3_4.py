with open("./data/result.txt", "r") as f:
    for line in f:
        (name, height, weight) = line.strip().split(", ")

        if (not name) or (not height) or (not weight):
            continue

        bmi = int(weight) / (int(height) * int(height)) * 10000
        result = ""

        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름 : {}",
            "키 : {}",
            "몸무게 : {}",
            "BMI : {}",
            "결과 : {}"
        ]).format(name, height, weight, bmi, result))
        print()