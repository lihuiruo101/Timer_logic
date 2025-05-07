import time

def main():
    try:
        seconds = int(input("타이머 시간(초)을 입력하세요: "))
        print(f"{seconds}초 동안 타이머를 시작합니다...")
        time.sleep(seconds)
        print("타이머 종료!")
    except ValueError:
        print("숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
