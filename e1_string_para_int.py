
print("O seu numero da sorte é a soma do seu mes de nascimento com o dia do seu nascimento! ") # JUST DO A PRINT, NOT A INPUT
mes = int(input("Digite o mês do seu nascimento (1-12): ")) # TRANSFORM TO INT IN THIS LINE
dia = (input("Digite o dia do seu nascimento (1-31): ")) # TRANSFORM TO INT IN THIS LINE
# numero_da_sorte = int(mes) + int(dia) DONT NEED TO DO THAT, JUST USE IN THE PRINT BELOW
print(f"Seu número da sorte é: {mes + dia}") # USE A F-STRING
