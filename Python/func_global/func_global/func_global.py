x = 50

def func():
	global x

	print('x равен', x)
	x = 2
	print('Заменяем глобальное x на', x)

func()
print('Значение х составляет', x)
