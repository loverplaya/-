import random

rost = [random.randint(155,200) for i in range(15)]
familia = ["Столов","Стулов","Стенов","Полов","Листков","Наушников","Телефонов","Иванов","Петров","Друнов","Ч","Фог","Сладсоть","Гадость","Друнность"]
sred = sum(rost)/len(rost)
max_rost = max(rost)
samiy = rost.index(max_rost)
print(samiy)
print("Средний рост",sred, "Самый высокий",max_rost,familia[samiy])
