from zeep import Client
from zeep.exceptions import Fault

# URL del archivo WSDL
wsdl_url = 'http://localhost:1516/WS/Users?wsdl'

def print_users(users):
    print("Lista de usuarios:")
    for user in users:
        print(user)

try: 
    # Crear un cliente SOAP
    client = Client(wsdl=wsdl_url)

    # Llamar a los métodos del servicio
    # Por ejemplo, getUsers()
    results = client.service.getUsers()
    print_users(results)

    # Añadir un usuario
    user = {'name': 'Diego3', 'username': 'Huanaco3'}
    print("Actualizacion:")
    client.service.addUser(user)

    # Imprimir la lista de usuarios actualizada
    results = client.service.getUsers()
    print_users(results)

except Fault as f:
    print("Error:", f.message)
except Exception as e:
    print("Error:", e)
