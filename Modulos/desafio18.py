# from math import cos, sin, tan, radians
import math

ang = float(input("Digite o angulo: "))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f"O seno com o angulo {ang} é igual a {sen:.2f}")
print(f"O cosseno com o angulo {ang} é igual a {cos:.2f}")
print(f"A tangente com o angulo {ang} é igual a {tan:.2f}")