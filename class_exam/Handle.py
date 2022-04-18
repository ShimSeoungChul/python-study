class Handle:
    quantity = 0  # 회전량을 기억

    def leftTurn(self, quantity):  # 좌회전일 때 수행
        self.quantity = quantity
        return '좌회전'

    def rightTurn(self, quantity):  # 우회전일 때 수행
        self.quantity = quantity
        return '우회전'
