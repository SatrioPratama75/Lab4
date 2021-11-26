print(30*"=")

#Membuat List
r = [1,3,9,6,"satrio"]
s = []

#Akses List
print(r[2]) #Menampilkan Elemen Ke-3
print(r[1:4]) #Mengambil Elemen ke-2 hingga ke-4
print(r[4]) # Mengambil Elemen Terakhir

print(30*"=")

#Ubah Element List
r[3]=10
print (r) #Mengubah Nilai Ke-4
r[3:5]= 5,"saha"
print (r) #Mengubah Elemen Ke-4 s/d Terakhir

print(30*"=")

#Tambah Element List
s.append(r[3:5])
print(s) # Mengambil 2 bagian dari List r Dan Dijadikan List s 
s.extend(["iyeu"])
print(s) #
s.extend([2,3,4])
print(s)

print(30*"=")