"""
Nama    : Muhammad Khairu Mufid
NIM     : 220742101
Kelas   : TMJ 3B
"""

class Penduduk:
    def __init__(self, nama, gender, agama, pekerjaan):
        self.nama = nama
        self.gender = gender
        self.agama = agama
        self.pekerjaan = pekerjaan

    def display_information(self):
        print(f"Nama\t\t: {self.nama}")
        print(f"gender\t\t: {self.gender}")
        print(f"Agama\t\t: {self.agama}")
        print(f"pekerjaan\t: {self.pekerjaan}")
        print("=================================\n")

orang1 = Penduduk("Abdurrauf,S.Pd,M.Pd", "Laki-laki", "Islam", "PNS")
orang2 = Penduduk("Mira Setiawan", "Perempuan", "Islam", "Pegawai Swasta")
orang3 = Penduduk("Agung Nazar", "Laki-laki", "Islam", "Wiraswasta")
orang4 = Penduduk("Tuhan", "Laki-laki", "Islam", "Buruh Harian Lepas")
orang5 = Penduduk("Langgeng Rifai", "Laki-laki", "Islam", "Pelajar")

orang1.display_information()
orang2.display_information()
orang3.display_information()
orang4.display_information()
orang5.display_information()