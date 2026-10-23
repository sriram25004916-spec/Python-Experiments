class car():
    def four(self):
        print("4 wheels")

class bike(car):
    def four(self):
        super().four()
        print("2 wheels")

obj1=bike()
obj1.four()

