def divisors(num):
	try:
		if num <= 0 :
			raise ValueError('Debes ingresar numeros positivos o diferentes de 0')
		divisors = []
		for i in range(1,num+1):
			if(num%i==0):
				divisors.append(i)
		return divisors
	except ValueError as er:
		print(er)
		return []
def run():
	try:
		num = int(input('Ingrese un número :'))
		print(divisors(num))
		print('Fin de programa')
	except ValueError:
		print('Debe ingresar un numero')

if __name__ =='__main__':
	run()