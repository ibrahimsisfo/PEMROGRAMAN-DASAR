import sys
import time


def jalanin_lirik():
    
    lirik = [
        ("HINDINA", 0.1),
        ("MA", 0.2),
        ("KALAYA..", 0.2),
        ("DINADALAW MO 'KO BAWAT GABI", 0.10),
        ("WALA MANG", 0.05),
        ("NA..KIKITA", 0.2),
        ("HAPLOS MO'Y RAMDAM PA RIN SA DILIM", 0.09),
        ("NG DAMDAMIN KOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", 0.09),
    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [0.7, 0.4, 0.7, 2, 0.8, 0.9, 0.9]
   
    print("\n== MULTO  ==")
    print("by ibo")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    
    print("// Code by ibrahim")


jalanin_lirik()