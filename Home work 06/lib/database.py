import mysql.connector
import requests
from lib.settings import COVID19_URL
if __name__ == "__main__":
    db_manager

class db_manager:
    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID19")
        self.__cursor.execute("USE COVID19")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS global(id INT AUTO_INCREMENT PRIMARY KEY, NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT(10))")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS countries(id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(12), Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT(10), Date DATE)")
    def menu(self):
        exit = False
        while not exit:
            choise = int(input("1. Show COVID19 data base\n2. Search info by country name\n3. Search info by country code\n4. Top 10 by total confirmed\n5. Top 10 total recovered\n0. To exit\n===> "))
            if choise == 0:
                exit = True
                print("      11111        1¶111¶¶¶\n    ¶1    1¶      ¶1      ¶¶\n   ¶¶      1¶    ¶¶        ¶\n   ¶        ¶1   ¶         ¶\n  1¶        ¶¶  ¶¶        1¶\n  1¶        ¶¶  ¶         ¶1\n  1¶        ¶¶  ¶        1¶\n  1¶        ¶1 ¶¶        ¶1\n  1¶        ¶  ¶¶       ¶¶\n   ¶        ¶  ¶        ¶\n   ¶       1¶ 1¶       ¶1\n   ¶1    11¶¶1¶¶11    ¶¶\n   ¶¶ 1¶11      11¶¶1 ¶\n   1¶¶1            1¶¶1\n   1¶                1¶1\n  1¶                   ¶\n  ¶                    ¶¶\n 1¶   1¶¶¶           1¶¶¶\n 1¶   ¶¶¶¶            ¶¶¶1\n 1¶    ¶¶1              ¶1\n  ¶1        1¶¶¶¶¶¶¶¶   ¶  __BYE-BYE!\n  1¶       ¶¶¶¶¶¶¶¶¶1  ¶1 /\n   1¶     ¶¶¶¶¶¶¶¶¶¶  ¶¶                  1¶¶¶¶¶¶\n    1¶¶    ¶¶¶¶¶¶¶¶1 ¶¶ 1               ¶¶¶¶¶¶¶¶¶¶\n      1¶¶1          11 11¶¶¶          1¶¶¶¶¶¶1\n      1111                 ¶¶¶     1¶¶¶¶¶1\n     ¶1                      ¶¶ 11¶¶¶¶¶\n    ¶¶                   ¶¶    ¶¶¶    ¶¶\n    ¶1         1¶¶¶¶1     ¶¶1¶¶¶¶¶    ¶1\n    ¶¶        ¶¶¶¶¶1      ¶¶¶¶¶¶111 1¶\n    ¶¶  1¶   ¶¶¶¶¶     1¶¶¶¶¶¶    11\n     ¶   ¶¶1¶¶¶¶¶¶1 1¶¶¶¶¶1  ¶¶\n     ¶1   ¶¶¶¶¶¶1¶¶¶¶¶¶¶1     ¶¶\n 1¶¶¶¶¶    ¶¶¶ 1¶¶¶¶¶¶         ¶¶\n¶¶¶¶¶¶¶¶    1¶\n¶¶¶¶            ¶¶\n¶¶¶¶¶¶¶¶1    ¶¶   ¶¶   1         ¶¶\n¶¶¶¶¶¶¶¶¶¶    ¶1   1¶¶¶¶¶         ¶1\n¶¶¶¶¶¶¶ ¶¶¶1  ¶   111¶¶1          1¶\n¶¶¶¶¶¶¶¶1¶¶111  ¶¶¶11              ¶¶\n ¶¶¶¶¶¶¶¶¶¶   1¶¶        1¶¶        1¶\n  ¶¶¶¶¶¶¶¶¶  1¶1      111  ¶1       ¶1\n   ¶¶¶¶¶¶¶¶1¶¶¶   1¶11     ¶¶      1¶\n    1¶¶¶¶¶¶¶¶      ¶¶      1¶1    1¶\n      1¶¶¶¶         ¶1       11111\n          ¶         1¶\n           ¶¶11111111")
            elif choise == 1:
                answer = self.__update_data()
            elif choise == 2:
                answer = self.__search_data_country()
            elif choise == 3:
                answer = self.__search_data_country_code()
            elif choise == 4:
                answer = self.__top_ten()
            elif choise == 5:
                answer = self.__top_ten_recovered()

    def __update_data(self):
        covid_data = requests.get(COVID19_URL)
        covid_data = covid_data.json()
        self.__cursor.execute("TRUNCATE TABLE global")
        global_sql = "INSERT INTO global (NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered) VALUES(%s, %s, %s, %s, %s, %s)"
        global_values = (covid_data['Global']["NewConfirmed"],
              covid_data['Global']["TotalConfirmed"], covid_data['Global']["NewDeaths"], covid_data['Global']["TotalDeaths"], covid_data['Global']["NewRecovered"], covid_data['Global']["TotalRecovered"])
        self.__cursor.execute("TRUNCATE TABLE countries")
        self.__cursor.execute(global_sql, global_values)
        for item in covid_data['Countries']:
            countries_sql = "INSERT INTO countries (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            countries_values = item["Country"], item["CountryCode"], item["Slug"], item["NewConfirmed"], item["TotalConfirmed"], item["NewDeaths"], item["TotalDeaths"], item["NewRecovered"], item["TotalRecovered"], item["Date"]
            self.__cursor.execute(countries_sql, countries_values)
            print("Country COVID19 info:\n" + "Country:", countries_values[0], "\n" + "Country code:", countries_values[1], "\n" + "Slug:", countries_values[2], "\n" + "New confirmed:", countries_values[3],"\n" + "Total confirmed:", countries_values[4], "\n" + "New deaths:", countries_values[5], "\n" + "Total death:", countries_values[6], "\n" +"New recovered:", countries_values[7], "\n" + "Total recovered:", countries_values[8], "\n" + "Last data update:", countries_values[9], "\n")
        print("GLOBAL COVID19 info:\n" + "New confirmed:", global_values[0], "\n" + "Total global confirmed:", global_values[1], "\n" + "New deaths global:", global_values[2], "\n" + "Total global death:", global_values[3], "\n" +"New global recovered:", global_values[4], "\n" + "Total global recovered:", global_values[5], "\n")
        self.__db.commit()
        
    def __search_data_country(self):
        answer = input("To search COVID19 info by country, please enter country name:\n===> ")
        self.__cursor.execute("SELECT * FROM `countries` WHERE Country = '" + answer + "'")
        result = self.__cursor.fetchone()
        if result != None:
            print("COVID19 info by country name:\n" + "Country:", result[1], "\n" + "Country code:", result[2], "\n" + "New confirmed:", result[4], "\n" + "Total confirmed:", result[5], "\n" + "New deaths:", result[6], "\n" + "Total death:", result[7], "\n" +"New recovered:", result[8], "\n" + "Total recovered:", result[9], "\n" + "Last data update:", result[10], "\n")
        elif result == None:
            return print("\nWrong country name!\n")
        
    def __search_data_country_code(self):
        answer = input("To search COVID19 info by country code, please enter country code name:\n===> ")
        self.__cursor.execute("SELECT * FROM `countries` WHERE CountryCode = '" + answer + "'")
        result = self.__cursor.fetchone()
        if result != None:
            print("COVID19 info by country code:\n" + "Country:", result[1], "\n" + "Country code:", result[2], "\n" + "New confirmed:", result[4], "\n" + "Total confirmed:", result[5], "\n" + "New Deaths:", result[6], "\n" + "Total death:", result[7], "\n" +"New recovered:", result[8], "\n" + "Total recovered:", result[9], "\n" + "Last data update:", result[10], "\n")
        elif result == None:
            return print("\nWrong country code!\n")
    def __top_ten(self):
        self.__cursor.execute("SELECT Country, TotalConfirmed FROM `countries` ORDER BY TotalConfirmed DESC LIMIT 10")
        result = self.__cursor.fetchall()
        print("top 10 of total confirmed with COVID-19:")
        position = 0
        for i in result:
            position +=1
            print(position, "Country:", i[0],"\nTotal confirmed:", i[1],"\n")

    def __top_ten_recovered(self):
        self.__cursor.execute("SELECT Country, TotalRecovered FROM `countries` ORDER BY TotalRecovered DESC LIMIT 10")
        result = self.__cursor.fetchall()
        print("top 10 of total recovered:")
        position = 0
        for i in result:
            position +=1
            print(position,"Country:", i[0],"\nTotal recovered:", i[1],"\n")