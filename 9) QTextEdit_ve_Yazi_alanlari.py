import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout

class Pencere(QWidget):
    def __init__(self): #consturtor
        super().__init__()      # QMainWindow'un init'ini çalıştır
        self.init_ui()          # Arayüzü kuran metodumuzu çağır

    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.yazi_alani.setPlaceholderText("Mesajını yaz...")

        self.temizle = QPushButton("Temizle")
        self.mesaj = QLabel("")

        # Bu değişkenle ilk yazma mı, temizle sonrası mı olduğunu kontrol ediyoruz
        self.ilk_temizle = False

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.mesaj)

        self.setLayout(v_box)
        self.setWindowTitle("Yazı Alanı")

        self.temizle.clicked.connect(self.click)
        self.yazi_alani.textChanged.connect(self.yazi_degisti) # Yazı alanında bir değişiklik olunca yazi_degisti fonksiyonunu tetikliyoruz

        self.show()

    def click(self):
        self.yazi_alani.clear()
        self.mesaj.setText("Niye sildin ki? 🥲 Yazıyordun güzel güzel...")
        # Kullanıcı sildi, bir sonraki yazmada mesajı göster
        self.ilk_temizle = True


    def yazi_degisti(self):
        # Yazı yazılıyor ama ilk kez silinip yazılıyorsa mesaj ver
        if self.yazi_alani.toPlainText().strip():
            if self.ilk_temizle:
                self.mesaj.setText("Süper! hadi bir şeyler yaz...")
                self.ilk_temizle = False  # Tekrar tekrar yazmasın diye sıfırlıyoruz

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
