import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, \
    QHBoxLayout, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        lab = QLabel("Température")
        self.__text = QLineEdit("")
        ok = QPushButton("Convertir")
        aide = QPushButton("?")
        self.__conversion = QLabel("conversion")

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItem("C -> K")
        self.cb.addItem("K -> C")
        if self.cb.currentText() == "C -> K":
            C = QLabel("°C")
        if self.cb.currentText() == "K -> C":
            C = QLabel("°K")


        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)

        # Ajouter les composants au grid ayout
        grid.addWidget(lab, 0, 0)
        grid.addWidget(self.__text, 0, 1)
        grid.addWidget(C, 0, 2)
        grid.addWidget(ok, 2, 1)
        grid.addWidget(self.cb, 2, 2)
        grid.addWidget(self.__conversion, 3, 0)
        grid.addWidget(aide, 3, 3)

        ok.clicked.connect(self._actionOk)
        aide.clicked.connect(self._aide)



    def selectionchange(self, i):
        print
        "Items in the list are :"

        for count in range(self.cb.count()):
            print
            self.cb.itemText(count)
        print
        "Current index", i, "selection changed ", self.cb.currentText()

    def _actionOk(self):
        if self.cb.currentText() == "C -> K":
            try:
                self.__conversion.setText(f'{"{:.2f}".format(float(self.__text.text())+ 273.15)}K')
            except ValueError:
                QMessageBox(text="Valeur incorrect").exec()
        else:
            try:
                self.__conversion.setText(f'{"{:.2f}".format(float(self.__text.text())- 273.15)}C')
            except ValueError:
                QMessageBox(text="Valeur incorrect").exec()

    def _aide(self):
        """widget = QWidget()
        self.setCentralWidget(widget)
        self.setWindowTitle("Aide")
        grid = QGridLayout()
        widget.setLayout(grid)
        text = QLabel("Permet de convertir un nombre soit de Kelvin vers Celius, soit de Celius vers Kelvin")
        grid.addWidget(text,0,0)
        """
        QMessageBox(text="Permet de convertir un nombre soit de Kelvin vers Celius, soit de Celius vers Kelvin").exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()