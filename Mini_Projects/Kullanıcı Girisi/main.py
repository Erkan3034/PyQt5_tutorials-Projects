import sqlite3
import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connection = None
        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        # Veritabanı bağlantısı kur ve cursor hazırla
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(userName TEXT, password TEXT)")
        self.connection.commit()

    def init_ui(self):
        # Arayüz elemanları
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.kullanici_adi.setPlaceholderText("Kullanıcı Adınızı Girin...")

        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola.setPlaceholderText("Parolanızı Girin...")

        self.giris_yap = QtWidgets.QPushButton("Giriş Yap")
        self.kayit_ol = QtWidgets.QPushButton("Kayıt Ol")  # EKLENMİŞ
        self.yazi_alani = QtWidgets.QLabel(" ")
        self.kayit_yazi_alani = QtWidgets.QLabel(" ")

        self.cikis_yap = QtWidgets.QPushButton("Çıkış Yap")


        # Arayüz düzeni
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.kayit_yazi_alani)
        v_box.addWidget(self.kayit_ol)
        v_box.addWidget(self.giris_yap)
        v_box.addWidget(self.cikis_yap)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Kullanıcı Giriş")

        # Butonlar işlevlere baglaanıyor
        self.giris_yap.clicked.connect(self.login)
        self.kayit_ol.clicked.connect(self.register)
        self.cikis_yap.clicked.connect(self.logout)


        self.show()

    def login(self):
        username = self.kullanici_adi.text().strip()
        password = self.parola.text().strip()

        if not username or not password:
            self.yazi_alani.setText("Lütfen tüm alanları doldurın.")
            return

        self.cursor.execute("SELECT * FROM users WHERE userName = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()

        if user:
            self.yazi_alani.setText(f"Merhaba {username}!")
            self.kullanici_adi.clear()
            self.parola.clear()
        else:
            self.yazi_alani.setText("Kullanıcı adı veya parola yanlış.\nLütfen tekrar deneyiniz.")

    def register(self):
        register_user_name = self.kullanici_adi.text().strip()
        register_password = self.parola.text().strip()

        # Boş alan kontrolü
        if not register_user_name or not register_password:
            self.kayit_yazi_alani.setText("Lütfen tüm alanları doldurun.")
            return

        # Aynı kullanıcı adı var mı?
        self.cursor.execute("SELECT userName FROM users WHERE userName = ?", (register_user_name,))
        existing_user = self.cursor.fetchone()

        if existing_user:
            self.kayit_yazi_alani.setText("Bu kullanıcı adı zaten kullanılıyor.")
        else:
            self.cursor.execute("INSERT INTO users VALUES (?, ?)", (register_user_name, register_password))
            self.connection.commit()
            self.kayit_yazi_alani.setText("Kayıt başarılı!")
            self.kullanici_adi.clear()
            self.parola.clear()


    def logout(self):
        self.yazi_alani.setText("")
        self.kayit_yazi_alani.setText("")
        self.kullanici_adi.clear()
        self.parola.clear()
        pencere.close()

# Uygulamayı başlat
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
