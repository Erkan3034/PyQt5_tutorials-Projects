# Kullanıcı Girişi Uygulaması

## 📝 Proje Hakkında
Bu uygulama, PyQt5 kullanılarak geliştirilmiş basit bir kullanıcı giriş ve kayıt sistemidir. SQLite veritabanı kullanarak kullanıcı bilgilerini güvenli bir şekilde saklar ve yönetir.

## ✨ Özellikler
- Kullanıcı girişi
- Yeni kullanıcı kaydı
- Güvenli parola girişi
- SQLite veritabanı entegrasyonu
- Kullanıcı dostu arayüz
- Oturum yönetimi

## 🛠️ Kullanılan Teknolojiler
- Python 3.x
- PyQt5 (GUI için)
- SQLite3 (Veritabanı yönetimi için)

## 📋 Gereksinimler
```
PyQt5>=5.15.0
```

# Ekran Görüntüleri

![Ana Ekran](pngs/Ekran%20görüntüsü%202025-05-13%20135235.png)

![Ana Ekran](pngs/Ekran%20görüntüsü%202025-05-13%20135250.png)

![Ana Ekran](pngs/Ekran%20görüntüsü%202025-05-13%20135300.png)

![Ana Ekran](pngs/Ekran%20görüntüsü%202025-05-13%20135335.png)


## 🚀 Kurulum
1. Projeyi bilgisayarınıza klonlayın:
```bash
git clone [https://github.com/Erkan3034/PyQt5_tutorials-Projects/tree/master/Mini_Projects/Kullanıcı%20Girisi]
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Uygulamayı çalıştırın:
```bash
python main.py
```

## 💻 Kullanım

### Giriş Yapma
1. Kullanıcı adınızı girin
2. Parolanızı girin
3. "Giriş Yap" butonuna tıklayın
4. Başarılı girişte karşılama mesajı görüntülenecektir

### Kayıt Olma
1. Kullanmak istediğiniz kullanıcı adını girin
2. Parolanızı belirleyin
3. "Kayıt Ol" butonuna tıklayın
4. Kayıt başarılı olduğunda bilgilendirme mesajı görüntülenecektir

### Çıkış Yapma
- "Çıkış Yap" butonuna tıklayarak uygulamadan çıkabilirsiniz

## 🔒 Güvenlik Notları
- Kullanıcı bilgileri SQLite veritabanında saklanmaktadır
- Parolalar şu an için düz metin olarak saklanmaktadır (geliştirme aşamasında)
- Aynı kullanıcı adıyla birden fazla kayıt yapılamaz

## 🐛 Bilinen Eksikler
- Parolalar şifrelenmeden saklanmaktadır
- Parola sıfırlama özelliği bulunmamaktadır
- Kullanıcı adı ve parola için karakter sınırlaması yoktur

## 🔄 Geliştirme Planı
- [ ] Parola şifreleme
- [ ] Parola sıfırlama özelliği
- [ ] Kullanıcı profili yönetimi
- [ ] Oturum süresi sınırlaması
- [ ] Güçlü parola kontrolü

## 📝 Lisans
Bu proje MIT lisansı altında lisanslanmıştır.

## 👥 İletişim
[Linkedin](https://www.linkedin.com/in/erkanturgut1205) 
