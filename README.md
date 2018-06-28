Esta es la aplicación de la cámara aérea para rastrear pelotas de colores para el Laboratorio de Proyectos 3 de Abril-Julio 2018.

![Aplicación de Detección de Pelotas](https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_1.png)

Esta aplicación recibe el video de una cámara, ubica una marcador AR en la imagen, y procede a usarlo para proporcionar una de vista aérea de la imagen mediante una corrección de perspectiva. En esa imagen se ubica la presencia de un Marcador de Realidad Aumentada para que marque el origen **(0,0)** de la cancha en la **esquina inferior izquierda**.
El marcador usado es el siguiente:

<p align="center">
  <img width="200" height="200" src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/marker_27.jpg">
</p>


# Opciones del GUI:

La interfaz gráfica consiste de 2 partes. Una te muestra la imagen que está viendo la cámara, y otra que muestra la imagen corregida. Esta segunda tiene las siguientes opciones:


<p align="center">
  <img src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_2.png">
</p>

1. **Track AR Marker:**
    - **1**: El programa activamente busca el marcador AR para recuadrar la pista en la vista aérea.
    - **0**: El programa recuerda la última corrección que hizo y la sigue usando en vez de intentar conseguir el marcador nuevamente (Bueno para evitar vibraciones en la imagen).
2. **Field Length \[cm\]**:
El tamaño de la cancha en pantalla es modificable. Este es el largo de la cancha en centímetros, como está definido en la figura.
3. **Field Width \[cm\]**:
El tamaño de la cancha en pantalla es modificable. Este es el ancho de la cancha en centímetros, como está definido en la figura.
4. **Reset Tracked Colors**:
Presiona este slider para resetear las pelotas que están siendo rastreadas en la pantalla. Con moverlo de posición basta, no importa en qué posición quede.


# Instrucciones de Uso:

Estas instrucciones asumen que se tiene el programa instalado en la carpeta portátil  de **WinPython**.

1. Iniciar el command prompt de powershell incluido en la carpeta "WinPython Powershell Prompt.exe", como se ve en la figura.
<p align="center">
  <img width="70%" height="70%" src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_9.png">
</p>
El terminal de comandos debería verse como alguno de los siguientes 2:
<p align="center">
  <img width="90%" height="90%" src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_12.png">
</p>

2. Usar siguiente comando para moverte desde la carpeta predeterminada de inicio a la carpeta donde está la aplicación:
```bash
cd ..\Ball_Locating_Server
```

3. Iniciar la aplicación con el siguiente comando. Donde el número **1** es el número de la cámara que se quiere usar. Puede ser 0, 1, 2, depende de cuántas cámaras tengas conectadas a tu computadora.
```bash
python main.py -c 1
```
4. Usa los sliders de opciones de la aplicación para configurar el tamaño de cancha como fue descrito en la sección anterior. Cuadrar la cámara al lugar deseado, asegurarse de que el marcador AR esté visible y seleccionar la opción "Track AR Marker" para que la imagen deje de vibrar.

5. Para comenzar el rastreado de las pelotas, ubica las pelotas que desees rastrear con el mouse.
<p align="center">
  <img width="60%" height="60%" src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_3.png">
</p>
Y dale click a la pelota en la pantalla para indicarle a la herramienta que deseas rastrearla.
<p align="center">
  <img width="60%" height="60%" src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_4.png">
</p>

Si le diste click al color equivocado, recuerda que el 4° slider de las opciones puede deseleccionar los colores elegidos.

6. Para recibir los datos del servidor, se puede acceder a la página```http://localhost:8000``` donde se verá el arreglo con la información de las pelotas rastreadas (cambiar ```localhost``` por la dirección IP de la computadora corriendo el servidor). Como se ve a continuación:

<p align="center">
  <img src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_5.png">
</p>

La información de las pelotas viene en arreglos de un **JSON**, y contiene la siguiente información:
<p align="center">
  <img width="60%" height="60%" src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_6.png">
</p>
donde:


- **x**: Es la posición de la pelota en el eje X (ancho) en metros, variable flotante.
- **y**: Es la posición de la pelota en el eje Y (largo) en metros, variable flotante.
- **radius**: El radio de la pelota en metros, variable flotante.
- **COLOR**: Una etiqueta con el color detectado de la pelota, es un string de un color determinado (Ej. "RED", "GREEN", "YELLOW", "CYAN"...)


