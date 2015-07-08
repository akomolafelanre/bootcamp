def check_lowercase(word):
	i = 0
	word = list(word)
	for item in word:
		if item.islower():
			i += 1
	return i

def check_uppercase(word):
	i = 0
	word = list(word)
	for item in word:
		if item.isupper():
			i += 1
	return i

def check_numbers(word):
	i = 0
	word = list(word)
	for item in word:
		if item.isdigit():
			i += 1
	return i

def check_passwords(s):
	result = 0
	passwords = open(s, 'r')
	for item in passwords:
		if check_numbers(item) >= 4:
			if check_lowercase(item) >= 2:
				if check_uppercase(item) >= 4:
					result += 1
	print "%s has %d valid passwords." %(s, result)

if __name__ == "__main__":
	check_passwords("password.txt")
