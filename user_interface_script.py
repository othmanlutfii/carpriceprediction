import pandas as pd
import pickle
import os
import numpy as np


def interface():
    os.system("cls")
    print("                                   SELAMAT DATANG DI AUTOBAHN                            ")
    print("  =========================================================================================================      ")
    tulisan = '''
                     Program ini ditujukan untuk memprediksi harga mobil berdasarkan beberapa 
                    spesifikasi yang anda masukan. metode yang kami gunakan untuk memprediksi 
                            harga mobil anda adalah multiple linear regression.
                            
                            Berikut merupakan spesifikasi yang anda perlu masukkan !
    
    Variabel Prediktor / Independen:
    a) Variabel Kualitatif
    1. Fueltype         : Jenis bahan bakar mobil ( gas / diesel )
    2. Aspiration       : Performa mesin mobil (Turbo/std)
    3. Doornumber       : Jumlah pintu mobil (dua/empat)
    4. Carbody          : Bentuk mobil (convertible, hatchback, sedan, wagon, dan hardtop)
    5. Drivewheel       : Jenis sistem penggerak mobil (FWD, RWD, dan 4WD)
    6. Enginelocation   : Letak mesin mobil ( depan /belakang )
    7. Enginetype       : Jenis mesin mobil (dohc, ohcv,cdcdcdad ohc, 4.dohcv, ohcf, rotor, dan 1)
    8. Cylindernumber   : jumlah silinder mobil untuk menggerakkan mesin (3, 2, 4, 5, 6, 8, dan 12)

    b) Variabel Kuantitatif
    1. Wheelbase        : Ukuran jarak antara ban depan dan belakang
    2. Horsepower       : satuan daya yang setara dengan tenaga kuda
    
    Sumber
    Dataset: https: // www.kaggle.com / hellbuoy / car - price - prediction /?select = CarPrice_Assignment.csv
     '''

    print(tulisan)
    mulai = input('apakah anda ingin mengestimasi harga mobil: \n1.ya \n2.tidak \n--->')
    if mulai == 'ya':
        inputan()
    else:
        print("terima kasih sudah mengunjungi")

