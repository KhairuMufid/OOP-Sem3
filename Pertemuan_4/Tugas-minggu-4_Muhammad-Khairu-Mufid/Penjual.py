# Nama  : Muhammad Khairu Mufid
# NIM   : 2207421031
# Kelas : TMJ-3B

from Mobil import Mobil 
from Mobil import semua_mobil

class Penjual:
    def Tambah_Mobil(self, kategori, tipe, model, harga, premium_color=None, two_tone_color=None):
        mobil_baru = Mobil(kategori, tipe, model, harga, premium_color, two_tone_color)
        if tipe in semua_mobil:
            semua_mobil[tipe].append(mobil_baru)
        else:
            semua_mobil[tipe] = [mobil_baru]
        harga_tambahan = f""
        harga_tambahan += f" + premium color {mobil_baru.premium_color} (opsional) " if premium_color else ""
        harga_tambahan += f" + two-tone color {two_tone_color} (opsional) " if two_tone_color else ""
        
        print(f"\nMobil baru telah ditambahkan ke tipe {tipe}:\nKategori: {kategori}, Model: {model}, Harga: {harga}{harga_tambahan}")

    def Update_Mobil(self, tipe_diUpdate, index_diUpdate, model=None, harga=None):
        if tipe_diUpdate in semua_mobil and 0 <= index_diUpdate < len(semua_mobil[tipe_diUpdate]):
            mobil_diUpdate = semua_mobil[tipe_diUpdate][index_diUpdate]
            if model:
                mobil_diUpdate.model = model
            if harga:
                mobil_diUpdate.harga = harga
            if model or harga:
                print("\nData mobil telah diperbarui:")
                print(f"Kategori: {mobil_diUpdate.kategori}, Tipe: {tipe_diUpdate}, Model: {mobil_diUpdate.model}, Harga: {mobil_diUpdate.harga}")
            else:
                print("\nUpdate mobil dibatalkan. Anda tidak memasukkan input update.")
        else:
            print("\nNomor model mobil tidak valid. Proses perubahan gagal.")

    def Hapus_Mobil(self, tipe_dihapus, index):
        if tipe_dihapus in semua_mobil and 0 <= index < len(semua_mobil[tipe_dihapus]):
            mobil_hapus = semua_mobil[tipe_dihapus].pop(index)
            print("\nMobil telah dihapus dari daftar:")
            print(f"Kategori: {mobil_hapus.kategori}, Tipe: {tipe_dihapus}, Model: {mobil_hapus.model}, Harga: {mobil_hapus.harga}")
        else:
            print("\nNomor model mobil tidak valid. Proses penghapusan gagal")

