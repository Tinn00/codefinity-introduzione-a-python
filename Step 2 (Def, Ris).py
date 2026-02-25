def calcola():
    a = int(input("Print First Number: "))
    b = int(input("Print Second Number: "))
    operazione = input("scrivere +,-,*,/ oppure q: ").strip().lower()

    if operazione == "+":
        return a + b
    elif operazione == "-":
        return a - b
    elif operazione == "*":
        return a * b
    elif operazione == "/":
        if b == 0:
            print("Errore: divisione per zero")
            return None
        return a / b
    elif operazione == "q":
        return "Quit"
    else:
        print("Operazione non valida")
        return None

ris = calcola()
if ris == "Quit":
    print("Uscita")
elif ris is not None:
    print("Risultato:", ris)