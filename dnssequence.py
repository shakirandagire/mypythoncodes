value = raw_input("Enter a DNA string:")

print value

dna_seq={}

def count(value):

	for item in value:

		if item in dna_seq:

			dna_seq[item] +=1
		else:

			dna_seq[item] = 1

	return dna_seq

print(count(value))				