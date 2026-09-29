import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import f1_score, recall_score, precision_score, accuracy_score
from sklearn.preprocessing import StandardScaler

# ==========================================
# 0. YENİDEN ÜRETİLEBİLİRLİK (15 Puan)
# ==========================================
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
os.makedirs('figures', exist_ok=True)

# ==========================================
# 1. VERİ YÜKLEME VE TEMİZLEME
# ==========================================
# Dosya adını klasöründeki isme göre ayarladık
file_path = 'customer_churn - customer_churn.csv'
df = pd.read_csv(file_path)

print("Orijinal Veri Boyutu:", df.shape)

# ÖNEMLİ VERİ TEMİZLEME ADIMI: 
# Verideki sayılar "-1.493.348..." şeklinde hatalı formatlanmış.
# İçindeki noktaları kaldırıp makine öğrenmesinin anlayacağı 'float' tipine dönüştürüyoruz.
cols_to_clean = ['usage_score', 'late_payment', 'support_calls', 'tenure_score', 'contract_score', 'discount_score']
for col in cols_to_clean:
    df[col] = df[col].astype(str).str.replace('.', '', regex=False).astype(float)

# Özellikler (X) ve Hedef (y) ayrımı
X = df[cols_to_clean]
y = df['churn']

# Eğitim ve Test seti ayrımı (Stratify ile sınıf oranlarını koruyoruz)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y)

# ==========================================
# 2. GÖREV 1: SINIFLANDIRMA (Müşteri Kaybı Tahmini)
# ==========================================
rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=RANDOM_STATE)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

# Metrikler
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

# Baseline Metrikleri (ZeroR)
y_baseline = np.zeros_like(y_test)
base_acc = accuracy_score(y_test, y_baseline)
base_f1 = f1_score(y_test, y_baseline, zero_division=0)

# Sonuçları Kaydetme
results_df = pd.DataFrame({
    'Model_Tipi': ['Baseline (ZeroR)', 'Random Forest Classification'],
    'Accuracy': [base_acc, acc],
    'Precision': [0.0, prec],
    'Recall': [0.0, rec],
    'F1_Score': [base_f1, f1]
})
results_df.to_csv('results.csv', index=False)
print("Sınıflandırma sonuçları results.csv dosyasına kaydedildi.")

# Görsel 1: Özellik Önem Grafiği
plt.figure(figsize=(8, 5))
sns.barplot(x=rf_model.feature_importances_, y=X.columns, palette='viridis')
plt.title('Random Forest - Özellik Önem Düzeyleri')
plt.xlabel('Önem Derecesi')
plt.ylabel('Değişkenler')
plt.tight_layout()
plt.savefig('figures/feature_importance.png')
plt.close()

# ==========================================
# 3. GÖREV 2: KÜMELEME (Müşteri Segmentasyonu)
# ==========================================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=RANDOM_STATE, n_init='auto')
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Görsel 2: Kümeleme Dağılımı Grafiği (En önemli iki özelliğe göre)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='contract_score', y='tenure_score', hue='Cluster', palette='Set1', data=df, alpha=0.7)
plt.title('K-Means Müşteri Segmentasyonu')
plt.xlabel('Sözleşme Skoru (Contract Score)')
plt.ylabel('Müşteri Yaşı Skoru (Tenure Score)')
plt.legend(title='Segmentler')
plt.tight_layout()
plt.savefig('figures/customer_segments.png')
plt.close()

print("Görseller figures/ klasörüne kaydedildi. İşlem tamamlandı.")