def inputan():

    os.system("cls")
    model = pickle.load(open('saved model','rb'))
    list_jawaban = []
    hp = int(input("Berapakah besaran Horse power mobil anda (ex:150):"))
    list_jawaban.append(hp)

    wb = int(input("Berapakah panjang wheelbase mobil anda (ex:80):"))
    list_jawaban.append(wb)
    loops = True
    while loops == True:
        bensin = input("Masukan jenis bahan bakar anda: \n1.Bensin \n2.Solar \n--->")
        bensin=bensin.lower()
        if bensin == "bensin" :
            list_jawaban.append(1)
            break
        elif bensin == 'solar' :
            list_jawaban.append(0)
            break
        else:
            print(f'Maaf, input {bensin} tidak kami temukan')
            continue
    while loops == True:
        mesin_turbo = input("Apakah mesin mobil anda berturbo: \n1.ya \n2.tidak \n--->")
        mesin_turbo = mesin_turbo.lower()
        if mesin_turbo == "ya":
            list_jawaban.append(1)
            break
        elif mesin_turbo == 'tidak':
            list_jawaban.append(0)
            break
        else:
            print(f'Maaf, input {mesin_turbo} tidak kami temukan')
            continue
    while loops == True:
        pintu = input("Berapakah jumlah pintu mobil anda: \n1.2 \n2.4 \n--->")
        if pintu == "2" :
            list_jawaban.append(1)
            break
        elif pintu == "4" :
            list_jawaban.append(0)
            break
        else:
            print(f'Maaf, input {pintu} tidak kami temukan')
            continue
    while loops == True:
        penggerak = input("Apa penggerak mobil anda: \n1.FWD \n2.RWD \n3.4WD \n--->")
        penggerak = penggerak.lower()
        if penggerak == "fwd" :
            list_jawaban.append(1)
            list_jawaban.append(0)
            break
        elif penggerak == "rwd" :
            list_jawaban.append(0)
            list_jawaban.append(1)
            break
        elif penggerak == "4wd" :
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        else:
            print(f'Maaf, input {penggerak} tidak kami temukan')
            continue
    while loops == True:
        letak_mesin = str(input("Dimanakah letak mesin mobil anda: \n1.Depan \n2.Belakang \n--->"))
        letak_mesin = letak_mesin.lower()
        if letak_mesin == "depan" :
            list_jawaban.append(0)
            break
        elif letak_mesin == "belakang" :
            list_jawaban.append(1)
            break
        else:
            print(f'Maaf, input {letak_mesin} tidak kami temukan')
            continue
    while loops == True:
        jenis_mobil = input("Apa jenis mobil anda: \n1.convertible \n2.hatchback \n3.sedan \n4.wagon \n5.hardtop \n--->")
        jenis_mobil = jenis_mobil.lower()
        if jenis_mobil == 'convertible':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif jenis_mobil == 'hatchback':
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif jenis_mobil == 'sedan':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            break
        elif jenis_mobil == 'hardtop':
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif jenis_mobil == 'wagon':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            break
        else:
            print(f'Maaf, input {jenis_mobil} tidak kami temukan')
            continue
    while loops == True:
        type_mesin = input("Apa Jenis mesin anda: \n1.dohc \n2.ohcv \n3.ohc \n4.dohcv \n5.ohcf \n6.rotor \n7.1 \n--->")
        type_mesin = type_mesin.lower()
        if type_mesin == 'dohc':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif type_mesin == 'ohcv':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            break
        elif type_mesin == 'ohc':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif type_mesin == '1':
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif type_mesin == 'rotor':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            break
        elif type_mesin == 'ohcf':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif type_mesin == 'dohcv':
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        else:
            print(f'Maaf, input {type_mesin} tidak kami temukan')
            continue
    while loops == True:
        cylinder = (input('Berapa jumlah cylinder mobil anda: \n1.3 \n2.2 \n3.4 \n4.5 \n5.6 \n6.8 \n7.12 \n--->'))
        if cylinder == '5':
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif cylinder == '4':
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif cylinder == '6':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif cylinder == '3':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif cylinder == '12':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            list_jawaban.append(0)
            break
        elif cylinder == '8':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            break
        elif cylinder == '2':
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(0)
            list_jawaban.append(1)
            break
        else:
            print(f'Maaf, input {cylinder} tidak kami temukan')
            continue
    os.system("cls")

    prediksi = np.array([list_jawaban])
    harga_mobil = model.predict(prediksi)
    harga_mobil = harga_mobil[0]*17262
    harga_mobil = round(harga_mobil)
    d = {'Bahan Bakar': [bensin],'Aspiration': [mesin_turbo],'Jumlah Pintu': [pintu],'Penggerak': penggerak,'Letak Mesin': [letak_mesin],'Jenis Mobil': [jenis_mobil],'Jenis Mesin':[type_mesin],'Jumlah Silinder':[cylinder],'Harga mobil':[harga_mobil]}
    df_hasil = pd.DataFrame(d)
    output = '''------------------------------------- HASIL PREDIKSI HARGA MOBIL ANDA --------------------------------------------------'''
    print(output)

    tulisan1 = '''  \n    Dari hasil perhitungan model yang kami buat, maka prediksi harga mobil anda adalah sebagai berikut:'''
    print(tulisan1)
    print(" ")
    print(f'                              - Estimasi harga mobil anda adalah: Rp.{harga_mobil} -')
    print(" ")
    print('                                 Berikut rincian spesifikasi mobil yang anda masukan:',
          '\n', df_hasil)
    print(
        '''\n------------------------------------- HASIL PREDIKSI HARGA MOBIL ANDA --------------------------------------------------''')

    coba_lagi = input('Apakah anda ingin mencoba lagi:')
    if coba_lagi == 'ya':
        inputan()
    else:
        print("\nTerima kasih sudah mengunjungi ")


interface()





