def palindrome(string):
	try:
		if len(string)==0:
			raise ValueError('No se puede ingresar cadena vac´ia')
		return string == string[::-1]
	except ValueError as ve:
		print(ve)
		return False


try:
	print(palindrome(''))
except TypeError:
	print('Solo se pueden ingresar cadenas')
else:
	print('No se produjo ninguna exception')
finally:
	print('Fin del archivo')