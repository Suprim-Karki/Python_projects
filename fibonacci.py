''' Fibonacci series '''
def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


numero = int(input("ingrese un numero entero  positivo: "))

if numero < 0:
	print("Number invalid")

i = 0

print("Fibonacci sequence is: ")

for i in range(0, numero):
	print(fibonacci(i))