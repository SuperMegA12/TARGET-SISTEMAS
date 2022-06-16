#Forma com loop
frase = str(input('Digite uma frase ou palavra: ')).strip().upper()
string = ''
for i in frase:
    string = i + string


print(string)

#Forma sem loop
print('='*40)


frase_2 = str(input('Digite uma frase ou palavra: ')).strip().upper()
frase_2_reversa = frase_2[::-1]
print(frase_2_reversa)