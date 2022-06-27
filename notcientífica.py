import os
import time

programOn=True
while programOn==True:
    mode=None
    while mode==None:
        print("""// CONVERSOR DE NOTAÇÃO CIENTÍFICA //
Escolha o modo de operação:
1. Transformar em notação científica
2. Expandir notação científica
3. Fechar""")
        print("\n")
        mode=int(input("Modo: "))

        if mode == 3:
            mode=None
            exit()

        if mode == 2:
            os.system('cls')
            n1="m"
            n2="p"
            print("Digite a mantissa")
            print(f"{n1} x 10^{n2}")
            n1=float(input("N: "))
            os.system('cls')
            print("Digite a potência")
            print(f"{n1} x 10^{n2}")
            n2=int(input("N: "))
            nr=n1*(10**n2)
            nrOut= "{:,}".format(nr)
            os.system('cls')
            print("Input:")
            print(f"{n1} x 10^{n2}")
            print("Resultado:")
            print(nrOut)
            print("\n")
            input("Pressione qualquer tecla para continuar...")
            os.system('cls')
            mode==None
        
        if mode == 1:
            os.system('cls')
            n1=0
            nr=0
            n2=0
            print("Digite o número extenso a ser expresso em notação científica:")
            n1=float(input("N: "))
            nx=n1
            n1Out= "{:,}".format(n1)            
            os.system('cls')
            if abs(nx)<1:
                while abs(nx)<1:
                    nx=nx*10
                    n2=n2-1                
                print("Número original:")
                print(n1Out)
                print("Forma notação científica:")
                print(f"{nx} x 10^{n2}")
                print("\n")
                input("Pressione qualquer tecla para continuar...")

            if abs(nx)>=10:
                while abs(nx)>10:
                    nx=nx/10
                    n2=n2+1                
                print("Número original: ")
                print(n1Out)
                print("Forma notação científica: ")
                print(f"{nx} x 10^{n2}")
                print("\n")
                input("Pressione qualquer tecla para continuar...")

            else:
                print("Número original: ")
                print(n1)
                print("Forma notação científica: ")
                print("Número já está na sua forma mais simplificada.")
                print("\n")
                input("Pressione qualquer tecla para continuar...")

            os.system('cls')
            mode==None

        else:
            print("Operação inválida.")
            time.sleep(2)
            os.system('cls')   
