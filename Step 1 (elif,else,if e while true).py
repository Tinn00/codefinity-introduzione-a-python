while True:
    print("Programma attivo")

    a = int(input("Give me a number:"))
    b = int(input("Give me another number:"))
    operazione = input("scrivi +,-,*,/ oppure q:").strip().lower()

    if operazione == "+":
        print("Risultato=", a+b)

    elif operazione == "-":
        print("Risultato=", a-b)

    elif operazione == "*":
        print("Risultato=", a*b)

    elif operazione == "/":
        if b == 0:
            print("Errore: divisione per zero")
        else:
            print("Risultato=",a/b)

    elif operazione == "q":
        print("Uscita")
        break

    else:
        print("Operazione non valida")
        
