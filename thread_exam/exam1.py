# Pool class_exam
from multiprocessing import Pool
import time
import os


def pool_func(arg):
    print('값', arg, '에 대한 pid:', os.getpid())  # 현재 실행되는 프로세스의 id 출력
    time.sleep(1)  # 너무 빠른 처리가 되지 않도록 편의상 약간의 지연 시간을 준다.
    return arg + 10  # 매개변수 값에 10을 더해 반환


if __name__ == '__main__':
    startTime = int(time.time())  # 처리 시작 시간 체크용

    # [방법 1] Pool 객체를 사용하지 않은 일반적인 방법으로 함수 호출
    for i in range(10):
        print(pool_func(i))

    endTime = int(time.time())  # 처리 종료 시간 기억
    print('총 작업 시간:', (endTime - startTime))

    print()

    # [방법 2] 멀티 태스킹이 가능한 Pool 객체로 함수를 호출
    startTime = int(time.time())
    po = Pool(processes=3)  # 프로세스 개수를 인자로 주고 함수 호출
    print(po.map(pool_func, range(10))) # 함수와 인자 값을 매핑하면서 처리 10회 반복

    endTime = int(time.time())
    print('총 작업 시간:', (endTime - startTime))
