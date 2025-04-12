import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

def pencere():
    app = QApplication(sys.argv)
    pencere = QWidget()
    pencere.setWindowTitle("BoxLayout Örneği")
    pencere.setGeometry(300, 200, 400, 200)

    # --- Butonlar oluşturuluyor ---
    buton1 = QPushButton("Buton 1")
    buton2 = QPushButton("Buton 2")
    buton3 = QPushButton("Buton 3")

    # --- Yatay (horizontal) layout ---
    h_layout = QHBoxLayout()
    h_layout.addWidget(buton1)
    h_layout.addWidget(buton2)

    # --- Dikey (vertical) layout ---
    v_layout = QVBoxLayout()
    v_layout.addLayout(h_layout)  # Yatay layout'u dikeyin içine ekledik (üst kısma)
    v_layout.addWidget(buton3)    # Altta tek başına Buton 3 olacak

    # Pencereye layout'u yerleştiriyoruz
    pencere.setLayout(v_layout)

    pencere.show()
    sys.exit(app.exec_())

pencere()


"""
QHBoxLayout()	Yatay yerleşim oluşturur (butonlar yan yana)
QVBoxLayout()	Dikey yerleşim oluşturur (bileşenler alt alta)
addWidget()	Layout içine bir widget (örneğin buton) ekler
addLayout()	Bir layout'u başka bir layout içine gömer (örn. yatayı dike)

"""