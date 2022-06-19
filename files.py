# With - manejador contextual
def read():
	numbers = []
	with open('./files/data.txt','r',encoding='utf-8') as f:
		for line in f:
			numbers.append(int(line))
	print(numbers)


def write():
	names= ['Facundo','Miguel','Pepe','Christian','Rocío']
	with open('./files/names.txt','a',encoding='utf-8') as f:
		for name in names:
			f.write(name)
			f.write('\n')

def run():
	read()
	write()



if __name__ =='__main__':
	run()
