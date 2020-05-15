# 마지막 테스트 파이썬
import json

dic_mcu = []

# print(dic_mcu)
# with open("./data/mcu_movies.json", "w", encoding="UTF-8") as mcu_list:
#   json.dump(dic_mcu, mcu_list, ensure_ascii=False)

with open("./mcu_movies.json", "r", encoding="UTF-8") as mcu_list:
  dic_mcu = json.load(mcu_list)

# print(dic_mcu)

# for line in dic_mcu:
#   for item in line:
#     print(item, line[item])
#   print()

# 문제 1번
# 페이즈가 1인 마블 시네마틱 유니버스 영화면 뽑기
list_movie = []

for movie in dic_mcu:
  if movie.get('시리즈') == '페이즈2':
    # print("{} ( {} )".format(movie['영화명'], movie['개봉일']))
    list_movie.append([movie['영화명'], movie['개봉일']])

for line in list_movie:
  print("{} ( {} )".format(line[0], line[1]))
print()

# 문제 2번
# 박스오피스가 450000000 이상인 영화들의 감독이름 리스트와 전체 합계금액, 평균 박스오피스 구하기
list_pd = []
count = 0
sum = 0
avr = 0.0

for movie in dic_mcu:
  if movie.get('박스오피스') > 450000000:
    for item in list_pd:
      if item == movie['감독']:
        list_pd.remove(movie['감독'])
    list_pd.append(movie['감독'])
    sum += movie['박스오피스']
    count += 1

avr = sum / count

# pd = set(list_pd)

print("감독 리스트 :")
# print(list(pd))
print(list_pd)
print("총 박스오피스 합계 $", format(sum, ',d'))
print("평균 박스오피스 $", format(int(avr), ',d'))