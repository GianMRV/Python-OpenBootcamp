from functools import reduce

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16]
num_impar = filter(lambda x: x % 2 !=0, list_num)
sum = reduce(lambda a,b: a + b, num_impar)
print(sum)