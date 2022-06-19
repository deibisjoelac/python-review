# def palindrome(string):
# 	assert len(string)>0 , "No se puede ingresar una cadena vacía"
# 	return string == string[::-1]

# print(palindrome(''))


def divisors(num):
	divisors = []
	for i in range(1,num+1):
		if(num%i==0):
			divisors.append(i)
	return divisors

def run():
		num = input('Ingrese un número :')
		assert num.isnumeric() > 0,'Solo se permiten numeros y no negativos'
		print(divisors(int(num)))
		print('Fin de programa')

if __name__ =='__main__':
	run()