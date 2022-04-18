print('module_exam 사용하기')

import sys  # sys 모듈의 멤버를 사용할 수 있게 된다.
print("module_exam 경로: ",sys.path)
print()

# 수학 함수 읽기
import math
print("원주율(pi):",math.pi)
print("sin(30):",math.sin(math.radians(30)))
print()

# 달력 출력
import calendar
calendar.setfirstweekday(6) # 일요일을 첫 요일로 설정 (0:월, 1:화, ... ,6:일)
calendar.prmonth(2022,3)    # 출력 날짜를 설정
del calendar    # calendar 객체 삭제
print()

# 작업 경로 관련 정보 얻기
import os
print(os.getcwd())  # 현재 작업 경로 반환
print(os.listdir('/'))  # root 내의 파일 목록 반환
