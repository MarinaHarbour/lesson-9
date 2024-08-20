my_list = [42, 69, 322, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):
    element = my_list[index]
    element = int(input('Введите число: '))
    if index < 0:
        break
    print(element)
    index += 1
    if element > 0:
        continue
    elif element < 0:
        break


