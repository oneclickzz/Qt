if __name__ == '__main__':
    from PySide2.QtCore import QCoreApplication
    QCoreApplication.setLibraryPaths(['C:\\Users\\501\\Documents\\develop\\py_example\\venv\\Lib\\site-packages\\PySide2\\plugins'])

import PySide2
import PySide2.QtCore

# print("PySide2 version: ", PySide2.__version__)
# print("QtCore version: ", PySide2.QtCore.qVersion())

from PySide2.QtCore import Qt
# from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()

    labelId = QLabel('Id :')
    labelId.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    labelPW = QLabel("Password :")

    lineEditId = QLineEdit()
    lineEditPW = QLineEdit()
    # lineEditPW.setEchoMode(QLineEdit.Password)
    # lineEditPW.setEchoMode(QLineEdit.Normal)
    # lineEditPW.setEchoMode(QLineEdit.NoEcho)
    lineEditPW.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    labelId.setBuddy(lineEditId)
    labelPW.setBuddy(lineEditPW)

    #       Id : [linEditId]
    # Password : [linEditPW]

    buttonOk = QPushButton("Ok")
    # buttonOk.setIcon(QIcon(":/ok.png"))
    # buttonOk.setText("OK")

    layout1 = QGridLayout()
    layout1.addWidget(labelId,0,0)
    layout1.addWidget(lineEditId,0,1)
    layout1.addWidget(labelPW,1,0)
    layout1.addWidget(lineEditPW,1,1)

    #  |0,0|0,1|
    #  |1,0|1,1|
    #  |2,0|2,1|

    layout2 = QHBoxLayout()
    layout2.addStretch()
    layout2.addWidget(buttonOk)

    # | 0 | 1 | 2 |

    mainLayout = QVBoxLayout()
    mainLayout.addLayout(layout1)
    mainLayout.addLayout(layout2)

    # | 0 |
    # | 1 |
    # | 2 |

    window.setLayout(mainLayout)
    window.setWindowTitle('Log on')
    # window.setWindowIcon(QIcon(":/images/ok.png"))

    buttonOk.clicked.connect(app.quit)



    window.show()
    app.exec_()
    # print("끝!")



