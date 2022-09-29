# Função para calcular o IMC
def calculate_bmi(weight, height):
    # IMC = Peso ÷ (Altura × Altura)
    return weight / (height * height)

# Função para classificar o IMC segundo a OMS
def get_who_classification(bmi):
    # Verifica o valor do IMC e retorna a classificação segundo a OMS
    if bmi < 18.5:
        return "Magreza"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif bmi >= 25 and bmi < 30:
        return "Sobrepeso"
    elif bmi >= 30 and bmi < 35:
        return "Obesidade Grau 1"
    elif bmi >= 35 and bmi < 40:
        return "Obesidade Grau 2"
    elif bmi >= 40:
        return "Obesidade Grau 3"

# Função para classificar o IMC segundo o Ministério da Saúde
def get_ms_classification(bmi):
    # Verifica o valor do IMC e retorna a classificação segundo o Ministério da Saúde
    if bmi < 18.5:
        return "Abaixo do peso"
    elif bmi >= 18.5 and bmi < 25:
        return "Peso normal"
    elif bmi >= 25 and bmi < 30:
        return "Sobrepeso"
    elif bmi >= 30:
        return "Obesidade"

# Função principal
def main():
    print("\nCalculadora de IMC\n")
    
    # Solicita o peso e a altura em float
    while True:
        try:
            weight = float(input("Peso (kg): "))
            height = float(input("Altura (m): "))
            break
        except:
            print("Valor inválido!")
            
    # Utiliza a função para calcular o IMC
    bmi = calculate_bmi(weight, height)
    
    # Imprime o resultado aproximado do IMC
    print("\nSeu IMC é:", "{:.2f}".format(bmi))
    # Imprime a classificação segundo a OMS
    print("A OMS classifica seu IMC como:", get_who_classification(bmi))
    # Imprime a classificação segundo o Ministério da Saúde
    print("O Ministério da Saúde classifica seu IMC como:", get_ms_classification(bmi))
    
# Executa o programa
main()