"""
Nama    : Muhammad Khairu Mufid
NIM     : 220742101
Kelas   : TMJ 3B
"""

class Mahasiswa:
    def __init__(self, nama, nilai, NIM, jurusan, prodi, kelas):
        self.nama = nama
        self.nilai = nilai
        self.NIM = NIM
        self.jurusan = jurusan
        self.prodi = prodi
        self.kelas = kelas

    def Hitung_nilai(self):
        if self.nilai >= 81:
            print("Angka Mutu\t: 4")
            print("Sebutan Mutu\t: Sangat Istimewa")
            print("Huruf Mutu\t: A")
        elif self.nilai >= 76 and self.nilai <= 80.9:
            print("Angka Mutu\t: 3,7")
            print("Sebutan Mutu\t: Istimewa")
            print("Huruf Mutu\t: A-")
        elif self.nilai >= 72 and self.nilai <= 75.9:
            print("Angka Mutu\t: 3,3")
            print("Sebutan Mutu\t: Lebih baik")
            print("Huruf Mutu\t: B+")
        elif self.nilai >= 68 and self.nilai <= 71.9:
            print("Angka Mutu\t: 3")
            print("Sebutan Mutu\t: Lebih dari baik")
            print("Huruf Mutu\t: B")
        elif self.nilai >= 64 and self.nilai <= 67.9:
            print("Angka Mutu\t: 2.7")
            print("Sebutan Mutu\t: Cukup baik")
            print("Huruf Mutu\t: B-")
        elif self.nilai >= 60 and self.nilai <= 63.9:
            print("Angka Mutu\t: 2.3")
            print("Sebutan Mutu\t: Lebih dari cukup")
            print("Huruf Mutu\t: C+")
        elif self.nilai >= 56 and self.nilai <= 59.9:
            print("Angka Mutu\t: 2")
            print("Sebutan Mutu\t: Cukup")
            print("Huruf Mutu\t: C")
        elif self.nilai >= 41 and self.nilai <= 55.9:
            print("Angka Mutu\t: 1")
            print("Sebutan Mutu\t: Kuran")
            print("Huruf Mutu\t: D")
        elif self.nilai >= 1 and self.nilai <= 40.9:
            print("Angka Mutu\t: 0")
            print("Sebutan Mutu\t: Gagal")
            print("Huruf Mutu\t: E")

    def nilaiAkhir(self):
        print(f"Nama\t\t: {self.nama}")
        print(f"NIM\t\t: {self.NIM}")
        print(f"Jurusan\t\t: {self.jurusan}")
        print(f"Prodi\t\t: {self.prodi}")
        print(f"Kelas\t\t: {self.kelas}")
        print(f"Nilai\t\t: {self.nilai}")
        self.Hitung_nilai()
        print("=====================\n")

        

mahasiswa1 = Mahasiswa("Khairu", 100, 2207421031, "TIK", "TMJ", "TMJ")
mahasiswa2 = Mahasiswa("Mudryk", 80, 2207421060, "TIK", "TMJ", "TMJ")
mahasiswa3 = Mahasiswa("Sterling", 70, 2207421061, "TIK", "TMJ", "TMJ")


mahasiswa1.nilaiAkhir()
mahasiswa2.nilaiAkhir()
mahasiswa3.nilaiAkhir()

