tickets = int(input("Введите количество билетов, которые хотите приобрести на мероприятие:"))
coupon = 10
cost = 0

for i in range(tickets):
    age = int(input("возраст посетителя %d:" % (i + 1)))

    if age >= 18 and age < 25:
        cost += 990
    elif age >= 25:
        cost += 1390
    else:
        cost += 0

if tickets > 3:
    cost = cost - coupon / 100 * cost

print("сумма к оплате", cost)