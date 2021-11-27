#Menambahkan data kedalam sebuah list

data=[]
while(True):
    NIM=input("Masukan NIM: ")
    Nama=input("Masukan Nama: ")
    Tugas=input("Masukan Nilai Tugas: ")
    UTS=input("Masukan Nilai UTS: ")
    UAS=input("Masukan Nilai UAS: ")
    Akhir=(int(Tugas)*.30)+(int(UTS)*.35)+(int(UAS)*.35)
    data.append([NIM, Nama, Tugas, UTS, UAS, Akhir])
    ulangi=input("Tambah data (ya/tidak)?")
    if ulangi .lower()== 'tidak' :
        break

print("\nDaftar Nama\n")
print(42*"=")
print("| NIM | Nama | Tugas | UTS | UAS | Akhir |")
print(42*"=")
for x in data:
    print("| {0:1}| {1:1} |  {2:1}  | {3:1} | {4:1} | {5:1} |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
print(42*"=")