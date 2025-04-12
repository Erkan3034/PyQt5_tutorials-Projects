import sys
from PyQt5 import QtWidgets

# Ana pencere sınıfımızı QWidget'tan türetiyoruz
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        # Üst sınıfın yapıcı metodunu çağırıyoruz
        super().__init__()
        # Pencere başlığını ayarlıyoruz
        self.setWindowTitle("Buton Örneği")
        # Arayüz elemanlarını oluşturan metodu çağırıyoruz
        self.init_ui()

    def init_ui(self):
        # Ekranda görünecek yazı alanını (QLabel) oluşturuyoruz
        self.yazi_alani = QtWidgets.QLabel("Bana Henüz tıklanmadı")
        # Tıklanabilir butonu (QPushButton) oluşturuyoruz
        self.buton = QtWidgets.QPushButton("Bana tıkla")
        # Buton tıklama sayısını tutacak değişken
        self.sayac = 0

        # Dikey (vertical) yerleşim düzeni oluşturuyoruz
        vertical_box = QtWidgets.QVBoxLayout()
        vertical_box.addWidget(self.buton)  # Butonu dikey düzene ekliyoruz
        vertical_box.addWidget(self.yazi_alani)  # Yazı alanını dikey düzene ekliyoruz
        vertical_box.addStretch()  # Alt tarafa esnek boşluk ekliyoruz

        # Yatay (horizontal) yerleşim düzeni oluşturuyoruz
        horizontal_box = QtWidgets.QHBoxLayout()
        horizontal_box.addStretch()  # Sol tarafa esnek boşluk ekliyoruz
        horizontal_box.addLayout(vertical_box)  # Dikey düzeni yatay düzene ekliyoruz
        horizontal_box.addStretch()  # Sağ tarafa esnek boşluk ekliyoruz

        # Ana pencereye yatay düzeni yerleştiriyoruz
        self.setLayout(horizontal_box)

        # Butona tıklandığında çalışacak fonksiyonu bağlıyoruz
        self.buton.clicked.connect(self.butona_tiklandi)

        # Pencereyi gösteriyoruz
        self.show()

    def butona_tiklandi(self):
        # Butona her tıklandığında sayacı bir artırıyoruz
        self.sayac += 1
        # Yazı alanını güncelliyoruz
        self.yazi_alani.setText(f"Bana {self.sayac} defa tıklandı")

# PyQt uygulamasını oluşturuyoruz
app = QtWidgets.QApplication(sys.argv)
# Pencere sınıfından bir örnek oluşturuyoruz
pencere = Pencere()
# Uygulamayı çalıştırıyoruz ve kapandığında programı sonlandırıyoruz
sys.exit(app.exec_())
