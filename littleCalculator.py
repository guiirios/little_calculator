#MY Calculator

#FUNCTIONS
def add(): 
    print("ADDING...")
    listOfNumbers = []
    continueTrue = True
    while continueTrue:
        number = (input("Type your number:  or ok"))
        if number.lower() == "ok":
            break
        else:
            number = int(number)
            listOfNumbers.append(number)
            print(listOfNumbers)
    
    result = sum(listOfNumbers)
    print(f"Your result is: {result}")  

 
def calculationSignal():
    signalChoose = input("Calculator Operations: 1 - Add\n 2- Subtract\n 3- Multiply\n 4- Divide\n")
    if signalChoose == str(1):
        add()
    elif signalChoose == str(2):
        subs()
    elif signalChoose == str(3):    
        multiply()
    elif signalChoose == str(4):    
        divide()
    else:
        print("Invalid")

 

def subs():
    print("Substracting")
    n1 = int(input("Type your number: "))
    print(f"{n1} x - = ?")
    n2 = int(input("Type your number: "))
    print(f"{n1} - {n2} = ")
    result = n1 - n2 
    print(f"{n1} - {n2} = {result}")


def multiply():
    print("Multiplyig")
    n1 = int(input("Type your number: "))
    print(f"{n1} x ? = ?")
    n2 = int(input("Type your number: "))
    result = n1 * n2 
    print(f"{n1} x {n2} = {result}")


def divide():
    print("Dividing")
    n1 = int(input("Type your number: "))
    n2 = int(input("Type your number: "))
    print(f"{n1} / {n2} = ")
    print(f"{n1} x / = ?")
    result = n1 / n2 
    print(f"{n1} / {n2} = {result}")



calculationSignal()

