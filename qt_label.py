
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox)

from PySide2.QtGui import QPixmap, QImage, QColorSpace
import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        # super().__init__(parent)
        QWidget.__init__(self, parent)

        self.setWindowTitle('Image viewer')

        self.imageLabel = QLabel()
        # self.imageLabel.setFrameStyle(QFrame.WinPanel)
        self.imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        # self.imageLabel.setMaximumSize(500,500)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        self.imageLabel.setScaledContents(True)
        # 위젯에 표시될 이미지를 정의 (화면에 그림)
        self.imageLabel.setPixmap(QPixmap())

        openButton = QPushButton("Load image")

        layout = QVBoxLayout()
        layout.addWidget(self.imageLabel)
        layout.addWidget(openButton)

        self.setLayout(layout)

        openButton.clicked.connect(self.open)
        self.resize(QApplication.primaryScreen().availableSize()*2/5)
        # self.resize(100,200)


    def open(self):
        

        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", '.', "Images (*.png *.xpm *.jpg *.jpeg)")
        print("fileName: ", fileName)
        
        if fileName != "":
            self.load(fileName)
            pass

    def load(self, fileName):

        image = QImage(fileName)
        image.invertPixels(QImage.InvertMode.InvertRgba)

        if image.isNull():
            QMessageBox.information(self, QApplication.applicationName(), 'Cannot load ' + fileName)

            self.setWindowTitle("Image viewer")
            self.setPixmap(QPixmap())
            return
        
        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.setWindowTitle(fileName)

        pass


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()

