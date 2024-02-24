#third
import math

print("Third task: ", 36/6*2)
print("4th")
print("Fourth task: ", 4*3**2*2)
print("5th")
s = "tomato"
t = "cucumber"
print("Fifth task: ", 2*s+t)
print("6th")
s = "change me"
s = s[0:5]+s[5].upper()+s[6:len(s)-1]+s[len(s)-1].upper()
print("Sixth task: ", s)
print("7th")
ss = 0.09531033
str_1 = "red"
str_2 = "white"
str_3 = "green"
print(str_1+str_2)
print("_".join([str_1, str_2]))
print(str_3.find("a"))
print(str_2.find("e"))
print(str_3.split("r"))
print(str_3, str_2)
print("8th")
mass = list(map(float, input().split()))
print(mass.index(max(mass[0:10])))
print("9th")
x = [2, 4, 6, 8, 10, 12]
print(
    x[-1:2:-2],
    x[::-2],
    x[0::1], #0::0 - error
    x[1::3],
    x[0]
)
print("10th")
a = (2, "1", 1, 10, 1)
print(a.index(1))
print("11th")
melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni':
1455,'Si': 1415, 'Be': 1287}
els = list(map(str, input().split()))
first_element = els[0]
second_element = els[1]
print("Temperature of first element is higher on ", melt.get(first_element)-melt.get(second_element), " than second")
print("12th")
s1 = {'Рентген','Лоренц','Зееман','Кюри','Милликен', 'Сигбан', 'Франк', 'Герц'}
s2 = {'Фишер','Резерфорд','Кюри','Прегль'}
answer = []
for el1 in s1:
    for el2 in s2:
        if el1 == el2:
            answer.append(el1)

print(answer)
print("13th")
if 2**2 > 4:
    print("yes")
print("14th")
if 10 > 100:
    print('yes')
else:
    print('nope')
print("15th")
a = 4
if a/2 > 0:
    print('1')
elif a==4:
    print('2')
elif a < 0:
    print('3')
else:
    print('4')
print("16th")
ans = ""
x0, y0 = map(int, input().split())
if (x0-1)**2+y0**2-4 == 0:
    ans += "yes "
else:
    ans+= "no "
if abs(x0-4)<2 and abs(y0-2)<3:
    print(ans+"yes")
else:
    print(ans+"no")
print("17th")
alp = ord("a")
alphabet = ''.join([chr(i) for i in range(alp, alp+27)])
inp = str(input())
point = alphabet.index(inp[0])+1+int(inp[1])
if point%2 == 0:
    print("black")
else:
    print("white")
print("18th")
for i in range(3, 11, 4):
 print(i)
print("19th")
lst = [2, 6, 43, 1, 66]
s = 0
for item in lst:
    if item % 2 == 0:
        s += 1
    else:
        continue
print("20th")
n = 0
summ = 0
x = 1+float(input())
while True:
    n_sum = (((-1)**n)*(x**(n+1)))/(n+1)
    # if abs(n_sum) < 10**(-6):
    #     break
    if n == 60:
        break
    summ = summ + n_sum
    n += 1
print(ss)
print("21st")
nans = list(map(int, input().split()))
ans = 0
for nan_num in range(len(nans)-2):
    if (nans[nan_num+1]-nans[nan_num])/0.01 > ans:
        ans = (nans[nan_num+1]-nans[nan_num])/0.01

print(ans)
print("22nd")
melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}
ans = ""
for elem in melt.keys():
    ans += (str(elem)+" ")
print(ans)
print("23rd")
def my_filter(a: list=[]):
    string = ""
    for elem in a:
        string += (str(elem*10)+" ")
    return string

my_filter([-3, 7, 2, -10, -9, -2, 5, 8, 4, 5])
print("24th")
def fun(x):
    return math.sin(x)
def trapez(func, a, b, N):
    h = (a-b)/N
    return (fun(a)+fun(b)+sum(fun(a+step*h) for step in range(1, N)))*h


print("25th")
def function(a = 1, b = 2, c = 3):
    return int(a + b / c)
x = function(2, c = 1, b = 2)
print("26th")
def func(*args):
    lst = []
    for item in args:
        if item % 2 == 0:
            lst.append(item)
    return lst
a, *b, c = func(1, 2, 3, 4, 5, 6, 7, 8)
print(b)
print("27th")
def volume(*args):
    if len(args) == 2:
        return args[0]*args[1]
    else:
        return args[0]*args[1]*args[2]

inp = list(map(int, input().split()))
if len(inp) == 2:
    print(volume(inp[0], inp[1]))
else:
    print(volume(inp[0], inp[1], inp[2]))
print("28th")
y = lambda a, b: a ** b
x = y(2, 3)
print(x)






