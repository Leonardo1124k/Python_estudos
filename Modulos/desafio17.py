""" from math import hypot """
import math
catetoOp = float(input("Digite o valor do cateto oposto: "))
catetoAd = float(input("Digite o cateto adjacente: "))

hip = math.pow(catetoOp,2) + math.pow(catetoAd,2)
hip = math.sqrt(hip)

""" hip = hypot(catetoOp,catetoAd) ignore"""
    
print(f"O valor da hipotenusa é {hip:.2f}")

print(math.sqrt(16))