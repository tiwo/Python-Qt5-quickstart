import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow, QMessageBox, QWidget, QGridLayout,
    QCheckBox,
    QPushButton,  QLineEdit, QLabel, QToolBar
)

class Hauptfenster(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Hauptfenster')
        self._createMenu()
        self._createToolBar()
        self._createContent()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Datei")
        self.menu.addAction('&Beenden', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('&Info...', self._showInfobox)
    
    def _showInfobox(self):
        print(QMessageBox.about(self, "Über dieses Programm", "gibt es nicht viel zu erzählen."))


    def _createContent(self):

        layout = QGridLayout()
        layout.addWidget(QPushButton('Knöpfli 0,0'), 0, 0)
        layout.addWidget(QLineEdit("Angebereingabe 0,1"), 0, 1)
        layout.addWidget(QCheckBox('Option A (0,2)'), 0, 2)
        layout.addWidget(QPushButton('Knopf 1,0'), 1, 0)
        layout.addWidget(QPushButton('Bumperl 1,1'), 1, 1)
        layout.addWidget(QCheckBox('Option B (1,2)'), 1, 2)
        layout.addWidget(QPushButton('Button 2, 0'), 2, 0)
        layout.addWidget(QPushButton('Drück mi net! 2,1 + 2 Spalten'), 2, 1, 1, 2)
        
        fensterInhalt = QWidget()
        fensterInhalt.setLayout(layout)
        self.setCentralWidget(fensterInhalt)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Hauptfenster()
    win.show()
    sys.exit(app.exec_())