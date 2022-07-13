# 1
first_list = ['Programm', 66.35, True, 11, None, [7, 2, 14]]
for element in first_list:
    print(type(element))

# 2
second_list = []
while True:
    item = input('Введите элемент списка: ')
    if item != '':
            second_list.append(item)
    else:
        break

print(second_list)

for i in range(len(second_list)):
    if i%2 == 1:
        second_list.insert(i-1, second_list[i])
        second_list.pop(i+1)

print(second_list)


# 3
third_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
month = input('Введите месяц в виде целого числа от 1 до 12: ')
print(third_list[int(month)-1])


# 4
fourth_string = input('Введите cтроку: ')
fourth_list = fourth_string.split()
for i, el in enumerate(fourth_list):
    print(f"{i}. {el[:10]}")


# 5
fifth_list = [9, 6, 4, 4, 2]
new_number = int(input('Введите число: '))

for i, el in enumerate(fifth_list):
    if new_number > el:
        fifth_list.insert(i, new_number)
        break
    if i+1 == len(fifth_list):
        fifth_list.append(new_number)
        break

print(fifth_list)


# 6
sixth_list = []
count = 0
while True:
    name_item = input('Введите название товара: ')
    price_item = int(input('Введите цену товара: '))
    count_item = int(input('Введите количество товара: '))
    measure_item = input('Введите единицу измерения товара: ')

    sixth_list.append((count, {'name': name_item, 'price': price_item, 'count': count_item, 'measure': measure_item}))

    count += 1
    next_item = input('Продолжить заполнение товаров? (y/n): ')
    if next_item == 'n':
        break

print(sixth_list)

analytics = dict()
keys_item = sixth_list[0][1].keys()
for el in keys_item:
    values_key = []
    for elm in sixth_list:
        values_key.append(elm[1].get(el))
    analytics.update({el: values_key})

print(analytics)

