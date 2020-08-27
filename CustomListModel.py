from PyQt5 import QtCore


class CustomListModel(QtCore.QAbstractListModel):


    def __init__(self,parent=None, *args):
        super().__init__(parent, *args)
        self.lstData = []


    def update(self, lst_new_data):
        '''
        -> Substitui os dados da listView por novos dados.
        :param lst_new_data: (list) Novos dados.
        :return: Sem retorno.
        '''


        self.lstData = lst_new_data
        self.layoutChanged.emit()


    def rowCount(self, parent = QtCore.QModelIndex()):
        '''
        -> Retorna o número de linahs necessárias.
        :param parent: (optional)(QModelIndex)
        :return: (int) Tamanho da lista
        '''


        if self.lstData != None:
            return len(self.lstData)
        else:
            return 0


    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not self.lstData:
            return ''
        if role == QtCore.Qt.DisplayRole:
            i = index.row()
            well = self.lstData[i]
            return well
        else:
            return QtCore.QVariant


if __name__ == '__main__':
    MyLstViewMod = CustomListModel()