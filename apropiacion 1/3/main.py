def run(): 
    n1 = float(input("digite la primera nota: "))
    n2 =float(input("digite la segunda nota: "))
    n3 = float (input("digite la tercera nota: "))
    ne = float (input("digite la nota del examen final: "))
    nt = float (input("digite la nota del trabajo final: "))
    nd = (n1+n2+n3)/3
    final = nd*0.55+ne*0.30+nt*0.15
    print("La nota final es ",final)
    
run()   