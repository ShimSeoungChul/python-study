from abc import *

class AbstractClass(metaclass=ABCMeta):  # 추상클래스
    @abstractmethod
    def abcMethod(self):    # 추상메서드
        pass

    def normalMethod(self):    # 일반메서드
        print('추상클래스 내의 일반 메서드')


class Child1(AbstractClass):    # 추상클래스를 상속
    name = '난 Child1'

    def abcMethod(self):    # 메서드 선언을 강요
        print('추상메서드를 오버라이드함')


class Child2(AbstractClass):    # 추상클래스를 상속
    def abcMethod(self):    # 메서드 선언을 강요
        print('추상메서드를 Child2d에서 오버라이드함')

    def normalMethod(self): # 일반 메서드 오버라이드는 선택적
        print('추상클래스의 일반 메서드를 재정의')


c1 = Child1()   # Child1 객체 생성
print(c1.name)
c1.abcMethod()
c1.normalMethod()
print()

c2 = Child2    # Child2 객체 생성
c2.abcMethod(c2)
c2.normalMethod(c2)
print()

parent = AbstractClass()
D