def func(w, h, **other):    # other은 딕셔너리 형 자료와 매핑
    print('몸무게 {}. 키 {}'.format(w,h))
    print(other)

func(64, 175, name='Ted', age=23)
func(50, 175, name='Robin')
print()

# 함수의 매개변수에 인수를 전달할 때 *, ** 혼합도 가능
def functotal(a, b, *v1, **v2):
    print(a, b)
    print(v1)
    print(v2)

functotal(1, 2)
functotal(1, 2, 3, 4, 5)
functotal(1, 2, 3, 4, 5, m=6, n=7)