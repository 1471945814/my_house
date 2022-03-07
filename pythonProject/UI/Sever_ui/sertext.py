# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from UI.Sever_ui import server
import socket
import threading
from PyQt5.QtCore import *
import json
from www import textlog

class MyServer(QMainWindow,server.Ui_Form):
    signa_exist = pyqtSignal()
    client = ()
    so = []

    def __init__(self, parent=None):
        super(MyServer, self).__init__(parent)
        self.setupUi(self)
        self.log = textlog.Log()
        self.open_connect_Button.clicked.connect(self.star_server_phread)
        # self.ui.close_connect_pushButton_2.clicked.connect(self.closeEvent)
        self.send_data_pushButton.clicked.connect(self.send_data_thread)
        self.rcv_pushButton_2.clicked.connect(self.recv_data_thread)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.signa_exist.emit()

    def star_server_phread(self):
        thread = threading.Thread(target=self.star_server)
        thread.setDaemon(True)
        thread.start()

    def star_server(self):
        # so.setblocking(False)
        so = socket.socket()
        so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = socket.gethostname()
        port = 8888
        so.bind((host, port))
        so.listen(5)
        while True:
            print("等待客户连接.........")
            self.log.info(("等待客户端连接"))
            self.client =(client_so, addr) = so.accept()
            # self.client = self.client.append(client_so)
            self.ip_lineEdit.setText(str(addr[0]))
            self.port_lineEdit_2.setText(str(port))
            print("建立连接成功")
            self.log.info(("建立连接成功"))

    def close_server(self):
        self.s

    def recv_data_thread(self):
        ptread = threading.Thread(target=self.recv_Date)
        ptread.setDaemon(True)
        ptread.start()

    def recv_Date(self):
        while True:
            text = self.client[0].recv(1024)
            print(text)
            self.log.info(text)

    def send_data_thread(self):
        ptread = threading.Thread(target=self.send_data)
        ptread.setDaemon(True)
        ptread.start()

    def send_data(self):
        text = json.loads(self.send_lineEdit.text())
        self.client[0].send(text)






def print_hi(name):
     # Use a breakpoint in the code line below to debug your script.
     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

