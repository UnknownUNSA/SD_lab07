from zeep import Client
from zeep.exceptions import Fault

# URL del servicio WSDL
url = 'http://localhost:1516/WS/Lab07?wsdl'

# Crea el cliente SOAP
client = Client(url)

def listar_productos():
    try:
        # Llama al método getProducts del servicio
        response = client.service.getProducts()
        #print(type(response))
        # Accede a la lista de productos dentro de la respuesta
        #print (response)
        for producto in response:
            id_producto = producto['id']
            nombre_producto = producto['name']
            precio_producto = producto['price']
            print(f"ID: {id_producto}, Nombre: {nombre_producto}, Precio: {precio_producto}")

       
    except Fault as e:
        print(f"Error al listar productos: {e}")


def realizar_compra():
    try:
        listar_productos()

        productId = input("Ingrese el ID del producto que desea comprar: ")
        quantity = int(input("Ingrese la cantidad que desea comprar: "))

        # Llama al método makeSale del servicio
        sale = {'productId': productId , 'quantity': quantity}
   
        sale = client.service.makeSale(sale)
      
        print("Compra realizada con éxito.")
        try:
            # Llama al método getProducts del servicio
            gsale = client.service.getSales()
            #print(type(response))
            # Accede a la lista de productos dentro de la respuesta
            #print (response)
            for producto in gsale:
                id_producto = producto['productId']
                nombre_producto = producto['quantity']
                print(f"ID: {id_producto}, Cantidad: {nombre_producto}")

       
        except Fault as e:
            print(f"Error al listar productos: {e}")


    except Fault as e:
        print(f"Error al realizar la compra: {e}")

if __name__ == "__main__":
    # Menú interactivo
    while True:
        print("Menú:")
        print("1. Listar productos")
        print("2. Realizar una compra")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            listar_productos()
        elif choice == "2":
            realizar_compra()
        elif choice == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
