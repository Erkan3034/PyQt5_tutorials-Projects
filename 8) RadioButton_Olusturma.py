import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()  # Arayüzü başlat

    def init_ui(self):
        # Soru: Kullanıcıya hangi dili sevdiğini soruyorum
        self.soru = QLabel("Hangi dili daha çok seviyorsun?")

        # RadioButton'lar - kullanıcı sadece birini seçebilir
        self.radio_python = QRadioButton("Python")
        self.radio_java = QRadioButton("Java")
        self.radio_php = QRadioButton("PHP")

        # Sonuç yazısı burada gösterilecek
        self.sonuc = QLabel("")

        # Gönder butonu – cevabı gösterecek
        self.buton = QPushButton("Gönder")

        # Dikey yerleşim – tüm bileşenleri sırayla yerleştiriyoruz
        v_box = QVBoxLayout()
        v_box.addWidget(self.soru)
        v_box.addWidget(self.radio_python)
        v_box.addWidget(self.radio_java)
        v_box.addWidget(self.radio_php)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.sonuc)

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)  # Layout'u pencereye uygula

        # Butona tıklanırsa click() fonksiyonunu çağır
        self.buton.clicked.connect(self.click)

        self.setWindowTitle("Dil Tercihi")  # Pencere başlığı
        self.show()  # Pencereyi göster

    def click(self):
        # Hangi buton seçilmişse ona göre sonuç yazısını değiştiriyoruz
        if self.radio_python.isChecked():
            self.sonuc.setText("Python – Hem kolay hem güçlü! 🐍")
        elif self.radio_java.isChecked():
            self.sonuc.setText("Java – Kurumsal dünyanın kralı! ☕")
        elif self.radio_php.isChecked():
            self.sonuc.setText("PHP – Web'in eski ama tecrübeli savaşçısı! 🌐")
        else:
            self.sonuc.setText("Lütfen bir dil seç! 🤔")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
