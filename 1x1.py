def count_vowels(string: str):
	vowels = ['a', 'e', 'i', 'o', 'y', 'u']
	#count_vowels = 0

	for i in vowels:
		if string.count(i):
			# count_vowels += 1
			#print(f'-> {count_vowels}')
			print(f'{string.count(i)}')

count_vowels('abec')
