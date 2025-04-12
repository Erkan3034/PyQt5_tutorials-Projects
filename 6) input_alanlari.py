import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QIntValidator

def pencere():
    app = QApplication(sys.argv)
    pencere = QWidget()
    pencere.setWindowTitle("Gelişmiş Input Alanları")
    pencere.setGeometry(300, 200, 400, 400)

    # --- Inputlar ---
    input_ad = QLineEdit()
    input_ad.setPlaceholderText("Adınızı girin...")  # Kullanıcıya ipucu

    input_email = QLineEdit()
    input_email.setPlaceholderText("E-posta adresinizi girin...")

    input_yas = QLineEdit()
    input_yas.setPlaceholderText("Yaşınızı girin (Sadece sayı)")
    input_yas.setValidator(QIntValidator())  # Sadece sayı girilebilir

    input_sifre = QLineEdit()
    input_sifre.setPlaceholderText("En az 6 karakterli şifre")
    input_sifre.setEchoMode(QLineEdit.Password)

    btn_gonder = QPushButton("Gönder")

    # --- Doğrulama Fonksiyonu ---
    def form_kontrol():
        ad = input_ad.text().strip()
        email = input_email.text().strip()
        yas = input_yas.text().strip()
        sifre = input_sifre.text()

        # E-posta regex kontrolü
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            QMessageBox.warning(pencere, "Hata", "Geçerli bir e-posta adresi girin.")
            return

        # Şifre uzunluğu kontrolü
        if len(sifre) < 6:
            QMessageBox.warning(pencere, "Hata", "Şifreniz en az 6 karakter olmalı.")
            return

        # Tüm alanlar dolu mu?
        if not ad or not yas:
            QMessageBox.warning(pencere, "Hata", "Lütfen tüm alanları doldurun.")
            return

        # Başarılı durum
        QMessageBox.information(
            pencere, "Başarılı",
            f"Girişler başarılı!\nAd: {ad}\nE-posta: {email}\nYaş: {yas}"
        )

    # --- Butona fonksiyon bağla ---
    btn_gonder.clicked.connect(form_kontrol)

    # --- Layout ---
    layout = QVBoxLayout()
    layout.addWidget(QLabel("Ad:"))
    layout.addWidget(input_ad)
    layout.addWidget(QLabel("E-posta:"))
    layout.addWidget(input_email)
    layout.addWidget(QLabel("Yaş:"))
    layout.addWidget(input_yas)
    layout.addWidget(QLabel("Şifre:"))
    layout.addWidget(input_sifre)
    layout.addWidget(btn_gonder)

    pencere.setLayout(layout)
    pencere.show()
    sys.exit(app.exec_())

pencere()


"""
QLineEdit()	Metin giriş kutusu
setText("..."):   Kutunun içeriğini programla ayarlama
text():           Kutunun içindeki kullanıcı girişini alma
setEchoMode(QLineEdit.Password)	: Yazılan karakterleri gizler (şifre için)

"""
