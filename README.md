# Laboratorio-git
Ketzalli Sanchez A01786306

## Cambios en repo remoto



![logogit](/Imagenes/logogit.png)´


En Github podemos poner proyectos o archivos.

lo primero que hicimos fue descargarlo, agregar nuestro nombre y correro electronico usando los comandos git config --global user.name "" y git config --global user.gmail "".

Descpues en la pagina Github.com hacemos una cuenta con nuestro nombre de usurio y nos pedira una contraseña. 


### Llave
Configuramos el acceso SSH que permite conectarnos a otros servidores

Abrimos Git Bash y creamos nuestra llave con el comando  ssh-keygen -t ed25519 -C "nuentro gmail", tenemos dos opciones:
1. introducir contraseña
2. con enter dejara sin contraseña.

Despues introdicimos  eval "$(ssh-agent -s)" que agregara tu llave privada a SSH 
Luego agregamos nuestra llave a Github para poder accesar.
Copia la llave SSH pública a tu portapapeles usando el siguiente comando:
a. clip < ~/.ssh/id_ed25519.pub.
En github seleccionamos en la parte de nuestro perfil SSH and GPG keys, New ket y en la ventana ahora aparecera, pegamos el contenido del porta papeles de Key y finalmente damos dd SSH key.

### Repositorio
En el menú principar de github ponemos New (para crear un nuevo repositorio).Se desplegará la interfaz ‘Crear un nuevo repositorio’, llenamos los campos y creamos el repositorio.
Abajo del nombre del repositorio, se encuentra el número de commits, ramas y usuarios que hay en el repositorio
Indica el nombre de la rama en la que estás actualmente( se llama“main”),bajo nombre de la rama, aparece todo el contenido.

### Clonar repositorio
Entran los conceptos de repositorio local y remoto.

1. creamos una caperta (LaboratorioGit)
2. desde los archivos accedemos a la carpeta y copiamos la direccion.
3. abrimos powershell
4. Escribimos: cd (Dirección de la carpeta) para estar dentro de la carpeta.
5. En Github, entramos a nuetra carpeta (laboratorioGit).
4. En la parte derecha, presiona el botón Code. Aparece una ventana con opciones para hacer
el clone. Verifica que seleccionaste la opción SSH.
5. Gitbash escribimos: git clone. Luego, pegamos el URL que copiaste del repositorio.
6. aparecera la opción “Are you sure you want to continue connecting
(yes/no/[fingerprint])?” indícamos yes.

Y asi se clonara el repositorio remoto en el local.

### Subir contenido a repositorio remoto
Se usaran los comando en el orden:
- git add -A = Sube los cambios realizados a los archivos a una zona de pruebas para que Git
empiece a rastrearlos. En esta zona de pruebas es donde uno puede revisar que el código
esté preparado para subirse al repositorio remoto.
- git commit -m “Descripción del commit” = Sube los archivos al repositorio local.
- git push origin [Rama] = Sube los archivos de tu repositorio local al repositorio remoto

Ahora si creamos el archivo para integrarlo al repositorio local y luego subirlo al remoto.
Abrimos el bloc de notas y copiamos un codigo (el codigo nos lo dieron) guardamos el archivo fijandonos que este en "todos los archivos".
En gitbash escribimos los comandos:
-  git status
-  git add -A
- git commit -m “nombre del archivo”
- git push -u origin main
Y en github en la parte de main ya debe de aparecer (se tiene que guardar el archivo en la carpteta que creamos anterirmente "Laboratoriogit")
Y asi es como se crea un nuevo contenido en el repositorio.

## Pegar imagenes
Descargamos Visual Studios y dentro de el descargamos Markdown, ya que desde ahi podemos conectarnos a Github y modificar nuetros archivos.

Pegamos una imagen
1. primero creamos una nueva carpeta dentro de Laboratoriogit 
2. buscamos una imagen y la guardamos ahi
3. ponemos el comando: ![logogit] (la carpeta y el nombre de la imagen) asi se insertara la imagen.

## Guardar los cambios
para guardar los cambios en el documento vamos a la parte de la izquierda con los tres puntitos seleccionamos el archivo y escribimos los cambios que guardamos. le ponemos pull y listo.
