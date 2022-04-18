import module_exam.사용자정의모듈other.mymod2   # 메인 파일과 패키지가 다른 위치이므로 import를 한다.
add = module_exam.사용자정의모듈other.mymod2.add(5, 3)  # 패키지명.모듈명.함수명()으로 호출한다.
print('합:',add)
print('차:', module_exam.사용자정의모듈other.mymod2.subtract(5, 3))

from module_exam.사용자정의모듈other.mymod2 import add, subtract    # from ... import 모듈멤버, ... 처럼 나열하면,
print('합:',add(5, 3))   # 모듈명 없이 함수명()으로 실행한다.
print('차:', subtract(5, 3))

print('Pythonpath가 설정된 폴더의 module_exam 읽기 연습')
import mymod3
print('곱:', mymod3.multiply(5, 3))

from mymod3 import *    # *을 주면 호출되는 모듈의 모든 멤버가 호출 대상이 된다.
print('곱:', multiply(5, 3))

print('전혀 연관 없는 폴더')
import sys
sys.path.append(r'C:/Users/tlatm/Desktop/work') # 전혀 경로 설정과 관련 없는 폴더를 path에 추가
import mymod4
print('나누기:', mymod4.divide(5, 3))
