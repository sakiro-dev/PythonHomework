class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_e = Node(val)
        new_e.pref = self.end
        self.end = new_e

    def print(self):
        """
        вывод на печать содержимого стека
        """
        curr = self.end
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.pref
        print()


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print()
print(stack.pop())
stack.print()
print(stack.pop())
stack.print()
