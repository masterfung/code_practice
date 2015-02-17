def sequence_class(immutable):
	if immutable:
		klass = tuple
	else:
		klass = list
	return klass


def sequence_class_take_2(immutable):
	return tuple if immutable else list

seq = sequence_class(immutable=True)

t = seq('Hello Kitty')

print(t, type(t))

seq2 = sequence_class_take_2(immutable=True)
s = seq2('Zebrafish')

print(s, type(s))


def print_args(arg1, arg2, *arg):
	print(arg1)
	print(arg2)
	print(arg)


t = (11, 12, 13, 14, 15, 16, 17)

print(*t)


def colors(red, blue, green, **kwargs):
	print("red =", red)
	print("blue =", blue)
	print("green =", green)
	print(kwargs)


k = {'red':22, 'blue':77, 'green': 133, 'alpha': 60}

colors(**k)


first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second = [10, 293, 10, 29, 39, 493, 29, 93, 92]
third = [0, 29, 392, 10, 93, 3, 4, 0, 9]

for item in zip(first, second, third):
	print(item)

total_three = [first, second, third]
total_end = list(zip(*total_three))

print(total_end)
