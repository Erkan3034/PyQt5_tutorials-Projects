import sys
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QMessageBox, QFileDialog, QColorDialog
)
from PyQt5.QtGui import QColor


def pencere():
    app = QApplication(sys.argv)
    pencere = QWidget()
    pencere.setWindowTitle("Buton Fonksiyonları")
    pencere.setGeometry(300, 200, 400, 400)

    # --- Arayüz elemanları ---
    yazi = QLabel("Hoş geldin Erkan!", pencere)

    btn_yazi_degistir = QPushButton("Yazıyı Değiştir")
    btn_mesaj = QPushButton("Mesaj Kutusu Göster")
    btn_dosya_sec = QPushButton("Dosya Seç")
    btn_renk_sec = QPushButton("Renk Seç")
    btn_web = QPushButton("Web Sitesine Git")
    btn_gizle_goster = QPushButton("Yazıyı Gizle/Göster")
    btn_kapat = QPushButton("Pencereyi Kapat")

    # --- Fonksiyonlar ---
    def yazi_degistir():
        yazi.setText("Yazı değişti!")

    def mesaj_kutusu():
        QMessageBox.information(pencere, "Bilgi", "Bu bir bilgi mesajı!")

    def dosya_sec():
        dosya_adi, _ = QFileDialog.getOpenFileName(pencere, "Bir dosya seç", "", "Tüm Dosyalar (*)")
        if dosya_adi:
            yazi.setText(f"Seçilen: {dosya_adi}")

    def renk_sec():
        renk = QColorDialog.getColor()
        if renk.isValid():
            pencere.setStyleSheet(f"background-color: {renk.name()};")

    def siteye_git():
        webbrowser.open("https://www.python.org")

    def gizle_goster():
        if yazi.isVisible():
            yazi.hide()
        else:
            yazi.show()

    def kapat():
        pencere.close()

    # --- Butonlara fonksiyon bağlama ---
    btn_yazi_degistir.clicked.connect(yazi_degistir)
    btn_mesaj.clicked.connect(mesaj_kutusu)
    btn_dosya_sec.clicked.connect(dosya_sec)
    btn_renk_sec.clicked.connect(renk_sec)
    btn_web.clicked.connect(siteye_git)
    btn_gizle_goster.clicked.connect(gizle_goster)
    btn_kapat.clicked.connect(kapat)

    # --- Layout ayarları ---
    layout = QVBoxLayout()
    layout.addWidget(yazi)
    layout.addWidget(btn_yazi_degistir)
    layout.addWidget(btn_mesaj)
    layout.addWidget(btn_dosya_sec)
    layout.addWidget(btn_renk_sec)
    layout.addWidget(btn_web)
    layout.addWidget(btn_gizle_goster)
    layout.addWidget(btn_kapat)

    pencere.setLayout(layout)
    pencere.show()
    sys.exit(app.exec_())


pencere()

"""
QMessageBox.information()	Bilgi mesajı kutusu açar
QFileDialog.getOpenFileName()	Dosya seçme penceresi
QColorDialog.getColor()	Renk seçici pencere
webbrowser.open(url)	Tarayıcıda URL açar
hide() / show()	Bir elementi gizler/gösterir
close()	Pencereyi kapatır

"""
