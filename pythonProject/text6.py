from PyQt5.Qt import *
import combox
import sys
import threading
from UI.Sever_ui import sertext
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class combox_set(QMainWindow, combox.Ui_MainWindow):
    signal_i = pyqtSignal()

    def __init__(self):
        super(combox_set, self).__init__(parent=None)
        self.setupUi(self)
        # self.ui.setupUi(self)
        self.ui_serv = sertext.MyServer()
        self.textEdit.append("fsflsjflkj")

        self.actionset_ziti.triggered.connect(self.set_front)
        self.actionopen.triggered.connect(self.open_file_dialo)
        self.pushButton.clicked.connect(self.show_server)
        self.ui_serv.signa_exist.connect(lambda: print("子界面退出"))
        self.signal_i.connect(self.msg)

    def set_front(self):
        print("字体部分")
        result = QFontDialog.getFont()
        print(result)
        # print(result[0])
        print("选择字体", result[0].family())
        print("选择大小：", result[0].pointSize())
        if result[1]:
            self.textEdit.setFont(result[0])

    def open_file_dialo(self):

        file = QFileDialog()
        # File.getOpenFileNames("./")
        file.getExistingDirectory(self, ",/")
        # file.setFileMode(self, QFileDialog.AnyFile)

    def show_server(self):
        self.ui_serv.show()
        # app = QApplication(sys.argv)

    def sig_text(self):
        print("信号发出去了")
        self.signal_i.emit()

    def msg(self):
        flag = QMessageBox.information(self, "程序打开提示", "欢迎进入程序", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if flag == QMessageBox.Yes:
            pass
        else:
            self.close()

    def read_style(self, style):
        with open(style, "r") as f:
            return f.read()
if __name__ == '__text6__':
    print('PyCharm')

app = QApplication(sys.argv)
f = combox_set()
f.show()
text = f.read_style("./typle.qss")
f.setStyleSheet(text)
f.signal_i.emit()
sys.exit(app.exec_())
