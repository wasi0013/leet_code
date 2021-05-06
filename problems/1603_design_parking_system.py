class ParkingSystem:
    big, medium, small = 0, 0, 0

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 3 and self.small:
            self.small -= 1
            return True
        elif carType == 2 and self.medium:
            self.medium -= 1
            return True
        elif carType == 1 and self.big:
            self.big -= 1
            return True
