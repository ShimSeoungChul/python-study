class Person:
    say = '사람사람'  # class_exam 멤버변수
    age = 20

    def __init__(self, age):  # 생성자 매개변수로 age를 받아 각 객체에 고유한 age를 갖는다.
        print('Person 생성자')
        self.age = age

    def printInfo(self):  # self에 전달되는 객체 주소에 따라 say와 age 값으이 결정
        print('say:{}, age:{}'.format(self.say, self.age))


class Employee(Person):
    say = '일하는 사람'  # 부모와 같은 이름의 멤버변수에 부모와 다른 값이 기억
    subject = '근로자'  # Employee만의 고유 멤버변수로 사용

    def __init__(self):
        print('Employee 생성자')

    def eprintInfo(self):
        self.printInfo()  # 현재 클래스의 메서드를 참조, 없으면 부모 메서드 참조
        super().printInfo()  # super()에 의해 바로 부모 메서드를 참조
        print(self.say)  # 현재 클래스에서 say를 참조하고, 없으면 부모의 say를 참조
        print(super().say)  # super()에 의해 바로 부모의 say를 참조

    def printInfo(self):
        print('오버라이딩(override): 부모와 같은 이름의 메서드를 자식에서도 선언')


class Worker(Person):
    def __init__(self, age):
        print('Worker 생성자')
        super().__init__(age)  # Worker의 부모클래스 생성자를 호출, age를 인수로 전달

    def wprintInfo(self):
        self.printInfo()


class Programmer(Worker):  # Worker의 자식클래스
    def __init__(self, age):
        print('Programmer 생성자')
        # super().__init__(age)     # Bound call 방식으로 부모클래스 생성자 호출
        Worker.__init__(self, age)  # UnBound call 방식으로 부모클래스 생성자 호출

    def pprintInfo(self):
        self.printInfo()  # printInfo()를 Programmer -> Worker -> Person 순으로 찾는다.
        super().printInfo()  # printInfo()를 Worker -> Person 순으로 찾는다.


person = Person('22')  # Person 객체 생성
person.printInfo()  # Person 클래스의 메서드를 호출
print()

empl = Employee()  # Employee 객체 생성
print(empl.say, empl.age, empl.subject)
empl.eprintInfo()
print()

worker = Worker('31')  # Worker 객체 생성
print(worker.say, worker.age)
worker.wprintInfo()
print()

pr = Programmer(33)  # Programmer 객체 생성
print(pr.say, pr.age)
print()

# class_exam 타입 확인하기
print(type(pr))

# 부모클래스의 이름을 확인하기
print(Programmer.__base__)
print(Worker.__base__)
print(Person.__base__)

# MRO(Method Resolution Order)로 메서드 결정 순서 확인하기. 먼저 출력된 값일수록 실행 우선순위가 높다.
print(Programmer.__mro__)
