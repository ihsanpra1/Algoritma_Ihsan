
#print(rata_rata)
nalgoritma = int(input("Masukkan Nilai Algoritma:"))
nagama = int(input("Masukkan Nilai Agama:"))
nbasisdata = int(input("Masukkan Nilai Basis Data:"))
nfisika = int(input("Masukkan Nilai Fisika:"))
nkimia = int(input("Masukkan Nilai Kimia:"))
npancasila = int(input("Masukkan Nilai Pancasila:"))
nbahasainggris = int(input("Masukkan Nilai Bahasa Inggris:"))

rata_rata = (nalgoritma + nagama + nbasisdata + nfisika + nkimia + npancasila + nbahasainggris) / 7

#penentuan lulus atau tidak 
if rata_rata >=80 and rata_rata <=100:
    #kondisi jika terpenuhi
    #maka
    print("Nilai : A")
elif rata_rata >=70 and rata_rata <=80:
    print("Nilai : B")
elif rata_rata >=50 and rata_rata <=70:
    print("nilai : c")
elif rata_rata >=30 and rata_rata <=50:
    print("nilai : D")
elif rata_rata >=0 and rata_rata <=20:
    print("nilai : E")    
else :
    # cukup menjadi hasil
    #maka
    print("Nilai lebih dari 100 atau dibawah 50")