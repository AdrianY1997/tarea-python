def run(): 
    cfr = int(input("Digite la cantidad de frutos recolectados: "))
    cfp = int(input("Digite la cantidad de frutos producidos: "))
    ic = ((cfr/cfp)*100)
    print("El indice de cosecha es", ic, "%")
    
run()   