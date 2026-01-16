import pandas as pd
import re
import unicodedata

# Baca file CSV (pastikan nama file sesuai)
df = pd.read_csv('data_teks_svm.csv', encoding='utf-8', errors='ignore')

# Fungsi untuk membersihkan teks
def clean_text(text):
    if pd.isnull(text):
        return ""
    # pastikan teks dalam format string
    text = str(text)
    # normalisasi karakter aneh jadi format unicode standar
    text = unicodedata.normalize('NFKD', text)
    # hapus karakter non ASCII (kayak ƒ??, â€™, dll)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # ubah ke huruf kecil
    text = text.lower()
    # hapus possessive seperti argentina's
    text = re.sub(r"’s|'s", "", text)
    # hapus semua tanda baca, angka, simbol
    text = re.sub(r'[^a-z\s]', ' ', text)
    # ganti spasi ganda jadi satu
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Terapkan ke kolom teks kamu
df['text'] = df['text'].apply(clean_text)

# Simpan hasil bersih ke file baru
df.to_csv('Data_Teks_SVM_Cleaned.csv', index=False, encoding='utf-8')
print("✅ Data teks sudah dibersihkan dan disimpan ke 'Data_Teks_SVM_Cleaned.csv'")
