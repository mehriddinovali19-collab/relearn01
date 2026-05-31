1️⃣ Kutubxona Tizimi
Kitob class yarat:
- xususiyatlar: nom, muallif, yil
- metod: malumot_kor() — kitob haqida chiqarsin

Kutubxona class yarat:
- xususiyatlar: kitoblar (bo'sh list)
- metod: kitob_qosh(kitob)
- metod: hammasi_kor() — barcha kitoblarni chiqarsin
- metod: qidir(nom) — kitob nomini qidirsin

2️⃣ Talabalar Baholar Tizimi
Talaba class yarat:
- xususiyatlar: ism, baholar (bo'sh list)
- metod: baho_qosh(baho)
- metod: urtacha() — o'rtacha bahoni qaytarsin
- metod: natija() — o'rtacha 4+ bo'lsa "O'tdi", aks holda "Qoldi"

5 ta talaba ob'ekti yasab, har biriga 4-5 ta baho qo'sh
Natijalarni chiqar

3️⃣ Mahsulotlar Do'koni
Mahsulot class yarat:
- xususiyatlar: nom, narx, soni
- metod: jami_qiymat() — narx * soni

Dokon class yarat:
- xususiyatlar: mahsulotlar (bo'sh list)
- metod: mahsulot_qosh(mahsulot)
- metod: eng_qimmat() — eng qimmat mahsulotni topsин
- metod: jami_summa() — barcha mahsulotlar summasi

4️⃣ Kontakt Kitobi
Kontakt class yarat:
- xususiyatlar: ism, telefon, email
- dictionary da saqlash: {"ism": ..., "telefon": ..., "email": ...}

KontaktKitobi class yarat:
- xususiyatlar: kontaktlar (bo'sh dictionary, kalit = ism)
- metod: qosh(kontakt)
- metod: qidir(ism)
- metod: yangilash(ism, yangi_telefon)
- metod: ochir(ism)

5️⃣ Bank Tizimi
Hisob class yarat:
- xususiyatlar: egasi, __balans (yashirin), tarix (list)
- metod: pul_qosh(miqdor) — tarixga ham yozsin
- metod: pul_yechish(miqdor) — tarixga ham yozsin
- metod: tarix_kor() — barcha operatsiyalarni chiqarsin
- metod: balans_kor()

6️⃣ Restoran Menyu
Taom class yarat:
- xususiyatlar: nom, narx, kategoriya ("shirinlik", "asosiy", "ichimlik")

Restoran class yarat:
- xususiyatlar: taomlar (bo'sh list)
- metod: taom_qosh(taom)
- metod: kategoriya_boyicha(kategoriya) — faqat shu kategoriyani chiqarsin
- metod: arzon_taom() — eng arzon taomni topsин

7️⃣ O'yinchi Reytingi
Oyinchi class yarat:
- xususiyatlar: ism, ball (0 dan boshlaydi), daraja
- metod: ball_qosh(miqdor)
- metod: daraja_yangilash():
    0-100    → "Boshlang'ich"
    101-500  → "O'rta"
    501-1000 → "Tajribali"
    1000+    → "Master"

5 ta o'yinchi yasab, ball qo'sh, darajalarini chiqar

8️⃣ Vazifalar Ro'yxati (Todo List)
Vazifa class yarat:
- xususiyatlar: nom, bajarilganmi (False), muhimlik (1-3)

TodoList class yarat:
- xususiyatlar: vazifalar (bo'sh list)
- metod: vazifa_qosh(vazifa)
- metod: bajarildi(nom) — bajarilganmi = True qilsin
- metod: bajarilmaganlar() — faqat bajarilmaganlarni chiqarsin
- metod: muhimlik_boyicha() — muhimlik 3 dan 1 ga tartiblasın

9️⃣ Maktab Jurnali
Oqituvchi class yarat:
- xususiyatlar: ism, fan

Oquvchi class yarat (Odam classidan meros olsin):
- xususiyatlar: ism, sinf, baholar (bo'sh dictionary)
  baholar = {"matematika": [], "ingliz": [], "fizika": []}
- metod: baho_qosh(fan, baho)
- metod: fan_urtacha(fan)
- metod: eng_yaxshi_fan() — o'rtachasi eng yuqori fanni topsин

🔟 Mini Telegram Bot (Eng Qiyin! 🔥)
Foydalanuvchi class yarat:
- xususiyatlar: ism, username, xabarlar (bo'sh list)

Chat class yarat:
- xususiyatlar: 
    aʼzolar (dictionary: {username: Foydalanuvchi})
    tarix (list)
- metod: azо_qosh(foydalanuvchi)
- metod: xabar_yubor(username, matn)
    → tarixga {"kimdan": username, "matn": matn} qo'shsin
- metod: tarix_kor() — barcha xabarlarni chiqarsin
- metod: eng_faol() — eng ko'p xabar yozganni topsин
