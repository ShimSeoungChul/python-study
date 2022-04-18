def showplus(start, end=5):
    print(start + end)

showplus(2, 3)
showplus(3)
showplus(start=2, end=3)    # 동일한 이름의 인수와 매개변수가 매핑
showplus(end=4, start=3)    # 동일한 이름의 인수와 매개변수가 매핑
showplus(2, end=3)

# 두 번째 인자가 상수면 에러 발생
# showplus(start=2, 3)
# showplus(end=4, 3)