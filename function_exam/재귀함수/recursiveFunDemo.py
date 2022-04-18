def countdown(n):
    if n == 0:
        print("완료")
    else:
        print(n, end=' ')
        countdown(n - 1)    # 재귀 처리

countdown(5)