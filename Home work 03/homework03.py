import datetime
import random

class Discount:
    def __init__(self, number, dateToday, totalPurchases):
        self.__number= number
        self.__dateToday = dateToday
        self.__totalPurchases = totalPurchases

    @property
    def discount(self):
        return self.__discount

    @property
    def totalPurchases(self):
        return self.__totalPurchases

    @totalPurchases.setter
    def totalPurchases(self, newTotal):
        self.__totalPurchases = newTotal    
    
    def discount(self):
        if self.__totalPurchases < 1000:
            newNum = 1
            print("Buy the product for the amount more then", 1000 - self.__totalPurchases, "hrn to increase the percentage of your discount")
        elif self.__totalPurchases >= 1000 and self.__totalPurchases < 2000:
            newNum = 2
            print("Buy the product for the amount more then", 2000 - self.__totalPurchases, "hrn to increase the percentage of your discount")
        elif self.__totalPurchases >= 2000 and self.__totalPurchases < 3000:
            newNum = 3
            print("Buy the product for the amount more then", 3000 - self.__totalPurchases, "hrn to increase the percentage of your discount")
        elif self.__totalPurchases >= 3000 and self.__totalPurchases < 4000:
            newNum = 4
            print("Buy the product for the amount more then", 4000 - self.__totalPurchases, "hrn to increase the percentage of your discount")
        elif self.__totalPurchases > 4000:
            newNum = 5
            print("You have maximum percentage discount")
        discountValue = self.__totalPurchases*newNum/100
        totalPrise = self.__totalPurchases - discountValue
        print("You have:", newNum, "% discound")
        print("Total prise is:", totalPrise, "hrn")

pythonShop = {'apples': 50, 'potatoes': 70, 'milk': 35, 'sugar': 120, 'water': 20, 'bread': 20, 'salt': 45, 'carrot': 40, 'meat': 200, 'fish': 150, 'cheesee': 120, 'vine': 200, 'beer': 50, 'whiskey': 550}

print("Welcome to Python grosery store!\nPlease read instructions below\nand take a shopping cart\n☺ Enjoy your shopping ☺")

shoppingCart=[]
insideCart=[]

while True:
    print("======= Python shop price =======")
    for key, value in pythonShop.items():
        print(key, "=", value,'hrn')
    print("Enter buy to buy selected products\n===== Or enter exit to exit =====")
    choise = input()
    if choise in pythonShop.keys():
        shoppingCart.append(pythonShop[choise])
        insideCart.append(choise)
        print(choise, 'has been added to your shopping cart!\nNow you have:', ", ".join(insideCart))
    elif choise not in pythonShop.keys() and choise != 'exit' and choise != 'buy':
        print('Incorrect name of product')
    elif choise == 'exit':
        break
    elif choise == 'buy':
        def shoppingResult(shoppingCart):
            result = 0
            for i in shoppingCart:
                result = result + i
            return result
        newCard = Discount(random.randint(1000,9999), datetime.date.today(), shoppingResult(shoppingCart))
        newCard.discount()
        break
print("Thank you for visiting Python shop!")