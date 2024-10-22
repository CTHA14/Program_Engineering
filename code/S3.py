with open('input1.txt') as f:
	txt = f.read()
	print('Input file contains:')
	print(sum(map(str.isalpha, txt)), 'letters')
	print(len(txt.split()), 'words')
	print(txt.count('\n') + 1, 'lines')