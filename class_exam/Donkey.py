class Donkey:
    data = "당나귀 최고"

    def skill(self):
        print("당나귀: 짐나르기")

class Horse:
    def skill(self):
        print("말: 달리기")

    def hobby(self):
        print("말은 달리기가 취기")


class Mule1(Donkey, Horse):   # Donkey, Horse 순으로 다중 상속
    pass


class Mule2(Horse, Donkey): # Horse, Donkey 순으로 다중 상속
    def play(self):
        print("노새 고유 메서드")

    def hobby(self):    # 부모 메서드를 오버라이드
        print("노새는 걷기를 즐김")

    def showHobby(self):
        self.hobby()    # 클래스의 멤버 호출은 self
        super().hobby() # 부모 멤버 호출 시 super()

    def showData(self):
        print(self.data)    # class_exam 자신의 멤버부터 호출
        print(super().data) # 부모 멤버를 호출

mu1 = Mule1()
print(mu1.data) # Donkey의 멤버변수를 참조
mu1.skill()     # Donkey의 메서드를 수행
mu1.hobby()     # Horse의 메서드를 수행
print()

mu2 = Mule2()
mu2.skill()     # Horse의 메서드를 수행
mu2.hobby()     # Mule2의 메서드를 수행
mu2.play()      # Mule2의 메서드를 수행
mu2.showHobby()
mu2.showData()