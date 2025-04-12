import sys  # Sistemle ilgili işlemleri yapmak için sys'yi dahil ediyoruz
from PyQt5 import QtWidgets  # PyQt5'in widget (arayüz bileşenleri) modülünü içe aktarıyoruz

# Arayüzümüzü oluşturacak fonksiyonu tanımlıyoruz
def pencere():
    # QApplication: PyQt uygulamasının temelini oluşturur, tüm widget'lar bundan sonra çalışır
    app = QtWidgets.QApplication(sys.argv)  # sys.argv ile komut satırından gelen argümanlar alınır

    # QWidget: Pencere gibi davranan basit bir arayüz bileşeni oluşturur
    pencere = QtWidgets.QWidget()  # Boş bir pencere (widget) oluşturuyoruz


    # Pencere başlığını belirliyoruz
    pencere.setWindowTitle("My first project.")  # Pencerenin başlığını ayarlıyoruz

    # Pencereyi görünür hale getiriyoruz
    pencere.show()  # Pencereyi ekranda gösteriyoruz

    # Uygulamanın çalışmasını sağlıyoruz (olay döngüsü)
    sys.exit(app.exec_())  # Uygulama kapanana kadar çalışmaya devam eder

# Fonksiyonu çağırıyoruz, programı başlatıyoruz
pencere()  # pencere fonksiyonunu çalıştırarak uygulamayı başlatıyoruz
