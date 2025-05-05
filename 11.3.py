import csv
file = open('products.csv', encoding='utf-8')
summa=0
shopping_list=[]
reader = csv.DictReader(file)

for row in reader:
    product = row["Продукт"]
    kol_vo= int(row["Количество"])
    price = int(row["Цена"])
    cost =price*kol_vo
    summa+=cost
    shopping_list.append(f"{product} - {kol_vo} шт. за {price} руб.")

print("Нужно купить:")
for i in shopping_list:
    print(i)
print(f"Итоговая сумма: {summa} руб.")



