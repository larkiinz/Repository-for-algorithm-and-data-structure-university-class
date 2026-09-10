#задание 1
from math import sin, cos

def f(x): #вводим функцию, вычисляющую значение выражения
  return cos(2/x) - 2 * sin(1/x) + 1/x

L = 1
R = 2
B = 0
if f(L) * f (R) < 0: #проверяем на наличие корня
  while abs(R - L) > 0.001:
    B = L + (R - L)/2
    if f(R) * f(B) > 0: #смотрим, где относительно точки B находится корень
      R = B
    else:
      L = B
else:
  print("не имеет корня на данном интервале")
print(B)
# задание 2
def xk(a, b): #формула приближения корня для метода хорд
  return a - f(a) * (b - a) / (f(b) - f(a))

a = 1
b = 2
i = 0
j = 0
while True:
  j = i #предыдущее значение xk
  i = xk(a, b) #следующее значение xk
  if abs(f(i)) < 0.001: #смотрим, насколько близко точка i к корню
    break
  if f(i) * f(b) > 0:
    b = i
  else:
    a = i
print(i)
