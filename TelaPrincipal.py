import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_MainWindow import Ui_MainWindow
from CustomListModel import CustomListModel


class TelaPrincipal(QMainWindow, Ui_MainWindow):
    '''Janela principal'''


    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        #INICIALIZAÇÕES VÃO AQUI
        self.lst_data = ['bananas','maças', 'laranjas', 'uvas', 'mexiricas']

        self.entry = QtGui.QStandardItemModel()
        self.lstView.setModel(self.entry)

        for i in self.lst_data:
            item = QtGui.QStandardItem(i)
            self.entry.appendRow(item)


        #EVENT-HANDLERS (SLOTS) VÃO AQUI



#FUNÇÃO MAIN PADRÃO
def main():
    app = QApplication([])

    win = TelaPrincipal()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


