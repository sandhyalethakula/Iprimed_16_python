'''Write a program that asks the user to enter a word and then capitalizes every other letter of that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS. '''


inp = 'rhinoceros'        # inp = input()
outp = ''.join(c.upper() if i%2 else c for i, c in enumerate(inp))
print(outp)                     # 'rHiNoCeRoS'
              