7. Cuando se quiere terminar el programa se presiona **Q** en la aplicación para cerrarla, y **CTRL+C** en el terminal de comandos para detener el servidor.


# WinPython y Windows:

Para que los estudiantes pudieran libremente usar la aplicación sin tener que preocuparse por instalar Python en sus computadoras, o configurar la librerías usadas, se empaquetó la aplicación en una Distribución de [WinPython](https://winpython.github.io/).


WinPython es básicamente un Python completo en una carpeta que puedes copiar y pegar de un lado al otro. Esto otorga gran versatilidad y portatibilidad  a las aplicaciones, a cambio de cierto rendimiento y velocidad. Sin embargo, este sistema también puede causar algunos glitches visuales en la aplicación. Puede que su aplicación se vea así:

<p align="center">
  <img src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_7.png">
</p>

Si esto ocurre, observe a continuación la relación entre la aplicación en windows y las imágenes previamente presentadas del menú de configuración.

<p align="center">
  <img src="https://github.com/SaidAlvarado/EC3883-ColorBallTracker/blob/master/figures/wiki/wiki_figure_8.png">
</p>


# Modificar el código:

Hay varias formas de modificar el código para cambiar su comportamiento, a continuación se presentan algunas ideas.

### Más Etiquetas de Colores

El código aproxima el color de las pelotas una serie de etiquetas (R,G,B) predefinidas en la linea 20 del archivo ```ColorTracker.py```

```python
# Dictionary of recognized color labels.
self.RGB_dictionary = OrderedDict({
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "CYAN": (0, 255, 255),
    # It doesn't recognize Magenta very well.
    # "MAGENTA": (255, 0, 255),
    "YELLOW": (255, 255, 0),
        })
```

Si se quisiera agregar la etiqueta ```PINK``` al programa, se podrían modificar las lineas mostradas de la siguiente manera:

```python
# Dictionary of recognized color labels.
self.RGB_dictionary = OrderedDict({
    "PINK": (255, 100, 100),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "CYAN": (0, 255, 255),
    # It doesn't recognize Magenta very well.
    # "MAGENTA": (255, 0, 255),
    "YELLOW": (255, 255, 0),
        })
```


### Detección más Robusta de Colores

Cuando se le da click a un color en la pantalla, el programa lo registra y lo usa como base para detectar colores similares usando un intervalo de confianza definido en la linea 34 de ```ColorTracker.py```

```python
self.margins = { "hue": 0.05,
      "saturation": 0.3,
      "value": 0.3
      }
```
Si se quisiera aumentar el intervalo de incertidumbre del ```hue``` de 5% a 10% para que el algoritmo sea más resistente a variaciones en el color de las pelotas, se podría escribir lo siguiente:

```python
self.margins = { "hue": 0.1,
      "saturation": 0.3,
      "value": 0.3
      }
```

### Imprimir tu Propio Marcador AR

El programa usa el hecho de que el marcador AR es cuadrado y mide 14.4cm de lado para corregir la perspectiva de la imagen y usarlo como referencia para medir la posición de las pelotas. Si desean imprimir sus propios marcadores AR para usar, le deben informar al programa de qué largo (en metros) en el lado del cuadrado negro del marcador. Cambiando la linea 155 de ```main.py```. de:

```python
    ar_tracker = ARTracker(debug_flag = args["debug"])
```
a

```python
    ar_tracker = ARTracker(debug_flag = args["debug"], marker_size = 0.144)
```
donde 0.144 es el tamaño (en metros) de lado negro de marcador AR.


# Ejemplo para leer el servidor:

El servidor que envía la posición de las pelotas es un servidor WEB que recibe un GET request y responde con un paquete de JSON. El paquete de JSON contiene un arreglo con pequeños arreglos que guardan la información de las pelotas detectadas. Para recibir ese paquete desde Python recomiendo el siguiente código, que lo pueden encontrar en el repositorio en ```examples/GET-Request-example.py```.

```python
import requests
# Define the IP address and Port of the Server.
ip_address = "127.0.0.1"
port = "8000"
# Make the request
r = requests.get("http://" + ip_address + ":" + port)

# Move the response to another variable
response = r.json()
# Print the response
print(response)
```

Este código recibe el arreglo con la información de las pelotas en la variable ```response```
