import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication, QCheckBox, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QLineEdit
)

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Kullanıcıdan isim almak için giriş kutusu (QLineEdit)
        self.ad_giris = QLineEdit()
        self.ad_giris.setPlaceholderText("Adını yaz bro 😎")

        # Checkboxlarımız
        self.checkbox1 = QCheckBox("Kod yazıyor musun?")
        self.checkbox2 = QCheckBox("Python biliyor musun?")
        self.checkbox3 = QCheckBox("Java çalışıyor musun?")

        # Yazı alanı
        self.yazi_alani = QLabel("")

        # Buton ve başlangıçta pasif (çünkü checkbox seçili değil)
        self.buton = QPushButton("Cevapla")
        self.buton.setEnabled(False)

        # Layout ayarları
        v_box = QVBoxLayout()
        v_box.addWidget(self.ad_giris)
        v_box.addWidget(self.checkbox1)
        v_box.addWidget(self.checkbox2)
        v_box.addWidget(self.checkbox3)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Gelişmiş CheckBox Uygulaması")

        # Checkboxlara tıklanınca buton aktif/pasif olsun
        self.checkbox1.stateChanged.connect(self.checkbox_kontrol)
        self.checkbox2.stateChanged.connect(self.checkbox_kontrol)
        self.checkbox3.stateChanged.connect(self.checkbox_kontrol)

        # Buton tıklanınca click fonksiyonu çağrılacak
        self.buton.clicked.connect(self.click)

        self.show()

    def checkbox_kontrol(self):
        # En az bir checkbox işaretliyse buton aktif olsun
        if self.checkbox1.isChecked() or self.checkbox2.isChecked() or self.checkbox3.isChecked():
            self.buton.setEnabled(True)
        else:
            self.buton.setEnabled(False)

    def click(self):
        ad = self.ad_giris.text()  # Kullanıcının adını alıyoruz
        mesaj = f"{ad}, değerlendirmene bakalım:\n\n"

        if self.checkbox1.isChecked():
            mesaj += "✔ Kod yazıyorsun, harikasın!\n"
        else:
            mesaj += "❌ Kod yazmaya başlamalısın!\n"

        if self.checkbox2.isChecked():
            mesaj += "✔ Python iyi gidiyor gibi 🐍\n"
        else:
            mesaj += "❌ Python öğrenmeye başlamalısın.\n"

        if self.checkbox3.isChecked():
            mesaj += "✔ Java çalışıyorsun, müthiş ☕\n"
        else:
            mesaj += "❌ Java’yı da listene eklemelisin.\n"

        self.yazi_alani.setText(mesaj)

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
