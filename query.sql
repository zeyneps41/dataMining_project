-- query.sql
-- Müşteri verisi halihazırda tekilleştirilmiş (customer_id bazında) olduğu için,
-- modelleme aşamasında kullanılacak özellikleri (feature) doğrudan seçiyoruz.

SELECT 
    customer_id,
    usage_score,
    late_payment,
    support_calls,
    tenure_score,
    contract_score,
    discount_score,
    churn AS target_churn
FROM customer_churn;