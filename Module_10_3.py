# Домашнее задание по теме "Потоки на классах"
# ***************************************************************************************
# Задача "За честь и отвагу!":
#   Создайте класс Knight, наследованный от Thread, объекты которого
#   будут обладать следующими свойствами:
#       - Атрибут name - имя рыцаря. (str)
#       - Атрибут power - сила рыцаря. (int)
#
#   А также метод run, в котором рыцарь будет сражаться с врагами:
#       При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
#       Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
#       В процессе сражения количество врагов уменьшается на power текущего рыцаря.
#       По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>...,
#       осталось <кол-во воинов> воинов."
#       После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней>

# Пункты задачи:
# Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight.
# Выведите на экран строку об окончании битв.
# ****************************************************************************************

import random
import time
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for __ in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            print( f'Пополнение: {amount}. Баланс: {self.balance}')
            if self.balance >=500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            if amount <= self.balance:
                print(f'Снятие: {amount}. Баланс: {self.balance}')

            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

def start():
    bk = Bank()

    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()


if __name__ == '__main__':
    start()
