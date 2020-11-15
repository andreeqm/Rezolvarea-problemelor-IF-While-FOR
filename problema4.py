from fractions import Fraction
m=int(input("Introduceti numaratorul fractiei 1 m= "))
n=int(input("Introdueti numitorul fractiei 1 n= "))
l=int(input("Introduceti numaratorul fractiei 2 l= "))
x=int(input("Introduceti numitorul fractiei 2 x= "))
print("suma este:",Fraction(m,n)+Fraction(l,x))
print("produsul este",Fraction(m,n)*Fraction(l,x))
