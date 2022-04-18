print('경로지정 방법 1 -> import 패키지명.모듈명')
import module_exam.사용자정의모듈.mymod1    # module_test 파일과 같은 패키지에 있어도 패키지명은 적어 준다.
print(dir(module_exam.사용자정의모듈.mymod1))   # mymod1에 정의된 멤버 목록을 확인
print()

print('mymod1의 함수 호출')
list1 = [1, 3]
list2 = [1, 2]
module_exam.사용자정의모듈.mymod1.listAdd(list1, list2)
print()

print('경로지정 방법 2 -> from 패키지명 import 모듈명')
from module_exam.사용자정의모듈 import mymod1
mymod1.ted()    # ted 함수를 모듈명.함수명()으로 호출
print('다른 모듈의 전역변수 읽기 tot:',mymod1.tot) # 모듈명.변수
print()

print('경로지정 방법 3 -> from 패키지명.모듈명 import 함수명, ...변수, ...')
from module_exam.사용자정의모듈.mymod1 import robin
robin() # 함수명()만 적어도 호출 가능