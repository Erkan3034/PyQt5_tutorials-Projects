import sys
import os
import base64
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox, QHBoxLayout, QComboBox, QCheckBox, QProgressBar)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ModernMailSender(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Erkan Mail Sender ✉️")
        self.setGeometry(500, 200, 500, 600)

        self.is_dark_mode = False

        self.base_style()

        layout = QVBoxLayout()
        layout.setSpacing(12)

        #mail sunucusu secme
        self.smtp_combo = QComboBox()
        self.smtp_combo.addItems(["smtp.gmail.com", "smtp.outlook.com", "smtp.mail.yahoo.com"])
        layout.addWidget(self.smtp_combo)

        #mail gödneren kisi secme
        self.from_input = QLineEdit()
        self.from_input.setPlaceholderText("Gönderen E-Posta")
        layout.addWidget(self.from_input)

        #uygulama sifresi(mail sunucusundan alınabilir)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Uygulama Şifresi")
        self.password_input.setEchoMode(QLineEdit.Password) #giris sifresini gizle
        layout.addWidget(self.password_input)

        #uygulama sifresini hatirla
        self.remember_checkbox = QCheckBox("Şifreyi Hatırla")
        layout.addWidget(self.remember_checkbox)

        #mail alıcısı secme
        self.to_input = QLineEdit()
        self.to_input.setPlaceholderText("Alıcı E-Postalar (virgülle ayır)")
        layout.addWidget(self.to_input)

        #mail konusu
        self.subject_input = QLineEdit()
        self.subject_input.setPlaceholderText("Konu")
        layout.addWidget(self.subject_input)

        #mail mesaji
        self.body_input = QTextEdit()
        self.body_input.setPlaceholderText("Mesajınız...")
        layout.addWidget(self.body_input)

        #progress bar
        self.progress = QProgressBar()
        self.progress.setVisible(False) # progress barı gizliyoruz
        layout.addWidget(self.progress)

        button_layout = QHBoxLayout()

        #mail gonder butonu
        self.send_button = QPushButton("Mail Gönder")
        self.send_button.clicked.connect(self.send_mail)

        #mail gonderme butonunu layout'a ekliyoruz
        button_layout.addWidget(self.send_button)

        #tema değiştirme butonu
        self.theme_button = QPushButton("🌙 Mod Değiştir")
        self.theme_button.clicked.connect(self.toggle_theme)

        #tema değiştirme butonunu layout'a ekliyoruz
        button_layout.addWidget(self.theme_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.load_saved_credentials()


    #tema değiştirme(yerel temada ggöstereceğiz)
    def base_style(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f2;
            }
            QLineEdit, QTextEdit, QComboBox {
                background: white;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #5e72e4;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #324cdd;
            }
            QProgressBar {
                height: 20px;
                border-radius: 10px;
            }
        """)

    #karanlık tema
    def dark_style(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2c2c2c;
                color: white;
            }
            QLineEdit, QTextEdit, QComboBox {
                background: #404040;
                color: white;
                border: 1px solid #666;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #6c5ce7;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #5a4bcf;
            }
            QProgressBar {
                height: 20px;
                border-radius: 10px;
            }
        """)


    #tema değiştirme butonu
    def toggle_theme(self):
        if self.is_dark_mode:
            self.base_style()
            self.is_dark_mode = False
        else:
            self.dark_style()
            self.is_dark_mode = True


    #uygulama sifresini hatirla
    def load_saved_credentials(self):
        if os.path.exists(".config"):
            with open(".config", "rb") as f:
                data = f.read().decode()
                parts = data.split("\n")
                if len(parts) == 2:
                    self.from_input.setText(parts[0])
                    self.password_input.setText(base64.b64decode(parts[1]).decode())
                    self.remember_checkbox.setChecked(True)


    def save_credentials(self):
        if self.remember_checkbox.isChecked():
            with open(".config", "wb") as f:
                encoded_password = base64.b64encode(self.password_input.text().encode()).decode()
                f.write(f"{self.from_input.text()}\n{encoded_password}".encode())


    def send_mail(self):
        self.progress.setVisible(True)
        self.progress.setValue(0)

        self.send_button.setText("Gönderiliyor...")
        self.send_button.setEnabled(False)

        QTimer.singleShot(500, self.perform_send)

    #smtplib kullanarak maili gonder
    def perform_send(self):
        try:
            smtp_server = self.smtp_combo.currentText()
            mesaj = MIMEMultipart()
            mesaj["From"] = self.from_input.text()
            alicilar = [email.strip() for email in self.to_input.text().split(",")]
            mesaj["To"] = ", ".join(alicilar)
            mesaj["Subject"] = self.subject_input.text()

            body = self.body_input.toPlainText()
            mesaj.attach(MIMEText(body, "plain"))

            mail = smtplib.SMTP(smtp_server, 587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.from_input.text(), self.password_input.text())
            mail.sendmail(mesaj["From"], alicilar, mesaj.as_string())
            mail.close()

            self.save_credentials()
            self.log_mail(mesaj)

            QMessageBox.information(self, "Başarılı ✅", "Mail başarıyla gönderildi!")
        except Exception as e:
            QMessageBox.critical(self, "Hata ❌", f"Mail gönderilemedi!\nHata: {str(e)}")
        finally:
            self.send_button.setText("Mail Gönder")
            self.send_button.setEnabled(True)
            self.progress.setValue(100)

    def log_mail(self, mesaj):
        with open("logs.txt", "a", encoding="utf-8") as log:
            log.write(f"\n---\nGönderen: {mesaj['From']}\nAlıcı(lar): {mesaj['To']}\nKonu: {mesaj['Subject']}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernMailSender()
    window.show()
    sys.exit(app.exec_())