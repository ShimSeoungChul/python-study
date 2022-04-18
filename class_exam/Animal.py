class Animal:  # 부모클래스
    def move(self):
        print('움직이는 생물')


class Dog(Animal):  # Animal 클래스를 상속
    def my(self):  # Dog 클래스의 고유 메서드
        print('강아지')


class Horse(Animal):  # Animal 클래스를 상속
    pass  # Horse는 자체 멤버가 없는 클래스가 된다.


dog = Dog()
dog.my()  # Dog의 고유 메서드 수행
dog.move()  # Dog의 부모인 Animal의 메서드를 수행

horse = Horse()
horse.move()  # Horse의 부모인 Animal의 메서드를 수행
