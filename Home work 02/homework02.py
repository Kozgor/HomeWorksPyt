from my_modules.calc import sum, min, mnozh, dil

def calculator():
    choise = int(input("############################################################\n### Пайтон калькулятор. Натисніть клавішу для вибору дії ###\n############################################################\n####################### 1-додавання ########################\n####################### 2-віднімання #######################\n######################## 3-множення ########################\n######################### 4-ділення ########################\n#################### або ctrl+c для виходу #################\n############################################################\n"))
    if choise != 1 and choise != 2 and choise != 3 and choise != 4:
        print("################# !Я не знаю такої команди #################\n#################### Спробуйте ще раз! #####################\n")
        calculator()
    
    else:
        a = float(input("Введіть перше число\n"))
        while choise == 1:
            b = float(input("Введіть число\n"))
            res = sum(a, b)
            a = res
            print("############################################################\nРезультат =",
                    res, "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while choise == 2:
            b = float(input(" Введіть число\n"))
            res = min(a, b)
            a = res
            print("############################################################\nРезультат =",
                    res, "\n------------------------------------------------------------")
        while choise == 3:
            b = float(input("Введіть число\n"))
            res = 1
            if a != 0 and b != 0 and res != 0:
                res = mnozh(a, b)
                a = res
                print("############################################################\nРезультат =",
                        res, "\n************************************************************")
            else:
                print('############################################################\n############# Множення на нуль. Результат = 0.##############\n############################################################')
                calculator()
        while choise == 4:
            b = float(input("Введіть число\n"))
            res = 1
            if a !=0 and b != 0 and res != 0:
                res = dil(a, b)
                a = res
                print("############################################################\nРезультат =",
                        res, "\n////////////////////////////////////////////////////////////\n")
            else:
                print('############################################################\n############# Ділення на нуль. Результат = 0. ##############\n############################################################\n')
                calculator()
calculator()
