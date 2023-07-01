#Задача 24
n = int(input('Введите количество кустов: '))
berry = list()
for i in range(n):
    x = int(input('Введите какое количество ягод выросло на кусте: '))
    berry.append(x)
berry_count = list()
for i in range(len(berry) - 1):
    berry_count.append(berry[i-1] + berry[i] + berry[i+1])
berry_count.append(berry[-2] + berry[-1] + berry[0])
print(max(berry_count))