import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QAction, qApp, QMainWindow

# Notepad sınıfı, uygulamanın ana penceresini oluşturuyor ve bir QWidget'ten türetiliyor
class Notepad(QWidget):
    def __init__(self):
        # Üst sınıfın (QWidget) yapıcı metodunu çağırıyoruz
        super().__init__()
        # Arayüzü oluşturmak için init_ui metodunu çağırıyoruz
        self.init_ui()

    def init_ui(self):
        # QTextEdit widget'ı, metin düzenleme alanı olarak kullanılacak
        self.yazi_alani = QTextEdit()

        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")


        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        # Dikey bir düzen (QVBoxLayout) oluşturuyoruz, metin alanı ve butonları üst üste yerleştirmek için
        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)


        self.setLayout(v_box)


        self.setWindowTitle("NotePad")

        # Butonlara tıklama olaylarını bağlıyoruz
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)



    # Metin alanını temizleyen fonksiyon
    def yaziyi_temizle(self):
        self.yazi_alani.clear()


    # Dosya açma
    def dosya_ac(self):
        # QFileDialog ile kullanıcının bir dosya seçmesini sağlıyoruz
        # İlk parametre: dialog başlığı, ikinci parametre: başlangıç dizini (kullanıcının ev dizini)
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))
        # Seçilen dosyayı okuma modunda açıyoruz
        # dosya_ismi[0] dosyanın yolunu temsil ediyor çünkü dosya ismi değişkeni bir tuple dönüyor(dosyaismi, dosya uzantısı) [0]bize sadece dosya yolunu veriyor(ilk eleman)
        with open(dosya_ismi[0], "r") as file:
            # Dosyanın içeriğini metin alanına yazıyoruz
            self.yazi_alani.setText(file.read())


    # Dosya kaydetme
    def dosya_kaydet(self):
        # QFileDialog ile kullanıcının dosya kaydetme konumu ve adını seçmesini sağlıyoruz
        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("HOME"))

        # Seçilen dosyayı yazma modunda(w) açıyoruz
        with open(dosya_ismi[0], "w") as file:
            # Metin alanındaki içeriği dosyaya yazıyoruz
            file.write(self.yazi_alani.toPlainText())


# Menu sınıfı, menü çubuğunu ve ana pencereyi oluşturuyor, QMainWindow'dan türetiliyor
class Menu(QMainWindow):
    def __init__(self):
        # Üst sınıfın (QMainWindow) yapıcı metodunu çağırıyoruz
        super().__init__()
        # Notepad sınıfından bir pencere oluşturuyoruz
        self.pencere = Notepad()
        # Notepad widget'ını ana pencerenin merkezi widget'ı olarak ayarlıyoruz
        self.setCentralWidget(self.pencere)
        # Menüleri oluşturmak için metodu çağırıyoruz
        self.menuleri_olustur()

    def menuleri_olustur(self):
        # Menü çubuğunu oluşturuyoruz
        menubar = self.menuBar()
        # "Dosya" adında bir menü ekliyoruz
        dosya = menubar.addMenu("Dosya")

        # Menü için eylemler (QAction) oluşturuyoruz
        dosya_ac = QAction("Dosya Aç", self)
        dosya_ac.setShortcut("Ctrl+O")  # Kısayol tuşu: Ctrl+O

        dosya_kaydet = QAction("Dosya Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")  # Kısayol tuşu: Ctrl+S

        temizle = QAction("Dosyayı Temizle", self)
        temizle.setShortcut("Ctrl+D")  # Kısayol tuşu: Ctrl+D

        cikis = QAction("Çıkış", self)
        cikis.setShortcut("Ctrl+Q")  # Kısayol tuşu: Ctrl+Q

        # Eylemleri menüye ekliyoruz
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        # Menüdeki bir eylemin tetiklenmesi durumunda response fonksiyonunu çağırıyoruz
        dosya.triggered.connect(self.response)

        # Pencere başlığını "Metin Editörü" olarak ayarlıyoruz
        self.setWindowTitle("Metin Editörü")
        # Pencereyi gösteriyoruz
        self.show()

    # Menü eylemlerine yanıt veren fonksiyon
    def response(self, action):
        # Hangi eylemin tetiklendiğini kontrol ediyoruz
        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()  # Dosya açma fonksiyonunu çağır
        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()  # Dosya kaydetme fonksiyonunu çağır
        elif action.text() == "Dosyayı Temizle":
            self.pencere.yaziyi_temizle()  # Metin temizleme fonksiyonunu çağır
        elif action.text() == "Çıkış":
            qApp.quit()  # Uygulamayı kapat

# QApplication nesnesi oluşturuyoruz, bu PyQt uygulamasının ana döngüsünü yönetir
app = QApplication(sys.argv)
# Menu sınıfından bir nesne oluşturuyoruz
menu = Menu()
# Uygulamayı başlatıyoruz ve sistemden çıkış yapıldığında uygulamayı kapatıyoruz
sys.exit(app.exec_())