number = input("정수를 입력하세요 : ")

last_ch = number[-1] # 일단위 수
last_num = int(last_ch)

#if last_num % 2 == 1:
if last_ch in "13579":
    print("홀수입니다")

if last_num == 0 \
    or last_num == 2 \
    or last_num == 4 \
    or last_num == 6 \
    or last_num == 8:
    print("짝수입니다")