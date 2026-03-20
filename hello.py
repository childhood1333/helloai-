print("안녕하세요! 파이썬 공부를 시작합니다.")
import random

# 1부터 100 사이의 임의의 숫자를 뽑습니다 (모듈 사용)
secret_number = random.randint(1, 100)
attempts = 0

print("1부터 100 사이의 숫자를 맞춰보세요!")

# 정답을 맞출 때까지 무한 반복 (반복문)
while True:
    guess = int(input("숫자를 입력하세요: ")) # 입력 받기 및 자료형 변환
    attempts += 1

    # 숫자를 비교합니다 (조건문)
    if guess < secret_number:
        print("UP! 더 큰 숫자입니다.")
    elif guess > secret_number:
        print("DOWN! 더 작은 숫자입니다.")
    else:
        print(f"정답입니다! {attempts}번 만에 맞췄네요.")
        break # 반복문 탈출
