# Hata Riskleri ve Alınan Önlemler (Reflection)

Bu projede yanlış veya yanıltıcı sonuçlar üretilmesine yol açabilecek iki temel makine öğrenmesi riski tespit edilmiş ve aşağıdaki önlemler alınmıştır:

## Risk 1: Sınıf Dengesizliğinden (Class Imbalance) Kaynaklı Yanıltıcı Başarı
**Problem:** Müşteri kaybı (churn) senaryolarında, ayrılan müşteri sayısı (1), kalan müşteri sayısına (0) göre genellikle çok daha azdır. Model sadece verideki çoğunluğa bakarak sürekli "Müşteri ayrılmayacak (0)" tahmini yapsa bile Accuracy (Doğruluk) oranı %90'ın üzerinde çıkabilir. Bu durum, iş problemi açısından asıl hedefimiz olan "ayrılacak müşterileri yakalama" görevini tamamen başarısız kılar.
**Alınan Önlem:** 
- Sınıflandırma modelinde azınlık sınıfının hatalarına daha büyük ceza kesen `class_weight='balanced'` parametresi kullanıldı.
- Modelin başarısı Accuracy ile değil, azınlık sınıfını yakalama gücünü gösteren **Recall (Duyarlılık)** ve dengeli bir ölçüm sunan **F1-Score** metrikleriyle değerlendirildi.

## Risk 2: Veri Sızıntısı (Data Leakage)
**Problem:** Modelin, tahmin yapacağı an (gerçek dünya senaryosunda) henüz bilemeyeceği bilgileri eğitim aşamasında öğrenmesi durumudur. Örneğin, müşteri veritabanındaki "iptal_tarihi" veya sadece ayrılan müşterilere atanan "cikis_anket_skoru" gibi kolonların model eğitiminde kullanılması, test başarısını yapay bir şekilde %100'e yaklaştırır ancak model canlıya alındığında tamamen çöker.
**Alınan Önlem:** 
- Veri hazırlama (`query.sql`) ve modelleme (`solution.py`) aşamalarında analiz birimi net bir şekilde geçmiş verilerle sınırlandırıldı. Sadece karar anından *önce* bilinebilecek özellikler (geçmiş fatura ortalaması, açılan destek talebi sayısı vb.) kullanılarak sızıntı yapabilecek tüm mantıksal hataların önüne geçildi.