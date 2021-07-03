## Ruleta
esta simulacion de ruleta permite simular 1 de los tipos de juegos que existen en la ruleta y es cuando se apuesta a ROJO O NEGRO  impar o par
para la ejecucion de este proyecto se debe desplazar al directorio de descarga de este proyecto en su equipo y crear un entorno virtual para esto debe ejecutar

apt-get install python3-venv
python3 -m venv NOMBRE_PROYECTO_PREFERIDO

luego de poner un nombre a su entorno virtual ejecutar el siguiente comando en la carpeta de este proyecto descargado


pip3 install -r requirements.txt  

o bien el comando 

pip install -r requirements.txt 


una vez con todas las dependencias correctas del proyecto podra ver una interfaz como la siguiente:
 ![alt text](https://github.com/sebas1017/Ruleta/blob/main/Ruleta/home.PNG?raw=true)


en caso de que lo este corriendo de forma local podra verlo en la direccion:

http://127.0.0.1:5000/

 
 Donde podra verificar las reglas del juego en el home
 
 el servicio online para la base de datos se uso HEROKU y en el algoritmo se limpian conexiones activas para evitar problemas de concurrencia ya que esta app heroku tiene un limite maximo de 20 conexiones  y se desplego en un servidor AWS con un servidor WSGI apache2 puede ver el proyecto corriendo de forma online 
 en el siguiente url http://ec2-54-90-42-239.compute-1.amazonaws.com/
