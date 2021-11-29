#1.у пользователя запрашивается количество билетов
#2.для каждого билета запрашивается возраст посетителя
#Если менее 18 лет, то бесплатно. От 18 до 25 лет — 990 руб.От 25 лет 1390 руб.
#3. В результате программы выводится сумма к оплате. 
#если регистрирует больше трёх человек 10% скидку на стоимость заказа.

# accepting visitors quantity
cnt = int(input('How many ppl to register?\n'))
# accepting visitors ages according to their quantity
A = [int(input(f'age of person {i}')) for i in range(1,cnt+1) ]
# gathering a list of tickets' prices
C = [ 1390.0 for i in A if i >= 25] + [ 990.0 for i in A if 18 <= i < 25] + [ 0.0 for i in A if i < 18]
# printing the total summ
# in case of 4+ visitors applying 10% discount to the total bill
if cnt > 3 :
    print(f'Total summ to be paid: {sum(C)*0.9}')
else :    
    print(f'Total summ to be paid: {sum(C)}')
