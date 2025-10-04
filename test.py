# Функция для перевода температуры из Цельсия в Фаренгейт
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

# Запрашиваем у пользователя температуру в градусах Цельсия
celsius_temperature = float(input("Введите температуру в градусах Цельсия: "))

# Преобразуем значение и выводим результат
fahrenheit_temperature = convert_celsius_to_fahrenheit(celsius_temperature)
print(f"Температура {celsius_temperature:.2f}°C соответствует {fahrenheit_temperature:.2f}°F")

age = int(input("Введите ваш возраст: "))
if age <= 18:
   category = "Молодой"
elif 18 < age <= 60:
    category = "Взрослый"
else:
    category = "Пожилой"
print(f"Ваша категория возраста это: {category}")

#3 задание

chislo = int(input("Введите целое число, которые вы хотите проверить: "))
if chislo % 3 == 0 and chislo % 5 == 0:
    print ("Ваше число делится на оба значения")
else:
    print ("Ваше число не делится ни на одно из этих значений")

#4 задание

znachenie = int(input("Введите значение: "))
if znachenie % 7 == 0 and znachenie % 5 != 0:
    print("Ваше значение делится на 7, но не делится на 5")
else:
    print(" Ваше значение ошибочно")

#5 задание
# Запрашиваем ввод числа у пользователя
n = int(input("Введите число: "))

# Создаю цилк от 1 до n включительно
for i in range(1, n + 1):
    if i % 3 != 0:
        print(i)

#6 задание

for num in range(1, 101):
    if num % 2 == 0:
        if num > 50:
            break
        print(num)

#7 задание
# Цикл по числам от 1 до 10
for number in range(1, 11):
    if number == 6:
        continue
    print(number)

#8 задание

number = int(input("Введите число: "))
for i in range(1, 21):
    if i == number:
        print(f"Встречено число {number}, прекращаю работу.")
        break
    else:
        print(i)

#9 задание

n = int(input("Введите положительное число: "))

summa = 0
znachenie = 1
while znachenie <= n:
    summa += znachenie # Добавляем текущее число к общей сумме
    znachenie += 1          # Переход к следующему числу

# Вывод результата
print(f"Сумма всех чисел от 1 до {n}: {summa}")

#10 задание

# Получаем число от пользователя
number = int(input("Введите целое число: "))
count = 0

# Создаем копию числа, чтобы не изменять исходное значение
temp_number = abs(number)

if temp_number == 0:
    count = 1
else:
    # Циклом отсчитываем каждую цифру
    while temp_number > 0:
        temp_number //= 10
        count += 1

print(f"Введённое число состоит из {count} цифр.")

#11 задание

sum_even = 0
i = 2  # Начинаем с первого чётного числа

while i <= 100:
    sum_even += i
    i += 2  # Переходим к следующему чётному числу

print(f"Сумма всех чётных чисел до 100 равна {sum_even}.")

#12 задание

num = 10

while num >= 1:
    print(num)
    num -= 1

#13задание

max_num = None  # Переменная для хранения наибольшего числа

while True:
    number = float(input("Введите число (для завершения введите 0): "))
    
    if number == 0:
        break  # Завершаем цикл, если введена цифра 0
        
    if max_num is None or number > max_num:
        max_num = number  # Обновляем максимум, если ввели большее число

if max_num is not None:
    print(f"Наибольшее введённое число: {max_num}")
else:
    print("Вы ничего не ввели кроме нуля.")

#14задание

for num in range(1, 11):
    if num % 3 == 0 and num % 5 == 0:
        print(num)


#15задание

for num in range(1, 101):
    if num % 3 == 0 or num % 5 == 0:
        continue  # Прерывание итерации и переход к следующей
    print(num)
#Классная работа

#1 задание

n=list(range(1,21))
print(n)
#2
numbers = [1, 2, 2, 7, 5, 8, 3, 2]
summ = 0
prod = 1
for num in numbers:
    summ += num
    prod *= num
print(summ)
print(prod)
#3
n=[1,2,3,4,5,6,7,8,9]
b=[]
for num in n:
    if num%2==0:
        b.append(num)
print(b)
#4
n=int(input('Введите число:'))
for num in range(1,n+1):
    if num%3==0:
        print(num)
#5
n=[14,29,-11,47,6,111]
b=sorted(n)
print(b)
print('минимальное число в списке:',b[0])
print('максимальное число в списке:',b[-1])
#6
n=[-4,4,2,112,15,11,67,-16,15]
b=[]
for num in n:
    if num not in b:
        b.append(num)
print(len(b))
print(b)
print(n)
#7
n=[-1,-2,-3,1,2,3]
for i in range(len(n)):
    if n[i]<0:
        n[i]=0
print(n)
#8
n=[4, 13, 96, 6, 3, 17, -8]
min_index=0
max_index=0
for i, num in enumerate(n):
    if num < n[min_index]:
        min_index = i
    if num > n[max_index]:
        max_index = i

n[min_index], n[max_index] = n[max_index], n[min_index]
print(numbers)
#9
n=[5,12,7,3,-2,20,10]
print(sorted(n))
#10
a=[1,2,3]
b=[4,5,6]
c=[]
c.extend(a)
c.extend(b)
print(c)
#11
n=[20,10,44,51,67,9]
for num in n:
    if num >50:
        print(num)
#12       
n=[2,3,5,8,4]
m=[]
for num in n:
    b=num**2
    m.append(b)
print(m)
#13
n=[1,2,3,4,5,6]
i=[]
for num in n:
    if num %2==0:
        i.append(num+10)
    else:
        i.append(num)
print(i)
#14
n=[3,7,2,5,10]
sredny_nuumber=(3+7+2+5+10)/5
for i in range(len(n)):
    if n[i]<sredny_number:
        n[i]=-1
print(n)
print(sredny_number)


