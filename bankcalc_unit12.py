##### UniT 12 ########
money = int(input("insert deposit sum: "))
deposit = []
for i in list(per_cent.values()):
    s=int(round(money+i/100*money))
    deposit.append(s)
"""задание №1"""
print(deposit)
deposit_output = {'ТКБ': deposit[0], 'СКБ': deposit[1], 'ВТБ': deposit[2], 'СБЕР': deposit[3]}
#print(deposit_output)
"""Задание №2"""
print("максимальный доход: "+ str(max(deposit_output.values())))
