# 1
def func1(a, b):

    if b == 0:
        print('Делить на ноль нельзя')
        input_numbers()
    else:
        с = a/b
        print(с)

def input_numbers():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    func1(first_number, second_number)

input_numbers()


# 2
def func2(name, last_name, years, city, email, phone):
    print(f"Пользователь {name} {last_name}, {years} года рождения из города {city}. Контактные данные: {email} {phone}")

name_input = input('Введите ваше имя: ')
last_name_input = input('Введите вашу фамилию: ')
city_input = input('Из какого вы города: ')
year_input = input('Ваш год рождения: ')
phone_input = input('Введите ваш номер телефона: ')
email_input = input('Введите ваш email: ')

func2(name=name_input, last_name=last_name_input, city=city_input, years=year_input, phone=phone_input, email=email_input)


# 3
def func3(number1, number2, number3):
    list_numbers = [number1, number2, number3]
    min_number = min(list_numbers)
    list_numbers.remove(min_number)
    print(list_numbers[0] + list_numbers[1])

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите второе число: '))
func3(first_number, second_number, third_number)


# 4
def func41(x, y):
    result = x ** y
    print(result)

def func42(x,y):
    result = 0
    for i in range(-1, y-1, -1):
        if result == 0:
            result = 1/x
        else:
            result = result * 1/x
    print(result)

number1 = float(input('Введите действительно положительное число: '))
number2 = int(input('Введите целое отрицательное число: '))
func41(number1, number2)
func42(number1, number2)


# 5
my_sum = 0

def func5(numbers):
    number_list = numbers.split(' ')
    this_sum = 0
    isBreak = False
    for element in number_list:
        if element.isnumeric():
            this_sum = this_sum + int(element)
        else:
            isBreak = True
            break

    return [this_sum, isBreak]

while True:
    string_numbers = input('Введите числа через пробел: ')
    result = func5(string_numbers)
    my_sum = my_sum + result[0]
    print(my_sum)
    if result[1] == True: break