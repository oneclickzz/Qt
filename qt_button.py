if __name__ == '__main__':
    from PySide2.QtCore import QCoreApplication
    QCoreApplication.setLibraryPaths(['C:\\Users\\501\\Documents\\develop\\py_example\\venv\\Lib\\site-packages\\PySide2\\plugins'])

import PySide2
import PySide2.QtCore

# print("PySide2 version: ", PySide2.__version__)
# print("QtCore version: ", PySide2.QtCore.qVersion())

from PySide2.QtCore import Qt
# from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QRadioButton
from PySide2.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QCheckBox, QGroupBox

# from PySide2.QtWidgets import *
import sys


class MyForm(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle("Button Demo")

        # print('self.button: ', type(self.button))

        self.button = QPushButton("OK")
        # self.button.move(50,50)
        # print('self.button: ', type(self.button))
        self.button.clicked.connect(self.okButtonClicked)

        self.checkBox = QCheckBox('Case Sensitivity')
        self.checkBox.toggled.connect(self.onCaseSensitivity)


        self.nameLabel = QLabel("라면")
        
        box = QGroupBox("음식")

        self.button1 = QRadioButton("라면", box)
        self.button2 = QRadioButton("국수", box)
        self.button3 = QRadioButton("치킨", box)
        self.button4 = QRadioButton("삼겹살", box)
        self.button1.setChecked(True)

        groupBoxLayout = QVBoxLayout(box)
        groupBoxLayout.addWidget(self.button1)
        groupBoxLayout.addWidget(self.button2)
        groupBoxLayout.addWidget(self.button3)
        groupBoxLayout.addWidget(self.button4)
        # self.button1.toggled.connect(self.onMale)

        self.button1.toggled.connect(self.onToggle1)
        self.button2.toggled.connect(self.onToggle2)
        self.button3.toggled.connect(self.onToggle3)
        self.button4.toggled.connect(self.onToggle4)

        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.button)
        mainLayout.addWidget(self.checkBox)
        mainLayout.addWidget(self.nameLabel)
        mainLayout.addWidget(box)

        self.setLayout(mainLayout)

        pass

    def okButtonClicked(self):
        print('okButtonClicked')

    def onCaseSensitivity(self, toggle):
        print('onCaseSensitivity', toggle)
        print(self.checkBox.isChecked())

    def onMale(self, toggle):
        print('male' if toggle else 'famale')
        # print('onMale', toggle)

    def onToggle1(self, toggle):
        # print('라면') if toggle else None
        self.nameLabel.setText('라면')
        # self.nameLabel.move(10,100)
        # self.button.setText("라면")
        # print(self.button.text())
        pass

    def onToggle2(self, toggle):
        # print('국수') if toggle else None
        self.nameLabel.setText('국수')
        pass

    def onToggle3(self, toggle):
        # print('치킨') if toggle else None
        self.nameLabel.setText('치킨')
        pass

    def onToggle4(self, toggle):
        # print('삼겹살') if toggle else None
        self.nameLabel.setText('삼겹살')
        pass
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    form = MyForm()
    form.show()
    # form.button.setText("오케이")

    app.exec_()
    # print("끝!")



