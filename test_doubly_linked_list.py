import unittest
from unittest.mock import patch
from io import StringIO
from linkedlist import DoublyLinkedList, split_list


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    @patch('sys.stdout', new_callable=StringIO)
    def test_append_and_display(self, mock_stdout):
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            self.dll.append(elem)

        expected_output = "1 2 3 4 5 \n"

        self.dll.display()

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_split_list(self):
        elements = [10, -3, 5, -9, 12, -7, 3, -1]
        for elem in elements:
            self.dll.append(elem)

        l1, l2 = split_list(self.dll)

        expected_l1 = [10, 5, 12, 3]
        expected_l2 = [-3, -9, -7, -1]

        self.assertEqual(list_from_dll(l1), expected_l1)
        self.assertEqual(list_from_dll(l2), expected_l2)


def list_from_dll(dll):
    result = []
    current = dll.head
    while current:
        result.append(current.data)
        current = current.next
    return result


if __name__ == '__main__':
    unittest.main()
