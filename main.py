#구현 실전문제 게임개발
#내가 풀어보는 답

# 맵 크기 n,m = 행, 열
n, m = map(int, input().split())

# a,b는 캐릭터 위치, d는 바라보는 방향
a, b, d = map(int, input().split())
rows = []

#방향 0 북쪽 / 1 동쪽 / 2 남쪽 / 3 서쪽
directions = [0, 1, 2, 3]
next_positions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
count = 0
#현재 포지션
position = [a, b]
#현재 좌표
rows[a][b]
#이동 후의 좌표
#n_a
#n_b

# 바다(1)와 육지(0) 구현
for i in range(n):
  row = list(map(int, input().split()))
  rows.append(row)
print(rows)
print("주인공의 위치 :" + str(rows[a][b]))

# 첫단계: 반시계 90도로 틀기
# 아이디어: 가본곳은 바다로 바꿔버리자(1로 바꿔버리자)<-이거 안됨
# 개선 아이디어: 가본곳은 2로 바꾸자(0이 아닌걸로 구분하자)
# 0은 육지이자 갈 수 있는 곳
# 1은 바다이자 갈 수 없는 곳
# 2는 가본 육지이자 갈 수 없는 곳
while True:
  # 방향 왼쪽으로 틀기
  if d == 0:  #북쪽이면
    d = 3
  else:  #북쪽이 아니면
    for i in range(1, 4):
      if d == i:
        d -= 1

  # 튼 방향으로 한칸 전진해보기 n_a, n_b는 이동 후 캐릭터 좌표
  for i in range(4):
    if i == d:
      n_a = a + next_positions[d][0]
      n_b = b + next_positions[d][1]

  if rows[n_a][n_b] == 0:
    count += 1
    rows[a][b] = 1
    a = n_a
    b = n_b
    continue

  else:  #다시 원래칸으로 돌아가고, 왼쪽으로 회전만
    n_a = a
    n_b = b
    continue  #다시 돌아가기

#아 3번째 메뉴얼을 구현을 못하겠네..
#아