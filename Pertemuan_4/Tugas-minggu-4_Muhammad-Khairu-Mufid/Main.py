# Nama  : Muhammad Khairu Mufid
# NIM   : 2207421031
# Kelas : TMJ-3B

from Mobil import semua_mobil
from Pembeli import Pembeli
from Penjual import Penjual

# Instance Objek Pembeli dan Penjual
pembeli = Pembeli()
penjual = Penjual()

while True:
    print("\nSelamat datang di program pembelian mobil Toyota!\nPilih Menu:\n1. Pencarian tipe mobil\n2. Lihat semua mobil dan harga\n3. Cek Syarat Pengajuan kredit\n4. Beli mobil (Lihat tipe mobil terlebih dahulu)\n5. Tambah mobil\n6. Update model & harga mobil\n7. Hapus mobil\n8. Keluar dari program")
    
    pilihan = input("Silakan pilih menu (1/2/3/4/5/6/7/8): ")

    if pilihan == "1":
        tipe_mobil_dicari = input("\nMasukkan tipe mobil yang ingin dicari (ex: avanza, veloz, dll): ").lower()
        pembeli.cari_tipe_mobil(tipe_mobil_dicari)

    elif pilihan == "2":
        pembeli.lihat_semua_mobil()
        print("")

    elif pilihan == "3":
        jenis_kredit_dipilih = input("\nPilihan jenis kredit\n1. perorangan\n2. perusahaan\npilih jenis kredit (1/2): ")
        pembeli.pengajuan_kredit(jenis_kredit_dipilih)

    elif pilihan == "4":
        tipe_mobil_dibeli = input("\nMasukkan tipe mobil yang ingin dibeli (ex: avanza, veloz, dll): ").lower()
        pembeli.beli_mobil(tipe_mobil_dibeli)

    elif pilihan == "5":
        kategori_ditambah = input("\nMasukkan kategori mobil yang ingin ditambah (ex: MPV, SUV, dll): ")
        tipe_ditambah = input("Masukkan tipe mobil yang ingin ditambah (ex: avanza, veloz, dll): ").lower()
        model_ditambah = input("Masukkan model mobil yang ingin ditambah: ")
        harga_ditambah = input("Masukkan harga mobil yang ingin ditambah: ")
        if not kategori_ditambah or not tipe_ditambah or not model_ditambah or not harga_ditambah:
            print("\nPenambahan mobil dibatalkan. Anda harus mengisi semua bagian kategori, tipe, model, dan harga.")
        else:
            premium_ditambah = input("Masukkan harga premium color (kosongkan jika tidak ingin menambah):")
            two_tone_ditambah = input("Masukkan harga two-tone color (kosongkan jika tidak ingin menambah):")
            penjual.Tambah_Mobil(kategori_ditambah, tipe_ditambah, model_ditambah, harga_ditambah, premium_ditambah, two_tone_ditambah)

    elif pilihan == "6":
        tipe_mobil_diUpdate = input("\nMasukkan tipe mobil yang ingin di-update (ex: avanza, veloz, dll): ").lower()
        if pembeli.cari_tipe_mobil(tipe_mobil_diUpdate):
            try:
                urutan_mobil_diUpdate = int(input("\nPilih nomor model mobil yang ingin diupdate: ")) - 1
                if 0 <= urutan_mobil_diUpdate < len(semua_mobil[tipe_mobil_diUpdate]):
                    model_diUpdate = input("Masukkan model mobil yang baru (biarkan kosong jika tidak ingin mengubah): ")
                    harga_diUpdate = input("Masukkan harga mobil yang baru (biarkan kosong jika tidak ingin mengubah): ")
                    penjual.Update_Mobil(tipe_mobil_diUpdate, urutan_mobil_diUpdate, model_diUpdate, harga_diUpdate)
                else:
                    print("\nNomor model mobil tidak valid. Proses perubahan gagal.")
            except ValueError:
                print("\nMohon maaf, anda harus memasukkan angka yang tersedia")

    elif pilihan == "7":
        tipe_mobil_dihapus = input("\nMasukkan tipe mobil yang ingin dihapus (ex: avanza, veloz, dll): ").lower()
        if pembeli.cari_tipe_mobil(tipe_mobil_dihapus):
            try:
                urutan_mobil = int(input("\nPilih nomor model mobil yang ingin dihapus: ")) - 1
                penjual.Hapus_Mobil(tipe_mobil_dihapus, urutan_mobil)
            except ValueError:
                print("\nMohon maaf, anda harus memasukkan angka yang tersedia")

    elif pilihan == "8":
        print("Terima kasih, program telah selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

    input_tambahan = input("\nIngin kembali ke menu awal? (y/n): ")
    if input_tambahan.lower() != "y":
        print("Terima kasih, program telah selesai.")
        break
