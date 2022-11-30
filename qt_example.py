if __name__ == '__main__':
    from PySide2.QtCore import QCoreApplication
    QCoreApplication.setLibraryPaths(['C:\\Users\\501\\Documents\\develop\\py_example\\venv\\Lib\\site-packages\\PySide2\\plugins'])

import PySide2
import PySide2.QtCore
# print("PySide2 version: ", PySide2.__version__)
# print("QtCore version: ", PySide2.QtCore.qVersion())

from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    # window.resize(289, 170)
    window.resize(400, 500)
    window.setWindowTitle("QT어플리케이션")

    label = QLabel("이것은 큐티인가 큐트인가", window)
    # label.move(110, 80)
    label.move(200, 160)

    window.show()
    app.exec_()
    # print("끝!")



