


# para coisas contantes ao longo do programa colocar com letra grandre

NUMBER_1 = 1000

# evitar muitas condições dentro do mesmo (if)

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = float(1)

velocidade = 50
local_carro = 100.4
on_range = False

if local_carro > (LOCAL_1-(RADAR_RANGE/2)):
    if local_carro < (LOCAL_1+(RADAR_RANGE/2)):
        on_range = True
    else:
        print(f"O carro não está no range!")
else:
    print(f"O carro não está no range!")
if on_range:
    if velocidade > RADAR_1:
        print(f"Multa! Passou no radar de {RADAR_1}km/h a {velocidade}km/h")
    else:
        print(f"Bom trabalho! Passou no radar de {RADAR_1}km/h a {velocidade}km/h")