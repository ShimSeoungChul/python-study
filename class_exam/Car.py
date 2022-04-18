from class_exam.Handle import Handle


class Car:
    turnShow = '정지'

    def __init__(self, ownerName):
        self.ownerName = ownerName  # 객체별로 ownerName 멤버를 기억
        self.handle = Handle()  # 클래스의 포함관계가 된다.

    def turnHandle(self, q):  # q 값으로 회전 방향을 결정
        if q > 0:
            self.turnShow = self.handle.rightTurn(q)
        elif q < 0:
            self.turnShow = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShow = '직진'
