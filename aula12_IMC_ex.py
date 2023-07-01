

name = " Filipe Tavares"
height = 1.73
weight = 84

imc = weight / (height ** 2)

print("O IMC do " + name + " com uma altura de " + str(height) + 
"m e um peso de " + str(weight) + "kg é " + str("{:.2f}".format(imc)))