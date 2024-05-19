import string
import sys


class Stack:
    def __init__(self):
        # Для хранения элементов в списке используем приватный атрибут.
        # На его приватность указывают два подчёркивания в имени.
        self.__items = []

    def push(self, item):
        """Добавить элемент в стек."""
        self.__items.append(item)

    def pop(self):
        """Взять элемент из стека."""
        return self.__items.pop()

    def peek(self):
        """Посмотреть последний элемент без изъятия."""
        return self.__items[-1]

    def size(self):
        """Вернуть размер стека."""
        return len(self.__items)


def decode_str(encoded_str):
    stack = Stack()
    current_num = 0
    current_str = ''
    numbers = set(string.digits)
    for char in encoded_str:
        if char in numbers:
            current_num = int(char)
        elif char == '[':
            stack.push(current_num)
            stack.push(current_str)
            current_num = 0
            current_str = ''
        elif char == ']':
            prev_str = stack.pop()
            prev_num = stack.pop()
            current_str = prev_str + current_str * prev_num
        else:
            current_str += char
    return current_str


if __name__ == '__main__':
    encoded_str = sys.stdin.readline().rstrip()
    print(decode_str(encoded_str))
