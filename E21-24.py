# Текстовый файл состоит не более чем из 1e6 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
# Для выполнения этого задания следует написать программу.
import random  # импортируем библиотеку рандом
random.seed()  # инициализация генератора случайных чисел

def createRandomFile(charNum): #генератор файлов с символами
    with open('e24.txt','w') as f:
        for i in range(0,charNum):
            r=random.randint(0,2)
            if r == 0:
                f.write('X')
            elif r==1:
                f.write('Y')
            else:
                f.write('Z')

createRandomFile(random.randint(0,1000000))
with open('e24.txt','r') as f:
    file=f.readline()
count=1; #для промежуточного счета
mx=1;    #максимальная длина цепочки
for i in range(1,len(file)):
    if file[i]!=file[i-1]:
        count+=1
        mx=max(count,mx)
    else:
        count=1

print(file)
print(mx)