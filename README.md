# 2FAInstagram
## Disclaimer
El propósito de este repositorio es sólo educativo, no me hago responsable del mal uso que se pueda hacer de las herramientas que contiene.  
No soy un programador experto, todo el código se optimizará y mejorará en próximas veriones.  
  
    
_[ENG]  
This repository is meant for educational purposes only.  
I'm not an expert developer, the code will be improved in futher versions._

## Decripción
La autenticación en dos factores o verificación en dos pasos (2FA) es una medida de protección de los sistemas de autenticación que consiste en que el usuario presente dos pruebas demuestren que es quien dice ser. 
En este caso , este repositorio tiene como objetivo demostrar como los atacantes consiguen evadir el 2FA para el sistema de autenticación de Instagram. Los dos factores usados en este caso son la contraseña y un código enviado al móvil del usuario.

_[ENG]  
Two-factor authentication (2FA) adds an additional layer of protection in authentication systems consisting on the proof that the user shows to be the real user.
This repository aims at demonstrating how the attackers can bypass 2FA for instagram's authentication system. In this case, the two factors are password and a code sent to mobile user._

## Dependencias
- [Apache2](https://www.apache.org/)
- [Python](https://www.python.org/)
- [Selenium](https://www.seleniumhq.org/)

## How to run

```
git clone https://github.com/afernandezb92/2FAInstagram.git
cd 2FAInstagram
pip install -r requirements.txt
chmod +x run.sh
chmod +x geckodriver
./run.sh
```

Se debe eliminar el contenido del fichero code.txt para poder realizar nuevas capturas.

_[ENG]  
you must delete code.txt file for capturing new users._

````
rm /var/www/html/instagram/code.txt
````

## Escenario
El atacante mediante alguna de las de técnicas de hacking (dnsspoofing, ingeniería social, etc.) redirige a una victima que tiene activado 2FA a la web que suplanta Instagram. Una vez que la víctima introduzca sus correo y contraseña en la página falsa, la máquina del atacante iniciará un navegador automáticamente, introduciendo en la web real de Instagram las credenciales de la víctima, provocando esto que la víctima reciba el mensaje con el código del 2FA. Cuando la víctima reciba el código lo introducirá en la página falsa y cuando lo introduzca la máquina del atacante obtendrá ese código y completará el inicio de sesión en la web legítima de Instagram, obteniendo así el acceso a la cuenta de la víctima.

_[ENG]  
The attacker using hacking techniques (dnsspoofing, social engineering, etc.) redirect the victim with 2FA active in instagram to fake instagram web. Once the victim logs in the fake web, the attacker's machine will run a web browser and it will go to original instagram to log in with victim's credentials. This will cause instagram send the validation code to the victim. When the victim receives the code, he will put it in the fake web. The attacker will get the code and will complete the log in the original instagram web, gaining the access to the victim account._

![alt text](https://raw.githubusercontent.com/afernandezb92/2FAInstagram/master/2FAInstagram.png)

## POC
![alt text](https://i.imgur.com/hfkIwyO.gif)


## Mejoras
- Incluir los dos últimos dígitos del número de teléfono de la víctima en la página falsa de solicitud del código.
- Modificar el flujo de ejecución para permitir distinguir si el usuario tiene 2FA o no.
- Validar entrada de datos.
- Fichero de log.
- Sanetizar las entradas de datos.
