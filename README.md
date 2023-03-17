# Prueba Opcional Django rest framework
Este programa resuelve un CRUD basico con Django Rest Framework utilizando
Las siguientes clases heredan de APIView
## User (estas operaciones son muy similares para EcommerceStore)
**GET
    usario -> ListCreateAPIView: hace una solicitud GET para obtener la lista de usuarios
    ListCreateAPIView -> Serializer: recupera los datos y los convierte en formato JSON
    Serializer -> APIView: devuelve los datos serializados como respuesta HTTP

**POST
    usario -> ListCreateAPIView: hace una solicitud POST para crear un usuario
    ListCreateAPIView -> Serializer: serializa los datos de entrada de formato JSON a un objeto User Valido
    Serializer -> User: Guardar el usario nuevo en la base de datos
    User -> Serializer: Recuperar el usuario nuevo guardado y serializar los datos
    Serializer -> APIView: devolver el objeto creado como respuesta HTTP

**PUT
    usario -> RetrieveUpdateDestroyAPIView: hace una solicitud PUT para actuailizar un usuario
    RetrieveUpdateDestroyAPIView -> User: buscar el usuario en la base de datos por ID
    User -> Serializer: serializar los datos
    serializer -> APIView: devolver el objeto actualizado como respuesta HTTP

**DELETE
    usario -> RetrieveUpdateDestroyAPIView: hace una solicitud PUT para eliminar un usuario
    RetrieveUpdateDestroyAPIView -> User: buscar el usuario en la base de datos por ID
    User -> APIView: Elimina el usuario correspondiente de la base de datos
    APIView -> Usuario: Devuelve una respuesta HTTP 200 para indicar que fue correctamente borrado

** Podemos utilizar un cliente para realizar las operaciones GET, POST, PUT y DELETE como postman o Thunder Client