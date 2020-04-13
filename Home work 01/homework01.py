time = int(input("Введіть годину у 24-годинному форматі (1-24):\n"))
if time <= 3 and time > 0 or time == 24 :
    print("Good night")
elif time >= 4 and time < 12:
    print("Good morning")
elif time >= 12 and time < 18:
    print("Good day")
elif time >= 18 and time < 24:
    print("Good evening")
else: print ("Година введена не корректно!")

altron2 = int(input("Конвертер довжини Altron 2.0 запущено. Оберіть дію:\nВведіть 1 для конвертацію сантиметрів в дюйми\nВведіть 2 для конвертації дюймів в сантиметри\n"))
if altron2 == 1:
    distance = int(input("Введіть довжину у цифровому форматі\n"))
    result = distance * 2.54
    print(distance, 'д =', result, 'cm')
elif altron2 == 2:
    distance = int(input("Введіть довжину у цифровому форматі\n"))
    result = distance / 2.54
    print(distance, 'cm =', result, 'д')
elif altron2 != 1 or altron2 != 2:
    print ("Форма заповнена не корректно!")

temperature = int(input("Конвертер температури Церебро запущено\nВведіть 1 для конвертації градусів Цельсія у градуси Фаренгейта\nВведіть 2 для конвертації градусів Фаренгейта у градуси Цельсія\n"))
if temperature == 1:
    tData = int(input("Введіть температуру у цифровому форматі\n"))
    tResult = round((tData-32) * (5/9))
    print(tData, '℉ =', tResult, 'C')
elif temperature == 2:
    tData = int(input("Введіть температуру у цифровому форматі\n"))
    tResult = round(tData * (9/5) + 32)
    print(tData, '℃  =', tResult, 'F')
elif temperature != 1 or temperature != 2:
    print ("Форма заповнена не корректно!")

print("Введіть вісім цілих чисел")
num1 = int(input("Введіть перше число\n"))
num2 = int(input("Введіть друге число\n"))
num3 = int(input("Введіть третє число\n"))
num4 = int(input("Введіть четверте число\n"))
num5 = int(input("Введіть п'яте число\n"))
num6 = int(input("Введіть шосте число\n"))
num7 = int(input("Введіть сьоме число\n"))
num8 = int(input("Введіть восьме число\n"))
mathResult1 = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
mathResult2 = mathResult1 / 8
print("Сума введених вами чисел =", mathResult1, "Середнє арифметичне ваших чисел =", mathResult2)

import random
count = 0
lilNum = 20
bigNum = -10

while count < 8:
    count = count + 1
    randomNum = random.randrange(-10, 20)
    if randomNum < lilNum:
        lilNum = randomNum
    if randomNum > bigNum:
        bigNum = randomNum
print("Найменша температура за тиждень:", lilNum, "℃ \nНайвища температура за тиждень:", bigNum, "℃")