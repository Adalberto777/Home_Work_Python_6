# Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200. Использовать comprehensions
from math import sqrt


# my_lst = []
# for i in range(1, int(sqrt(200)), +2): 
#     my_lst.append(i)


my_lst = [i for i in range(1, int(sqrt(200)), +2)]

print(my_lst)