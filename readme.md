# Film Öneri Sistemi
Bu proje, film severlere kişiselleştirilmiş film önerileri sunan bir sistem içerir. TF-IDF ve kosinüs benzerliği algoritmalarını kullanarak, kullanıcının seçtiği bir film başlığına dayanarak benzer filmleri bulur.

## Nasıl Çalışır?
**Veri Seti:** İlk adımda, TMDB (The Movie Database) veri seti kullanılarak film verileri toplanır. Bu veri seti, filmlerin başlıkları, açıklamaları, türleri, anahtar kelimeleri, oyuncuları ve yönetmenleri gibi çeşitli özellikleri içerir.

**TF-IDF ve Kosinüs Benzerliği:** Veri setindeki metin tabanlı özellikler, TF-IDF vektörlerine dönüştürülür. Ardından, kosinüs benzerliği algoritması kullanılarak her film arasındaki benzerlik skorları hesaplanır.

**Arayüz:** Kullanıcılar, Streamlit kullanarak oluşturulan arayüzü kullanarak bir film başlığı seçerler. Ardından, sistem seçilen film başlığına dayanarak en yakın filmleri bulur ve kullanıcıya sunar.

Kurulum
1. Proje dizinine gidin:
2. Gerekli kütüphaneleri yükleyin:

```python
pip install -r requirements.txt
```
3. Uygulamayı başlatın:
```python
streamlit run app.py
```

## Kullanım
1. Arayüzdeki film seçme alanından bir film başlığı seçin.
2. "Öneri Al" butonuna tıklayın.
3. En yakın filmleri görüntüleyin ve keyifli bir film deneyimi yaşayın!

https://github.com/fatihilhan42/Movie_Recommendation_System/assets/63750425/f18b9b7d-f129-4166-9771-2353e242f63a

