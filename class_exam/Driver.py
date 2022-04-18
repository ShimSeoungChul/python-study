from class_exam.Car import Car

tom = Car('ted')
tom.turnHandle(10)  # tom이 우회전
print(tom.ownerName + '의 회전량:' + tom.turnShow + str(tom.handle.quantity))

robin = Car('robin')
robin.turnHandle(-25)  # robin이 우회전
print(robin.ownerName + '의 회전량:' + robin.turnShow + str(robin.handle.quantity))
