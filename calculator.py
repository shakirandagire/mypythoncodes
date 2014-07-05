
def	add(number1,number2):
	return number1 + number2

def subtract(number1,number2):
	return  number2 - number1

def multiply(number1,number2):
	return  number1 * number2
	
def divide(number1,number2):
	return  number1 / number2

option = raw_input("""Select mathematical operation: \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide\n""")

choice = int(raw_input('Enter choice (1/2/3/4)'))

number1 = float(raw_input('Enter first number:'))
number2 = float(raw_input('Enter second number:'))

if choice == "1":	
	print "The answer is:", number1, '+' ,number2, '=', add(number1,number2)

if choice == "2":	
	print "The answer is:", number1, '-' ,number2, '=', subtract(number1,number2)

if choice == "3":	
	print "The answer is:", number1, '*' ,number2, '=', multiply(number1,number2)

if choice == "4":	
	print "The answer is:", number1, '/' ,number2, '=', divide(number1,number2)