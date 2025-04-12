import sys

from PyQt5 import  QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.kullanici_adi.setPlaceholderText("Kullanıcı Adınızı Girin...")

        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password) #parolayı gizliyoruz(girilen karaterler gözükmez)
        self.parola.setPlaceholderText("Parolanızı Girin...")

        self.giris_yap = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani= QtWidgets.QLabel(" ") #bos bir yazi alanı olusturduk(geri bildirim için)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris_yap)



        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch() # yatayda sola boşluk ekliyoruz
        h_box.addLayout(v_box) # v_box'i h_box'in icerisine ekliyoruz
        h_box.addStretch() # yatayda saga boşluk ekliyoruz

        self.setLayout(h_box)
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Kullanıcı Giriş")
        self.show()



app = QtWidgets.QApplication(sys.argv)

pencere= Pencere()

sys.exit(app.exec_()) #uygulamanın açık kalamsını sağlayan döngü
