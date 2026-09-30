# Bölüm 1 - Müşteri Kaybı (Churn) Analizi Projesi

## 1. İş Problemi 
Şirketlerin karlılığını etkileyen en büyük faktörlerden biri mevcut müşteriyi elde tutmaktır. Bu projedeki temel iş problemi, telekomünikasyon/hizmet sektöründeki müşterilerin rakip firmalara geçmesi (churn) nedeniyle yaşanan ciro kaybıdır. Amacımız, geçmiş müşteri davranışlarını inceleyerek ayrılma riski yüksek profilleri tespit etmek ve bu müşterilere proaktif kampanyalar sunarak elde tutma oranını artırmaktır.

## 2. Analiz Birimi ve Veri Varsayımları
- **Analiz Birimi:** Veri setindeki her bir satır, tekil bir müşteriyi ve onun kullanım/fatura geçmişini temsil etmektedir.
- **Varsayımlar:** 
  - Müşterilerin geçmiş aylardaki fatura tutarları ve şikayet/çağrı merkezi etkileşimlerinin eksiksiz kaydedildiği varsayılmıştır. 
  - Veri setindeki "Churn" etiketinin müşterinin kendi isteğiyle ayrılmasını temsil ettiği, teknik veya yasal bir zorunluluktan kaynaklanmadığı kabul edilmiştir.

## 3. Hedef ve Zaman Ufku
- **Hedef:** Bir müşterinin hizmet aboneliğini iptal edip etmeyeceğinin (Churn = 1 veya 0) öngörülmesi.
- **Zaman Ufku:** 1 Ay (Model, müşterinin bir sonraki fatura dönemindeki kararını tahmin eder).

## 4. Başarı Metriği ve Baseline
- **Baseline:** Kurulacak modelin başarısını ölçebilmek için başlangıç noktası olarak, 'hiçbir müşteri aboneliğini iptal etmez' diyen en temel varsayım (ZeroR) referans alındı.
- **Başarı Metriği:** Sınıf dengesizliği (churn edenlerin azınlıkta olması) beklendiği için Accuracy (Doğruluk) yanıltıcı olacaktır. Bu nedenle, ayrılacak müşterileri kaçırmamak adına **Recall (Duyarlılık)** ve **F1-Score** metrikleri kullanılacaktır.

## 5. Görevin Yeniden Formüle Edilmesi
Aynı iş problemi iki farklı veri madenciliği görevi olarak aşağıdaki gibi ele alınmıştır:
1. **Sınıflandırma (Classification):** Müşterinin önümüzdeki ay ayrılıp ayrılmayacağının (Evet/Hayır) gözetimli öğrenme (Supervised Learning) ile tahmin edilmesi.
2. **Kümeleme (Clustering):** Müşterilerin demografik özellikleri ve harcama alışkanlıklarına göre gözetimsiz öğrenme (Unsupervised Learning) algoritmalarıyla segmentlere ayrılması (Örn: "Yüksek değerli sadık müşteriler", "Düşük harcamalı riskli müşteriler").

## 6. Sonuç ve İş Etkisi
Geliştirilen sınıflandırma modeli sayesinde pazarlama bütçesi tüm müşteriler yerine sadece "ayrılma riski yüksek" müşterilere odaklanacak şekilde optimize edilebilir. Kümeleme sonuçları ise, oluşturulacak promosyonların müşteri segmentlerinin karakteristik özelliklerine göre özelleştirilmesini sağlayacaktır.
