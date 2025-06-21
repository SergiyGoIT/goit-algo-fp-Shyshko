# Реалізація однозв'язного списку з операціями реверсування, сортування та об'єднання

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додає вузол із заданими даними в кінець списку."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        """Реверсує однозв'язний список, змінюючи вказівники між вузлами."""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо наступний вузол
            current.next = prev       # Змінюємо вказівник
            prev = current            # Переміщуємо prev на поточний
            current = next_node       # Переходимо до наступного
        self.head = prev

    def merge_sort(self):
        """Сортує однозв'язний список за допомогою сортування злиттям."""
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """Допоміжна функція для сортування злиттям: рекурсивно розбиває і об'єднує."""
        if not head or not head.next:
            return head

        # Розбиваємо список на дві половини
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None

        # Рекурсивно сортуємо обидві половини
        left = self._merge_sort(head)
        right = self._merge_sort(second_half)

        # Об'єднуємо відсортовані половини
        return self._merge(left, right)

    def _merge(self, left, right):
        """Об'єднує два відсортовані списки в один відсортований."""
        dummy = Node(0)
        current = dummy

        while left and right:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Додаємо залишки
        current.next = left if left else right
        return dummy.next

    def merge_sorted_lists(self, other_list):
        """Об'єднує інший відсортований список із поточним, повертаючи новий відсортований список."""
        result = LinkedList()
        result.head = self._merge(self.head, other_list.head)
        return result

    def display(self):
        """Відображає елементи однозв'язного списку."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Порожній"

# Приклад використання та тестування
if __name__ == "__main__":
    # Створюємо та заповнюємо перший список
    list1 = LinkedList()
    for data in [4, 2, 1, 3]:
        list1.append(data)
    
    print("Початковий список 1:", list1.display())
    
    # Реверсуємо список
    list1.reverse()
    print("Реверсований список 1:", list1.display())
    
    # Сортуємо список
    list1.merge_sort()
    print("Відсортований список 1:", list1.display())
    
    # Створюємо та заповнюємо другий список
    list2 = LinkedList()
    for data in [5, 0, 6]:
        list2.append(data)
    list2.merge_sort()  # Переконуємося, що список 2 відсортований
    print("Відсортований список 2:", list2.display())
    
    # Об'єднуємо два відсортовані списки
    merged_list = list1.merge_sorted_lists(list2)
    print("Об'єднаний відсортований список:", merged_list.display())
