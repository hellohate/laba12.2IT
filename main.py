from linkedlist import DoublyLinkedList, split_list


def main():

    original_list = DoublyLinkedList()
    elements = [10, -3, 5, -9, 12, -7, 3, -1]

    for elem in elements:
        original_list.append(elem)

    print("Original List:")
    original_list.display()

    l1, l2 = split_list(original_list)

    print("Positive List (L1):")
    l1.display()

    print("Negative List (L2):")
    l2.display()


if __name__ == "__main__":
    main()
