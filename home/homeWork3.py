class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на ваш счет: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other_balance):
        self._balance += other_balance

# Пример использования класса Bank

account1 = Bank("Beka", 0)
account1.moneyX()
print("Баланс после добавления:", account1._balance)

account1._kill()
print("Баланс после обнуления:", account1._balance)

# account1._jackpot()  # Нельзя прямо вызвать скрытый метод

account2 = Bank("Ali", 25)
account2._merge_balance(account2._balance + account1._balance)
print("Баланс после объединения счетов:", account2._balance + account1._balance)
