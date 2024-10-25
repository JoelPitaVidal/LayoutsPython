#Generar pequeño layout
import sys
from PyQt6.QtGui import QPalette, QColor
#Importamos los widgets necesarios.
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget)
#Creamos una clase que recibe el QMainWindow
class PrimeraFiestra (QMainWindow):
#Inicializamos la clase
    def __init__(self):
        super().__init__()
#Establecemos el título de la pantalla
        self.setWindowTitle("Primera ventana con QT")
#Establecemos un tamaño mínimo
        self.setMinimumSize(300,200)
#Establecemos un tamaño máximo
        self.setMaximumSize(400,300)
#Cambiamos el color de fondo de la ventana a negro
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("black"))
        self.setPalette(paleta)
#Creamos una caja en la que colocar elementos
        caixav = QVBoxLayout()
#Creamos un botón
        btnSaudo = QPushButton("Saludo")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)
#Añadimos el boton a la caja
        caixav.addWidget(btnSaudo)
#Indicamos que va a contener la ventana
    #Creamos un contenedor
        container = QWidget()
    #Metemos la caja dentro de el contenedor
        container.setLayout(caixav)
    #Establecemos el contenedor como el widget central
        self.setCentralWidget(container)
#Hacemos que la clase sea visible y muenster el layout
        self.show()
        self.setVisible(True)

    def on_btnSaudo_clicked(self):
        print("Hola usuari@")


#Crear QLabel
#Meterlo en el layout
#Buscar un metodo en etiqueta cambio de texto
#Cuando el usuario hace click---->Saludar en la etiqueta




#Si el nombre es igual a "Main"
if __name__ == "__main__":
#Creamos la aplicacion
    aplicacion = QApplication(sys.argv)
#Creamos la primera ventana igualandola a la clase que hemos creado
    fiestra = PrimeraFiestra()
#Ejecutamos la aplicación
    aplicacion.exec()