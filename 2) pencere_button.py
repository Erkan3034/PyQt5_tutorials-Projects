import sys
from PyQt5 import QtWidgets

def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Buton örneği")
    pencere.setGeometry(500, 300, 500, 500)

    yazi = QtWidgets.QLabel(pencere)
    yazi.setText("Butona tıklanmadı...")
    yazi.setMinimumWidth(250)
    yazi.move(180, 50)

    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Tıkla!")
    buton.move(210, 100)

    # Fonksiyon dışına sayaç koyuyoruz
    sayac = {"deger": 0}  # sözlük olarak kullanıyoruz, çünkü içi değiştirilebilir

    def butona_tiklandi():
        sayac["deger"] += 1
        yazi.setText(f"Butona {sayac['deger']} defa TIKLANDI ✅")
        #print(f"Butona {sayac['deger']} defa TIKLANDI ✅")

    buton.clicked.connect(butona_tiklandi)

    pencere.show()
    sys.exit(app.exec_())

pencere()


"""
QPushButton: 	    PyQt5'te buton oluşturmaya yarar
clicked.connect():	Butona tıklanınca çalışacak fonksiyonu bağlar
setText():      	Yazı veya buton üzerindeki metni değiştirmemizi sağlar
"""
