# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.client_ui import client as u2
import socket
import threading
so = socket.socket()


class MyClient(QMainWindow):
    def __init__(self, parent=None):
        super(MyClient, self).__init__(parent)
        self.ui = u2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.open_connect_Button.clicked.connect(self.start_thread)
        self.ui.send_data_pushButton.clicked.connect(self.start_thread1)
        self.ui.rcv_pushButton_2.clicked.connect(self.start_thread2)
    def start_client(self):
        host = socket.gethostname()
        server_ip = socket.gethostbyname(host)
        port = 8400
        so.connect((host, port))
        self.ui.ip_lineEdit.setText(server_ip)
        self.ui.port_lineEdit_2.setText(str(port))
        print("连接%s成功" % str(host))

    def start_thread(self):
        thread = threading.Thread(target=self.start_client)
        thread.start()
        time.sleep(1)
        thread.join()

    def start_thread1(self):
        thread = threading.Thread(target=self.send_data)
        thread.start()

    def start_thread2(self):
        thread = threading.Thread(target=self.rcv_data)
        thread.start()

    def send_data(self):
        so.send(self.ui.send_lineEdit.text().encode())

    def rcv_data(self):
        text = so.recv(1024)
        self.ui.rcv_textEdit.setText(text.decode())

def print_hi(name):
     # Use a breakpoint in the code line below to debug your script.
     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
app = QApplication(sys.argv)
mycli = MyClient()
mycli.show()
sys.exit(app.exec_())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

