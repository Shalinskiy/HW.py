revenue = int(input("Введите выручку своей фирмы: "))
costs = int(input("Введите издержки своей фирмы: "))
profit = revenue - costs
margin = (profit / revenue) * 0.10

if profit > costs:
    print("Ваша прибыль составляет:", profit, '$')
    print(f"Рентабельность выручки составляет: {margin:.2f}%")
    workers = int(input("Сколько сотрудников у вас работают? "))
    pw = profit / workers
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет: {pw:.1f}")
elif revenue == costs:
    print("Вы работаете в ноль")
elif profit < costs:
    print("Ваш убыток составляет:", profit, '$')