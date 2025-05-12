#Declaration of the main list inventory
#the productQty comes from the abrebiation of the word Quantity
"""{"productName":"name",
     "productPrice":intValue,
     "productQty":floatValue}"""
inventory = [{"productName":"queso","productPrice":100,"productQty":12},{"productName":"palo","productPrice":100,"productQty":12},{"productName":"agua","productPrice":100,"productQty":12}]
answersToRestart = ("si", "s", "no", "n")
answersOptionMenu =[
    "1", "2", "3", "4", "5", "6", "7",
    "calcular", "consultar", "actualizar", "eliminar",
    "ingresar", "listar", "salir"
    ]
#print(inventory[1]["productPrice"])

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

#####--\update product\--#####

def updateProductPrice(list, productName, newProductPrice):
    indexCounter = 0
    for i in list:        
        if i["productName"] == productName:
            list[indexCounter]["productPrice"] = float(newProductPrice)
            return list
        indexCounter += 1
    return None

#####--\delete product\--#####

def deleteProduct(list, productName):    
    for i in list:        
        if i["productName"] == productName:
            list.pop(list.index(i))
            return list        
    return None

#####--\calculations total products\--#####

def calculationTotalPrices(list):
    multipliedPricesQtyList = []
    for product in list:
        multipliedPricesQtyList.append(float(product["productPrice"]*product["productQty"]))
    totalPrices = sum(multipliedPricesQtyList)
    return totalPrices


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
                return showOptionMainMenu()
            
def validateAnswer(answersList, answer):
    try:
        if answer.lower() in answersList:
            return True
        else:
            decorationFunction()
            print(f"ERROR: La respuesta ingresada ({answer}) no es valida!")
            return False
    except:
        print("ERROR: en la validacion S/N.")

def askingForOptionMainMenu():
    """Esta funcion valida primero que se ingrese una respuesta y segundo
      \nque dicha respuesta exista por medio de la funcion validadora de respuestas
      \npor ultimo compara cual fue la respuesta y dependiendo de la respuesta 
      \nllamara a un proceso u otro."""
    answer = input("\nQue deseas hacer? \n")
    if validateAnswer(answersOptionMenu, answer):        
        match answer.lower():
            case "1" | "ingresar":
                return addProductMenu()
            case "2" | "consultar":
                return consulProductMenu()
            case "3" | "actualizar":
                return updateProductMenu()
            case "4" | "eliminar":
                return deleteProductMenu()
            case "5" | "calcular":
                return totalCalculationMenu()
            case "6" | "listar":
                decorationFunction()
                print(inventory)
                return showOptionMainMenu()
            case "7" | "salir":
                decorationFunction()
                print(" "*5,f"HASTA LUEGO!\n")
                exit()
            case _:
                print("ERROR: Opcion no valida!")
                return showOptionMainMenu()

###############-/visual Menu system functions/-###############

def showOptionMainMenu():
        decorationFunction()
        print("--"*5,f"MENU DE OPCIONES","--"*5)
        print(f"(1) - calcular total de la compra.")
        print(f"(2) - consultar valores de un producto.")
        print(f"(3) - actualizar precios del producto.")
        print(f"(4) - eliminar producto.")
        print(f"(5) - ingresar productos.")
        print(f"(6) - listar productos.")
        print(f"(7) - salir.")
        return askingForOptionMainMenu()

def decorationFunction():
    """The best function ever."""
    print(f"==" * 40, "\n")

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
    print("\nMenu de opciones ya disponible (No) para acceder a el")
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
    print("\nProducto consultado con exito!")
    print(f" - Nombre: {consultedProduct["productName"]}")
    print(f" - Precio: {consultedProduct["productPrice"]}$")
    print(f" - Cantidad: {consultedProduct["productQty"]}")
    return restartProcess(consulProductMenu)

def updateProductMenu():
    decorationFunction()
    print("--"*5,f"ACTUALIZACION DE INVENTARIO","--"*5)
    productNametoUpdate = inputProductName()
    if consultProductOnly(inventory, productNametoUpdate) == None:
        decorationFunction()
        print(f"\nERROR: nombre ingresado del producto no disponible para actualizar intente con otro nombre diferente a ({productNametoUpdate}).\n")
        return restartProcess(updateProductMenu)
    consultedProductToUpdate = consultProductOnly(inventory, productNametoUpdate)
    decorationFunction()
    print("\nProducto encontrado y disponible para modificar!")
    print(f" - actualizacion del precio de ({productNametoUpdate})")
    print(f" - precio actual: ({consultedProductToUpdate["productPrice"]}$)")
    newProductPrice = inputProductPrice()
    updateProductPrice(inventory, productNametoUpdate, newProductPrice)
    print(" - Precio del producto actualizado exitosamente!")
    return restartProcess(updateProductMenu)

def deleteProductMenu():
    decorationFunction()
    print("--"*5,f"ELIMINACION DE INVENTARIO","--"*5)
    productNametoDelete = inputProductName()
    if consultProductOnly(inventory, productNametoDelete) == None:
        decorationFunction()
        print(f"\nERROR: producto no disponible para eliminacion intente con otro nombre diferente a ({productNametoDelete}).\n")
        return restartProcess(deleteProductMenu)
    deleteProduct(inventory, productNametoDelete)
    decorationFunction()
    print("\nProducto eliminado con exito!")
    restartProcess(deleteProductMenu)

def totalCalculationMenu():
    decorationFunction()
    print("--"*5,f"SUMATORIA DEL COSTO TOTAL DEL INVENTARIO","--"*5)
    totalPrices = calculationTotalPrices(inventory)
    print(f"\nEl valor de compra de todos los PRODUCTOS del inventario.\n\nEs de: {totalPrices}$")
    restartProcess(totalCalculationMenu)

addProductMenu()