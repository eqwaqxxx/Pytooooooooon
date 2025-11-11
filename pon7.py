rastoianie = float(input("Введите расстояние вашего пути в километрах: "))
litra = float(input("Cколько литров ест машина на 100 км: "))
rub_Za_litra = 49.5
print(f"Нужно бензина: { rastoianie * ( litra / 100 ):.2f} ")
print(f"стоимост: { rastoianie * ( litra / 100 ) * rub_Za_litra :.2f} ")
