"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

# В целях оптимизации использования памяти для построения дерева использовал namedtuple вместо dict.
from collections import Counter, deque, namedtuple


class HuffmanCode:
    def __init__(self, row):
        self.row = row
        self.code_table = dict()
        self.code_table_nt = dict()
        # self.huffman_code(self.get_tree())
        self.huffman_code_nt(self.get_tree_nt())

    def count_val_sorted(self):
        return deque(sorted(Counter(self.row).items(),
                            key=lambda item: item[1]))

    # def get_tree(self):
    #     value_count_sorted = self.count_val_sorted().copy()
    #     value_count_sorted_nt = self.count_val_sorted().copy()
    #     New_elem_1 = namedtuple('New_elem_1', 'left right')
    #     if len(value_count_sorted) != 1:
    #         while len(value_count_sorted) > 1:
    #             weight = value_count_sorted[0][1] + value_count_sorted[1][1]
    #             new_elem = {0: value_count_sorted.popleft()[0],
    #                         1: value_count_sorted.popleft()[0]}
    #             new_elem_1 = New_elem_1(value_count_sorted_nt.popleft()[0], value_count_sorted_nt.popleft()[0])
    #             print(new_elem_1)
    #             for i, _count in enumerate(value_count_sorted):
    #                 if weight > _count[1]:
    #                     continue
    #                 else:
    #                     value_count_sorted.insert(i, (new_elem, weight))
    #                     value_count_sorted_nt.insert(i, (new_elem_1, weight))
    #                     break
    #             else:
    #                 value_count_sorted.append((new_elem, weight))
    #                 value_count_sorted_nt.append((new_elem_1, weight))
    #     else:
    #         weight = value_count_sorted[0][1]
    #         new_elem = {0: value_count_sorted.popleft()[0], 1: None}
    #         new_elem_1 = New_elem_1(value_count_sorted.popleft()[0], None)
    #         value_count_sorted.append((new_elem, weight))
    #         value_count_sorted_nt.append((new_elem_1, weight))
    #     return value_count_sorted[0][0]

    def get_tree_nt(self):
        value_count_sorted_nt = self.count_val_sorted().copy()
        New_elem_1 = namedtuple('New_elem_1', 'left right')
        if len(value_count_sorted_nt) != 1:
            while len(value_count_sorted_nt) > 1:
                weight = value_count_sorted_nt[0][1] + value_count_sorted_nt[1][1]
                new_elem_1 = New_elem_1(value_count_sorted_nt.popleft()[0], value_count_sorted_nt.popleft()[0])
                # print(new_elem_1)
                for i, _count in enumerate(value_count_sorted_nt):
                    if weight > _count[1]:
                        continue
                    else:
                        value_count_sorted_nt.insert(i, (new_elem_1, weight))
                        break
                else:
                    value_count_sorted_nt.append((new_elem_1, weight))
        else:
            weight = value_count_sorted_nt[0][1]
            new_elem_1 = New_elem_1(value_count_sorted_nt.popleft()[0], None)
            value_count_sorted_nt.append((new_elem_1, weight))
        return value_count_sorted_nt[0][0]

    # def huffman_code(self, some_tree, path=''):
    #     if not isinstance(some_tree, dict):
    #         self.code_table[some_tree] = path
    #     else:
    #         self.huffman_code(some_tree[0], path=f'{path}0')
    #
    #         self.huffman_code(some_tree[1], path=f'{path}1')

    def huffman_code_nt(self, some_tree, path=''):
        if type(some_tree) is str:
            self.code_table_nt[some_tree] = path
        else:
            self.huffman_code_nt(some_tree.left, path=f'{path}0')
            self.huffman_code_nt(some_tree.right, path=f'{path}1')

    def get_string_code(self):
        res = ''
        for el in self.row:
            res += self.code_table_nt[el]
        return res


string = 'beep bop beer!'
x = HuffmanCode(string)
print(f"Исходная строка:\n'{string}'")

tree = x.get_tree_nt()
print(f"Дерево:\n{tree}")


print(f"Таблица c кодами:\n{x.code_table_nt}")
code_str = x.get_string_code()
print(f"Строка кода после кодирования:\n{code_str}")
