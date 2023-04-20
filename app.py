import pymongo as mongo #importar el controlador para la conexión a la base de datos

miConexion = mongo.MongoClient("mongodb://localhost:27017/") #objeto para la Conexión al servidor mongodb

baseDatos = miConexion["miTienda"] #acceso a la base de datos tienda
#print(type(baseDatos))

productos = baseDatos["productos"] #acceso a la colección (tabla productos)
#print(type(productos))

# -------------------------------------------------------------------------------------------------

#Validar que la base de datos no exista para crearla
def existeBaseDatos():
    listaBaseDatos = miConexion.list_database_names()
    if "miTienda" in listaBaseDatos:
        return True
    return False

# -------------------------------------------------------------------------------------------------

#Agregar un producto a la colección productos de la base de datos tienda
def agregarProducto():
    try:
        #datos del producto - datos quemados - podrian ser solicittados
        codigo = 10
        nombre = "Televisor"
        precio = 2500000
        categoria = "Electrodomestico"
        
        #Objeto producto - tipo diccionario
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria
        }
        
        #Insertar datos a la colección de la base de datos
        code = {"codigo":codigo}
        p = productos.find_one(code)
        if (p is not None):
            print(f"Producto con ese codigo ya existe")
        else:
            resultado = productos.insert_one(producto)
            print("Producto agregado correctamente")
        
    except mongo.errors as error:
        print(f"Problemas al agregar producto. Error: {error}")

# -------------------------------------------------------------------------------------------------

#Consultar producto por código
def consultarPorCodigo():
    try:
        codigoConsultar = int(input("Ingrese el código del producto a consultar: ")) #código del producto a consultar
        consulta = {"codigo":codigoConsultar}
        
        #cosnultar en la coleccion
        #producto = baseDatos.producto.find_one(consulta)
        producto = productos.find_one(consulta)
        
        #Mostrar datos del producto
        if(producto is not None):
            print(f"Datos del producto: ")
            print(producto)
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoria: {producto['categoria']}")
        else:
            print(f"Producto con el código {codigoConsultar} NO existe")
            
    except mongo.errors as error:
        print(f"Problemas al consultar el producto. Error: {error}")

# -------------------------------------------------------------------------------------------------

#Actualizar producto
def actualizarProducto():
    try:
        codigoProducto = int(input("Ingrese el código del producto a actualizar: ")) #Código del producto a actualizar
        
        criterio = {"codigo":codigoProducto} #criterio para saber que producto se va a actualizar
        
        #diccionario con los datos nuevos
        datosActualiar = {
            "codigo": 1,
            "nombre": "Smartphone",
            "precio": 4500000,
            "categoria": "dispositivo electronico"
        }
        
        consulta = {"$set" : datosActualiar}
        
        #resultado = productos.update_one(criterio,consulta)
        resultado = baseDatos.productos.update_one(criterio,consulta)
        
        print(f"Producto actualizado correctamente")
        
    except mongo.errors as error:
        print(f"Porblemas al actualizar producto. Error: {error}") 

# -------------------------------------------------------------------------------------------------

#Eliminar producto
def eliminarProducto():
    try:
        codigoProductoEliminar = int(input("Ingrese el código del producto a eliminar: ")) #Código del prodcuto a eliminar
        
        consulta = {"codigo":codigoProductoEliminar}
        
        baseDatos.productos.delete_one(consulta)
        #productos.delete_one(consulta) #Eliminar producto de la colección
        
        producto = productos.find_one(consulta) #verificar despues si existe
        if(producto is None):
            print(f"Producto eliminado de la colección {productos.name}")
        else:
            print(f"No se ha podido eliminar el producto de la colección {productos.name}")
        
    except mongo.errors as error:
        print(f"Problemas al eliminar el producto. Error: {error}")

# -------------------------------------------------------------------------------------------------

#Agregar varios productos
def agregarVariosProductos():
    try:
        producto1 = {
            "codigo": 1,
            "nombre": "televisor",
            "precio": 2500000,
            "categoria": "electrodomestico"
        }
        producto2 = {
            "codigo": 2,
            "nombre": "computador",
            "precio": 5000000,
            "categoria": "dispositivo electronico"
        }
        producto3 = {
            "codigo": 3,
            "nombre": "nevera",
            "precio": 3600000,
            "categoria": "electrodomestico"
        }
        producto4 = {
            "codigo": 4,
            "nombre": "camisa",
            "precio": 150000,
            "categoria": "ropa"
        }
        lista_productos = [producto1,producto2,producto3,producto4]
        
        resultado = productos.insert_many(lista_productos)
        
        print(f"Productos agregados correctamente a la colección {productos.name}")
    except mongo.errors as error:
        print(f"Problemas al agregar productos. Error: {error}")

# -------------------------------------------------------------------------------------------------

#Listar productos de la colección
def listarProductos():
    try:
        listaProductos = baseDatos.productos.find()
        print(f"\nLista de productos de la colección {productos.name}:")
        for producto in listaProductos:
            print(f"\nCódigo: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoria: {producto['categoria']}")
            print("-"*50)
    except mongo.errors as error:
        print(f"Problemas al listar los productos. Error: {error}")

# -------------------------------------------------------------------------------------------------

#agregarProducto()
#consultarPorCodigo()
#actualizarProducto()
#eliminarProducto()
#agregarVariosProductos()
listarProductos()