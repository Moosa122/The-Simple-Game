commands = ['quit',
 	'add', 
 	'subtract',
 	'multiply',
  	'divide',
   	'help',
   	'game']
prompt = 'Enter Your Command: '
word1 = input(prompt)
running = True


while running:
	if word1 == commands[0]:
		print('Program Exited')
		running = False
		break

	if word1 == commands[1]:
		prompt1 = 'Put First Number: '
		num1 = input(prompt1)
		prompt1 = 'Put Second Number:'
		num2 = input(prompt1)
		sum = float(num2)+float(num1)
		print(sum)
		word1 = input(prompt)
		
	if word1 == commands[2]:
		prompt1 = 'Put First Number: '
		num1 = input(prompt1)
		prompt1 = 'Put Second Number: '
		num2 = input(prompt1)
		sum = float(num1)-float(num2)
		print(sum)
		word1 = input(prompt)
		
	if word1 == commands[3]:
		prompt1 = 'Put First Number: '
		num1 = input(prompt1)
		prompt1 = 'Put Second Number: '
		num2 = input(prompt1)
		sum = float(num1)*float(num2)
		print(sum)
		word1 = input(prompt)
		
	if word1 == commands[4]:
		prompt1 = 'Put First Number: '
		num1 = input(prompt1)
		prompt1 = 'Put Second Number: '
		num2 = input(prompt1)
		sum = float(num1)/float(num2)
		print(sum)
		word1 = input(prompt)
		
	if word1 != commands[0] or commands[1] or commands[2] or commands[3] or commands[4] or commands [5] or commands[6]:
		print('No Command By That Word')
		word1 = input(prompt)
		
	if word1 == commands[6]:
		Main()
		

	if word1 == commands[5]:
		print(commands)
		word1 = input(prompt)
