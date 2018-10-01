#no 1
"""
Buatlah program untuk mengetahui bilangan ganjil dan genap.
Contoh Output:
2 adalah bilangan genap.
5 adalah bilangan ganjil.
"""
def ganjil_genap(x):
    if (x % 2) == 0:
        return "genap"
    else:
        return "ganjil"


#no 2
"""
Buatlah operasi matriks berupa:
Penjumlahan matriks
Perkalian matriks
Pengurangan matriks
Perpangkatan matriks
Matriks yang digunakan bebas.
Contoh output:
Matriks A = [ 1 2 ]
Matriks B = [ 3 4 ]
Matriks hasil penjumlahan = [ 4 6 ]
"""
def buat_matriks():
	return [[int(input("element[%s][%s] = " % (y,x))) for x in range(1,3)] for y in range(1,3)]

def penjumlahan_matriks(matriks_a, matriks_b):
	return [[matriks_a[i][j] + matriks_b[i][j] for j in range(len(matriks_a))] for i in range(len(matriks_a))]

def perkalian_matriks(matriks_a, matriks_b):
	hasil_perkalian = []
	for i in range(len(matriks_a)):
		row = []
		for j in range(len(matriks_a)):
			tmp = 0
			for k in range(len(matriks_a)):
				tmp += matriks_a[i][k] * matriks_b[k][j]
			row.append(tmp)
		hasil_perkalian.append(row)

	return hasil_perkalian

def pengurangan_matriks(martiks_a, matriks_b):
	return [[matriks_a[i][j] - matriks_b[i][j] for j in range(len(matriks_a))] for i in range(len(matriks_a))]

def pangkat_matriks(matriks, pangkat):
	hasil_pangkat = matriks
	tmp_matriks = matriks
	for i in range(pangkat-1):
		hasil_pangkat = perkalian_matriks(tmp_matriks, matriks)
		tmp_matriks = hasil_pangkat

	return hasil_pangkat

def operasi_matriks(matriks_a, matriks_b, pangkat): 
	
	print("Hasil Penjumlahan matriks 	: ", penjumlahan_matriks(matriks_a, matriks_b))
	print("Hasil perkalian matriks 	: ", perkalian_matriks(matriks_a, matriks_b))
	print("Hasil pengurangan matriks 	: ", pengurangan_matriks(matriks_a, matriks_b))
	print("Hasil Perpangkatan matriks A 	: ", pangkat_matriks(matriks_a, pangkat))
	print("Hasil Perpangkatan matriks B 	: ", pangkat_matriks(matriks_b, pangkat))


"""
Buatlah program untuk mengetahui identitas ID kalian.
Masukkan NIM kalian, lalu berikan arti dari digit-digit yang ada di NIM tersebut.
Contoh output:
Nim : 12345678
1 menyatakan kode universitas
2 menyatakan kode fakultas
3 menyatakan kode jurusan
4 menyatakan kode angkatan
5678 menyatakan kode nomor mahasiswa.
"""
def pengenal_identitas(nim):
	print("Nim 	: ", nim)
	print(nim[:2], " menyatakan kode fakultas.")
	print(nim[2:4], " menyatakan kode jurusan.")
	print(nim[4:6], " menyatakan kode angkatan.")
	print(nim[6:], " menyatakan kode nomor mahasiswa.")

if __name__=='__main__':

	# Memanggil fungsi dan prosedure untuk soal no 1
	print("~~ Soal no 1 ~~")
	x = input("Input bilangan untuk diperiksa ganjil atau genap : ")
	print("Hasil pengecekan 		: ", ganjil_genap(int(x)))

	# Memanggil fungsi dan prosedure untuk soal no 2
	print("\n")
	print("~~ Soal no 2 ~~")
	print("Input matriks A (2 x 2) : ")
	matriks_a = buat_matriks()
	print("Input matriks B (2 x 2) : ")
	matriks_b = buat_matriks()
	pangkat = int(input("Input pangkat : "))
	operasi_matriks(matriks_a, matriks_b, pangkat)

	# Memanggil fungsi dan prosedure untuk soal no 3
	print("\n")
	print("~~ Soal no 3 ~~")
	nim = input("Input NIM anda untuk diidentifikasi : ")
	pengenal_identitas(nim)