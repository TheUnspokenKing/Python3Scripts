#!/usr/bin/python3
#Meu Primeiro Script

print("Desec Security")

ip = input("Digite o IP: ") #String
porta = int(input("Digite a porta: ")) #Inteiro
ver = 1.1

print("Scan versao:" , ver)
print("Varrendo Host:" , ip, " na porta " , porta)

print("IP - ", type(ip))
print("Porta - ", type(porta))
print("Ver - ", type(ver))

print("Varrendo Host: %s na porta %d" %(ip,porta))
