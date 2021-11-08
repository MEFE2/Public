# classes
MEFE2 classes

# Instalación de pyROOT (Ubuntu) - Español

Para entender qué es pyROOT, primero tenemos que entender qué es ROOT. Como lo dice en su página web (https://root.cern/), ROOT es una plataforma de análisis de datos de código abierto utilizada en Física de Altas Energías y otras ramas. ROOT nos dará las herramientas estadísticas necesarias para el curso y, pese a ser una herramienta especialmente focalizada en Física de Altas Energías, la encontraremos robusta y didáctica útil a la hora de meternos en los temas desarollados durante el curso.

pyROOT es ROOT en Python. Esto nos dará la ventaja de un debugging muy rápido y versátil, lo cuál es crucial durante y entre clases, pero la desventaja de una latencia más alta a la hora de la ejecución de los scripts. Si estás familiarizado con C/C++, pyROOT no es necesario. Dicho ésto se alienta a todos lxs alumnxs a instalar pyROOT y usarlo durante el curso dado que será de gran utilidad para la mayoría de las aplicaciones que no requieren una alta velocidad de procesamiento.
.
#### IMPORTANTE: Las siguientes instrucciones han sido escritas para una computadora con un sistema operativo Ubuntu 18.04 o mayor. Si están acá ya deberían tener Ubuntu instalado.

#### IMPORTANTE 2: Python3 es requerido. Pueden instalarlo desde su página web oficial (https://www.python.org/downloads/) o desde Anaconda (https://www.anaconda.com/products/individual). El primer link es solo Python y el segundo es  Python + algunas herramientas muy útiles (para Python). Si esta es la primera vez que están utilizando Python, Anaconda es preferrible. Para instalarlo descarguen el archivo .sh (Anaconda3-2021.05-Linux-x86_64.sh as today) desde la página web oficial de Anaconda, abran una terminal, muévanse al directorio donde el archivo fue descargado y corran el siguiente comando:

> sh Anaconda3-\*-Linux-x86_64.sh

## Pre-requisitos

Primero, chequeemos que tenemos todo lo necesario para poder instalar ROOT. Muchas dependencias son necesarias para correr ROOT (pueden chequearlas en https://root.cern/install/dependencies/). Para instalarlas, abran una terminal y corran los siguientes comandos:

> sudo apt-get update
> sudo apt-get install dpkg-dev cmake g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev python libssl-dev git tar

Un mensaje aparecerá en sus terminales preguntando por su contraseña de Ubuntu. Tipeenla, toquen Enter y sigas las instrucciones.

En este punto si no están familiarizados con ejecutar comandos en una terminal por favor refiéranse a alguna guía introductoria en el tema. No debería tomarles más que 10 minutos. Cualquier guía está bien.

## Compilando desde la fuente

Compilar desde la fuente es un proceso algo tedioso pero robusto de instalar ROOT y nos permitirá asegurarnos que todxs tiene la misma versión de cada paquete y ningún problema de compatibilidad surgirá.

Instrucciones acerca de cómo descargar y compilar ROOT (y pyROOT) pueden encontrarse en https://root.cern/install/build_from_source/ pero algunas instrucciones específicas están disponibles aquí:

- Descargar la última versión de ROOT seleccionando la opción "source distribution" en https://root.cern/releases/release-62406/ (o clickeando el siguiente link: https://root.cern/download/root_v6.24.06.source.tar.gz). Asegúrense de descargar el archivo en la carpeta `/home/<usuario>/` donde `<usuario>` es el nombre de usuario que tiene en Linux. El archivo descargado está en formato `TAR.GZ` así que para descomprimirlo deben correr el siguiente comando:

> tar -xzvf ~/root*.tar.gz 

Si este comando no funciona es probable que tengan el archivo descargado en otro directorio. Luego de descomprimir el `TAR.GZ`, cambien el nombre de la carpeta donde descomprimo a `root` usando el comando `mv`

> mv root-* root

Chequeen que hay un directorio llamado `root` en `home` de la siguiente manera:

> ls ~/root

Si les dice "No such file or directory" algo salió mal. Sigamos:

- Crear un directorio de compilación (`rootbuild`) y otro de instalación (`rootinstall`). Luego muévanse al escritorio de compilación:

> cd ~

> mkdir ~/rootbuild ~/rootinstall
> 
> cd ~/rootbuild

- Ejecutar el comando `cmake` en la terminal de la siguiente manera:
- 
> cmake -DCMAKE_INSTALL_PREFIX=~/rootinstall ~/root
  
- Queremos compilar pyROOT con Python3. El comando `cmake -DCMAKE_INSTALL_PREFIX=~/rootinstall ~/root` ejecutado en la terminal debería darles un mensaje largo en la misma terminal. Busquen en ese mensaje una línea que lea "PyROOT will be built for versions 3.something" o "PyROOT will be built for versions 3.something (Main) and 2.something" en el caso que tengan tanto python2 como 3 instalados en su computadora.
- Si ninguna versión de python3 es encontrada, o bien no tienen Python instalado o ROOT no lo está encontrando. Para solucionarlo, ejecuten el comando `which python3` en la terminal. Un mensaje corto aparecerá con una dirección. Llamemos a esta dirección &lt;python3_dir&gt; y corramos nuevamente el comando `cmake` de la siguiente manera:

> cmake -DCMAKE_INSTALL_PREFIX=~/rootinstall -DPython3_EXECUTABLE=&lt;python3_dir&gt; ~/root
 
 Importante: donde dice `<python3_dir>` deben escribir la dirección que el comando `which python3` les devolvió.
 
- Para compilar ROOT ejecuten el siguiente comando:

> cmake --build . --target install

Este comando puede tardar un par de horas en ejecutarse...

- Finalmente, el archivo de configuración de la terminal ~/.bashrc debe ser modificado con el fin de incluir la siguiente línea: 

``` bash
source ~/rootinstall/bin/thisroot.sh
```
Si no tienen un editor de textos de preferencia el siguiente comando les abrirá el predeterminado de Ubuntu (noten que corre con `sudo` así que nuevamente les pedirá su contraseña de Ubuntu):

> $ sudo gedit ~/.bashrc

Y agreguen la línea anteriormente citada. 


- Para chequear que la instalación de ROOT+pyROOT fue un éxito, abran una nueva terminal, corran python y traten de importar ROOT como paquete de la siguiente manera:

  > import ROOT
