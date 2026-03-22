class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start is not None:
            self.start.pref = None
        else:
            self.end = None
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_e = Node(val)
        if self.end is not None:
            self.end.nref = new_e
            new_e.pref = self.end
            self.end = new_e
        else:
            self.start = new_e
            self.end = new_e

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n < 0:
            print("Неверный ввод")
            return

        new_node = Node(val)
        if self.start is None:
            self.start = self.end = new_node
            return

        curr = self.start
        for i in range(n-1):
            if curr is None:
                break
            curr = curr.nref
        if curr is not None:
            prev = curr.pref
        else:
            prev = self.end

        next_node = curr
        new_node.pref = prev
        new_node.nref = next_node
        if prev is not None:
            prev.nref = new_node
        if next_node is not None:
            next_node.pref = new_node
        if prev is None:
            self.start = new_node
        if next_node is None:
            self.end = new_node

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        curr = self.start
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.nref
        print()


q = Queue()
q.push(10)
q.push(20)
q.push(30)
q.print()
q.insert(1, 821)
q.print()
print(q.pop())
q.print()
