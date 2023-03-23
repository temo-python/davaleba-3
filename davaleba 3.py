# davaleba 1
class Celsius:
    def __init__(self, temperature):
        self.__temperature = temperature
    def get_temp(self):
        return self.__temperature
    def set_temp(self):
        self.__temperature = "new_temperature"
    def del_temp(self):
        self.__temperature
    temperature_property = property(get_temp, set_temp, del_temp)
name = Celsius(10)
name1 = Celsius(15)
print(name.temperature_property)
print(name1.temperature_property)
# davaleba 2
class Bank_account:
    def __init__(self, account_name, balance = 0):
        self.__account_name = account_name
        self.__balance = balance
    def get_accountname(self):
        return self.__account_name
    def set_acountname(self, accountname):
        self.__account_name = accountname
    def __str__(self):
        return f"გამარჯობა:{self.__account_name}, თქვენ ანგარიშზე გაქვთ:{self.__balance}ლარი"
    def deposite(self, amount):
        self.__balance += amount
        print(f"თანხის შეტანა შესრულდა.ამჟამად თქვენ ანგარიშზე გაქვთ:{self.__balance}ლარი")
    def withdraw(self, amout):
        self.__balance -= amout
        print(f"თანხის გამოტანა შესრულებულია ამჟამად თქვენ ანგარიშზე გაქვთ:{self.__balance}ლარი")
name = Bank_account("თემო შონია")
name.deposite(input())
print(name.deposite)
name.withdraw(input())
print(name.withdraw)
print(name)
# davaleba 3
???
