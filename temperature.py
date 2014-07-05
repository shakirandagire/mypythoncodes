import math;

temperature = raw_input("""Choose option to convert temperature:\n 1.To celcius \n 2.To fahrenheit""")


def celcius():
	f = float(raw_input("Enter the temperature and convert it to celcius:"))
	tc= (f-32)* 5/9
	print "temperature in celcius = ", tc

def fahrenheit():
	c = float(raw_input("Enter the temperature and convert it to fahrenheit:"))
   	tf= c * 9/5 + 32
	print "temperature in fahrenheit = ", tf

if temperature == "1":
  celcius()

if temperature == "2":
  fahrenheit()






