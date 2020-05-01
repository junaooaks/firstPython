class Account:

    def __init__(self, number):
        self.number = number
        # __ define atribut private
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):

        if self.__total <= 0:
            return "Your don't have money your account"

        else:
            self.__total -= value

        return self.__total

    def get_total(self):
        return self.__total
