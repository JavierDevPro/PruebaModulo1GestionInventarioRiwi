#Declaration of the main list inventory
#the productQty comes from the abrebiation of the word Quantity
"""{"productName":"name",
     "productPrice":intValue,
     "productQty":floatValue}"""
inventory = [{"productName":"queso","productPrice":100,"productQty":12},{"productName":"palo","productPrice":100,"productQty":12},{"productName":"agua","productPrice":100,"productQty":12}]
answersToRestart = ("si", "s", "no", "n")
#print(inventory[1]["productPrice"])

def decorationFunction():
    """The best function ever."""
    print(f"==" * 40, "\n")


###############-/input functions and validations/-###############
#####--\adding product\--#####
def inputProductName():
    decorationFunction()
    temporaryName = input("- Ingresa el nombre del producto: \n     ")
    while (not (validationName(temporaryName))):
        temporaryName = input("- Ingresa el nombre del producto: \n     ")
        continue
    return temporaryName

def inputProductPrice():
    decorationFunction()
    temporaryPrice = input(" - Ingresa el precio unitario del producto: \n    ")
    while not (validationNumbersValue(temporaryPrice,1)):
        temporaryPrice = input(" - Ingresa el precio unitario del producto: \n     ")
        continue
    return float(temporaryPrice)

def inputProductQty():
    decorationFunction()
    temporaryQty = input(" - Ingresa la cantidad del producto: \n     ")
    while not (validationNumbersValue(temporaryQty,2)):
        temporaryQty = input(" - Ingresa la cantidad del producto: \n      ")
        continue
    return int(temporaryQty)

def validationName(temporaryProductName):
    try:
        if temporaryProductName[0].isdigit() or temporaryProductName[1].isdigit():
            print("ERROR: El nombre de un producto no debe poseer valores numericos en sus primeros dos caracteres.\n")
            return False
    except:
        print("ERROR: El nombre de un producto debe poseer almenos (2) caracteres.\n")
        return False
    return True

def validationNumbersValue(number, type):
    try:
        if type==1:
            float(number)
        else:
            int(number)

        if float(number) > 0:
            return True
        else:
            print(f"ERROR: El valor ingresado bajo ningun caso debe ser (0) ni inferior.  \n      ")
        
    except ValueError:
        decorationFunction()
        if not number.isdigit():
            print(f"ERROR: El valor ingresado no puede poseer alfanumericos. \nPor ende ({number}) no es admitido.\n      ")
        if type != 1 and not(number.isalpha()):
            print(f"ERROR: El valor ingresado no puede ser decimal. \nPor ende ({number}) no es admitido. \n      ")
        return False

def addProductToInventory(inventoryList, productName, productPrice, productQty):
    inventoryList.append({"productName":productName,"productPrice":productPrice,"productQty":productQty})
    return inventoryList

def validationMinProducts(dictionary):
    if len(dictionary) >= 5:
        return True
    else:
        return False

#####--\consulting product\--#####

def consultProductOnly(list, nameToConsult):
    for i in list:
        if i["productName"] == nameToConsult:
            return i
    return None


###############-/sequence functions/-###############

def restartProcess(actualProcess):
    decorationFunction()    
    while True:
        decorationFunction()
        answer = input("Desea intentar de nuevo el proceso? (Si/No) \n")
        if (validateAnswer(answersToRestart, answer)):
            if (answer.lower() == "si" or answer.lower() == "s"):               
                return actualProcess()                
            else:
                return None
            
def validateAnswer(answersList, answer):
    try:
        if answer in answersList:
            return True
        else:
            decorationFunction()
            print(f"ERROR: La respuesta ingresada ({answer}) no es valida!")
            return False
    except:
        print("ERROR: en la validacion S/N.")

###############-/Menu system functions/-###############
def addProductMenu():
    decorationFunction()
    print("--"*5,f"INGRESO DE INVENTARIO","--"*5)
    productName = inputProductName()
    productPrice = inputProductPrice()
    productQty = inputProductQty()
    addProductToInventory(inventory, productName, productPrice, productQty)
    if not validationMinProducts(inventory):
        print(f"\nSe requieren minimo (5) productos para realizar cualquier otra funcion \nte faltan: ({5-len(inventory)})")
        return addProductMenu()
    return restartProcess(addProductMenu)

def consulProductMenu():
    decorationFunction()
    print("--"*5,f"CONSULTAS DE INVENTARIO","--"*5)
    productNametoConsult = inputProductName()
    if consultProductOnly(inventory, productNametoConsult) == None:
        decorationFunction()
        print(f"\nERROR: nombre ingresado del producto no existe intente con otro nombre diferente a ({productNametoConsult}).\n")
        return restartProcess(consulProductMenu)
    consultedProduct = consultProductOnly(inventory, productNametoConsult)
    decorationFunction()
    print(consultedProduct["productName"])
    print("\nProducto consultado con exito!")
    print(f" - Nombre: {consultedProduct["productName"]}")
    print(f" - Precio: {consultedProduct["productPrice"]}$")
    print(f" - Cantidad: {consultedProduct["productQty"]}")
    return restartProcess(consulProductMenu)

addProductMenu()
print("la cantidad: ",len(inventory))
consulProductMenu()