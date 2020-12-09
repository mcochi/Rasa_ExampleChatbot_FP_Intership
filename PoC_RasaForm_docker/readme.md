## Instructions for setup

1 - First of all, it's necessary to execute ngrok http 5005 - Rasa server is set up on 5005 port as default

2 - Take uri - https one - and copy it to credentials.yml, telegram section. 

3 - Execute docker-compose up and wait. 

4- Just enjoy. 


# Preparación del entorno de ejecución de chatbot en RASA 2.0

## 1. Instalación de Virtualenv

```sh
pip install virtualenv
```

## 2.  Preparación del entorno virtual 

- En macOSX
En el directorio donde tengamos los ficheros descargados:

```virtualenv venv```

```./venv/bin/activate``` 

- En windows
En el directorio donde tengamos los ficheros descargados:

```virtualenv venv```

```cd venv/Scripts/```

```activate```

Siempre que ejecutemos algo en rasa tenemos que tener el entorno activo -> Recuerda que para desactivarlo es simplemente el comando deactivate.

Para identificarlo, ver el encabezado del shell y vemos que comienza como se llame nuestro entorno. Por ejemplo:
```
(base) MacBook-Air-de-Coro-2:PoC_RasaForm corodri$ source ./venv/bin/activate
(venv) (base) MacBook-Air-de-Coro-2:PoC_RasaForm corodri$ rasa —version
```

## 3. Instalación de rasa
```pip install rasa==2.0.2```

```pip  install —-use-feature=2020-resolver rasa==2.0.2```

Comprobación de la versión de rasa:
```rasa —-version
(venv) (base) MacBook-Air-de-Coro-2:PoC_RasaForm_docker corodri$ rasa --version
Rasa Version     : 2.0.2
Rasa SDK Version : 2.1.2
Rasa X Version   : None
Python Version   : 3.7.4
Operating System : Darwin-20.1.0-x86_64-i386-64bit
Python Path      : /Users/corodri/Downloads/Rasa_ExampleChatbot_FP_Intership-master/PoC_RasaForm_docker/venv/bin/python
```

## 4. Puesta a punto del entorno

```rasa train```


## 5. Activación del servidor de Custom Actions

En otra terminal y en el mismo directorio:

- En macOSX
En el directorio donde tengamos los ficheros descargados:

```virtualenv venv```

```./venv/bin/activate``` 

- En windows
En el directorio donde tengamos los ficheros descargados:

```cd venv/Scripts/```

```activate```


En mi caso tengo que instalar algunas librerías primero para que funcionen las custom actions

```pip3 install codaio && pip3 install requests && pip3 install typing_extensions``` 

```rasa run actions```

## 6. Comprobación de correcto funcionamiento
 ```rasa shell```
