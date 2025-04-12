import sys

from PyQt5 import QtWidgets ,QtGui

def pencere():
    app = QtWidgets.QApplication(sys.argv) # sys.argv ile komut satırından gelen argümanlar alınır

    pencere = QtWidgets.QWidget() #Ana pencere

    pencere.setWindowTitle("Pencereye yazı ve resim ekleme")

    pencere.setGeometry(200,200,500,500) #Pencere konumu ve boyutu(x,y,genilik,yükseklik)


    #Yazı ve görselleri göstermek için Java'daki sisteme benzer olan 'QLabel' kullanırız

    #Yazı için bir QLabel oluşturalım

    yazi = QtWidgets.QLabel(pencere) #Labeli pecereye yerleştirdik
    yazi.setText("Merhaba, bu ilk yazı.")
    yazi.move(150,30) #yazını penceredeki konumu


    #Resim eklemek için QLabel ve QPixmap Kullanıyoruz.
    resim = QtWidgets.QLabel(pencere) #Resim de bir QLabl içinde gösterilecek.
    pixmap = QtGui.QPixmap("python.png") #Resim dosyasını yüklüyoruz (aynı klasörde olmalı)
    resim.setPixmap(pixmap) # QLabel'a resmi yerleştiriyoruz
    resim.move(120,50)

    pencere.show()
    sys.exit(app.exec_())


pencere()

"""
QLabel: Hem yazı hem de resim göstermek için kullanılır.

QPixmap: Resimleri QLabel’a yüklemek için kullanılır.

move(x, y): Widget’ların pencere içindeki konumlarını ayarlamak için kullanılı

"""



