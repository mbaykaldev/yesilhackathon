import os
from datetime import datetime, timedelta
from pathlib import Path


def simule_et_cv_sikistirma(orijinal_boyut_kb=500):
    """
    1. Özellik: CV Boyutunu Sıkıştırma Simülasyonu
    Görseldeki %70 - %80 arası veri transfer/emisyon tasarrufunu simüle eder.
    """
    print("=" * 60)
    print("1. ÖZELLİK: CV BOYUTUNU SIKIŞTIRMA SİMÜLASYONU")
    print("=" * 60)
    print(f"Orijinal CV Boyutu: {orijinal_boyut_kb} KB")

    # %75 sıkıştırma oranı (Görseldeki %70 - %80 hedefine uygun)
    tasarruf_orani = 0.75
    yeni_boyut_kb = orijinal_boyut_kb * (1 - tasarruf_orani)
    azalan_veri_kb = orijinal_boyut_kb - yeni_boyut_kb

    print(f"Sıkıştırma Sonrası Boyut: {yeni_boyut_kb:.2f} KB")
    print(f"Bant Genişliği Tasarrufu: %{tasarruf_orani * 100:.0f}")
    print("-> Sonuç: İnternet ağlarında transfer edilen veri miktarı (Bant genişliği) azaldı.")
    print("-> Etki: Veri transferi kaynaklı emisyonlarda yaklaşık %70 - %80 düşüş sağlandı.\n")


def simule_et_eski_veri_silme(dizin_yolu="gecici_test_arsivi", gun_siniri=30):
    """
    2. Özellik: Eski Verileri Otomatik Silme Simülasyonu
    Veri merkezlerindeki disklerin ve soğutma sistemlerinin yükünü hafifletme etkisini simüle eder.
    """
    print("=" * 60)
    print("2. ÖZELLİK: ESKİ VERİLERİ OTOMATİK SİLME SİMÜLASYONU")
    print("=" * 60)

    # Test için geçici bir klasör oluşturalım
    klasor = Path(dizin_yolu)
    klasor.mkdir(exist_ok=True)

    # Test amaçlı iki dosya oluşturalım (Biri yeni, biri eski tarihli)
    eski_dosya = klasor / "eski_cv_verisi_2023.txt"
    yeni_dosya = klasor / "guncel_cv_verisi_2026.txt"

    eski_dosya.write_text("Bu eski bir CV verisidir.")
    yeni_dosya.write_text("Bu güncel bir CV verisidir.")

    # Eski dosyanın değiştirilme tarihini 60 gün öncesine ayarlayalım
    eski_zaman = (datetime.now() - timedelta(days=60)).timestamp()
    os.utime(eski_dosya, (eski_zaman, eski_zaman))

    print(f"'{dizin_yolu}' dizini taranıyor (Sınır: {gun_siniri} gün)...")
    simdi = datetime.now()
    silinen_sayisi = 0

    for dosya_yolu in klasor.glob("*"):
        if dosya_yolu.is_file():
            dosya_mtime = datetime.fromtimestamp(dosya_yolu.stat().st_mtime)
            yas_gun = (simdi - dosya_mtime).days

            if yas_gun > gun_siniri:
                dosya_yolu.unlink()  # Dosyayı sil
                print(f"  [SİLİNDİ] {dosya_yolu.name} (Yaş: {yas_gun} gün)")
                silinen_sayisi += 1
            else:
                print(f"  [SAKLANDI] {dosya_yolu.name} (Yaş: {yas_gun} gün)")

    print(f"\n-> Sonuç: Toplam {silinen_sayisi} eski veri otomatik olarak temizlendi.")
    print("-> Etki: Veri merkezlerindeki disklerin ve soğutma sistemlerinin yükü hafifletildi.")
    print("-> Uzun Vadeli Etki: Yıllık biriken sabit karbon yükünde sürekli düşüş sağlandı.\n")

    # Temizlik sonrası geçici dosya/klasör kalıntılarını temizleyelim
    try:
        yeni_dosya.unlink(missing_ok=True)
        klasor.rmdir()
    except:
        pass


if __name__ == "__main__":
    print("\n[SÜRDÜRÜLEBİLİRLİK VE VERİ OPTİMİZASYONU SİSTEMİ BAŞLATILDI]\n")

    # 1. Özellik Testi
    simule_et_cv_sikistirma(orijinal_boyut_kb=800)

    # 2. Özellik Testi
    simule_et_eski_veri_silme()

    print("[SİMÜLASYON BAŞARIYLA TAMAMLANDI]")
