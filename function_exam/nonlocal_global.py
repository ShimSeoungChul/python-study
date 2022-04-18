a = 10;b = 20;c = 30    # 전역변수
print('함수 수행 전 a:{}, b:{}, c:{}'.format(a, b, c))

def foo():
    # foo 함수 영역에서만 유효한 지역변수
    a = 40
    b = 50

    def bar():
        # b = 60  -> bar 함수 영역에서만 유효한 지역변수
        # c = 70
        nonlocal b  # b는 bar의 외부 함수인 foo의 b가 된다.
        global c    # c는 전역변수를 의미
        print('bar에서 출력1) a:{}, b:{}, c:{}'.format(a, b, c))
        b = 80
        print('bar에서 출력2) a:{}, b:{}, c:{}'.format(a, b, c))
        c = 90
        print('bar에서 출력3) a:{}, b:{}, c:{}'.format(a, b, c))

    bar()
    print('foo에서 출력 a:{}, b:{}, c:{}'.format(a, b, c))

foo()
print('함수 수행 후 a:{}, b:{}, c:{}'.format(a, b, c))
