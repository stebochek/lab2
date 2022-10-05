def esc(code):
    return f'\u001b[48;5;{code}m'
GREEN = esc(28)
YELLOW = esc(11)
RED = esc(160)
BLACK = esc(0)
WHITE = esc(7)
END = '\u001b[0m'
import csv
import os
import time

#БЛОК - ФЛАГ

for i in range(6):
    if i <= 2:
        print(f'{GREEN}{" " * 9}{YELLOW}{" " * 18}{END}')
    else:
        print(f'{GREEN}{" " * 9}{RED}{" " * 18}{END}')

#БЛОК - УЗОР

pixel = f'{BLACK}{"  "}{END}'
uzor0 = f'{"  " * 3}{pixel}'
print(uzor0*100)
uzor1 = f'{pixel * 3}{"  "}'
print(f'{"  " * 2}{uzor1*100}')
uzor2 = f'{pixel * 4}'
print(f'{"  "}{pixel}{uzor2*100}')
print(f'{"  " * 2}{uzor1*100}')
print(uzor0*100)

# БЛОК - ГРАФИК

for x in range(10, -1, -1):
    if 1 < x < 10:
        print(f'{x}| {WHITE}{"  " * (x - 2)}{RED}{"  "}{WHITE}{"  " * (12 - x)}{END}')
    elif x >= 10:
        print(f'{x}|{WHITE}{"  " * (x - 2)}{RED}{"  "}{WHITE}{"  " * (12 - x)}{END}')
    elif x == 1:
        print(f'1| {WHITE}{"  " * 11}{END}')
    elif x == 0:
        print(f'{"0| "}{"1|2|3|4|5|6|7|8|9|10|11"}{END}')

# БЛОК - ДИАГРАММА


count1 = 0
count2 = 0
a = 0
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    for row in table:
        if a != 0:
            if float(row[7]) <= 150.0:
                count1+=1
            else:
                count2+=1
        a+=1
percent1 = round((count1/(count2+count1))*100)
percent2 = round((count2/(count2+count1))*100)

if percent1%10>=5:
    percent1+=10-percent1%10
else:
    percent1-=percent1%10
if percent2%10>=5:
    percent2+=10-percent2%10
else:
    percent2-=percent2%10
percent1 //= 10
percent2 //= 10
RED = esc(160)
WHITE = esc(7)
END = '\u001b[0m'

dif = abs(percent1-percent2)
listWW = f'{WHITE}{"  " * 5}{END}'
listRW = f'{WHITE}{"  "}{END}{RED}{"  "}{END}{WHITE}{"  " * 3}{END}'
listWR = f'{WHITE}{"  " * 3}{END}{RED}{"  "}{END}{WHITE}{"  "}'
listRR = f'{WHITE}{"  "}{END}{RED}{"  "}{END}{WHITE}{"  "}{END}{RED}{"  "}{END}{WHITE}{"  "}{END}'

o = 100
for a in range(10 - percent1):
    if o == 100:
        print(f'{o}|{listWW}')
    else:
        print(f'{o} |{listWW}')
    o-=10
for b in range(dif):
    print(f'{o} |{listRW}')
    o-=10
for c in range(percent1 - dif):
    print(f'{o} |{listRR}')
    o-=10

rate1 = f'{"  " * 2}{BLACK}{"  " * 3}{END}\n{"  "}{BLACK}{"  "}{END}{"  " * 3}{BLACK}{"  "}{END}\n{BLACK}{"  "}{END}{"  " * 2}{BLACK}{"  "}{END}{"  " * 2}{BLACK}{"  "}{END}\n{"  "}{BLACK}{"  "}{END}{"  " * 3}{BLACK}{"  "}{END}\n{"  " * 2}{BLACK}{"  " * 3}{END}'
rate2 = f'{"  "}{BLACK}{"  " * 5}{END}\n{BLACK}{"  "}{END}{"  " * 2}{BLACK}{"  "}{END}{"  " * 2}{BLACK}{"  "}{END}\n{"  "}{BLACK}{"  " * 5}{END}'
rate3 = f'{BLACK}{"  " * 7}{END}'

os.system("clear")
for i in range(100):
    print(rate1)
    time.sleep(1)
    os.system("clear")
    print(rate2)
    time.sleep(1)
    os.system("clear")
    print(rate3)
    time.sleep(1)
    os.system("clear")
    print(rate2)
    time.sleep(1)
    os.system("clear")