#**GESTION DE INVENTARIO**

Algoritmo que cumple la necesidad de una tienda la cual es disponer de un sistema que le permita tener un control del inventario de sus propios productos, que cumple con las siguientes caracteristicas:

*   Creacion de nuevos productos
*   Consulta de los productos ya creados
*   Actualizacion o modificacion de los precios de los productos existentes
*   Eliminacion de los productos que ya no poseen existencias
*   Listar todos los productos existentes
*   Redondeo del valor total a pagar

Este sistema controla bien todo el flujo de datos minimizando asi los errores humanos tales como:

*   La creacion de productos con el mismo nombre
*   La entrada de nombres y valores que no pueden poseer un producto real
*   La manipulacion de datos cuando no se poseen datos

en definitiva este algoritmo cumple con las necesidades de la tienda.

##PASO A PASO
>   El programa no permitira la manipulacion de datos sin antes poseer un minimo adecuado de estos, es por que la primera pantalla que salte sera el ingrsar minimo 5 productos en caso tal de no complatar esto no se tendra acceso a las demas funciones del programa.
>
>   Apartir de aqui el usuario podra hacer lo que desee con total libertad, tomando encuenta claro que hay parametros de entrada que el programa bajo ningun concepto permitiria como se menciono con anterioridad.
>
>   En cualquier caso el programa guiara al usuario en caso de cualquier error con mensajes y especificaciones muy claras de como tiene que ingresar o realizar cualquiera de los procesos.
>
    >   #Lo unico complicado a entender es el listado de los objetos para ello se tiene en cuenta la siguiente plantilla:
    >   {} las llaves representan el inicio y final de cada objeto
    >   "productName" <-- indica como clave el nombre del producto (:) <-- separan la clave del valor "<nombre>" <-- representa el nombre del producto
    >   "productPrice" el precio <numero decimal> representa el valor numerico como un valor decimal
    >   "productQty" la cantidad de este objeto y su respectivo valor como un numero entero
  
