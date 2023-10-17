# Nama  : Muhammad Khairu Mufid
# NIM   : 2207421031
# Kelas : TMJ-3B

from Mobil import semua_mobil

class Pembeli:
    def __init__(self):
        self.mobil_dipilih = None
    
    def cari_tipe_mobil(self, tipe_mobil_dicari):
        if tipe_mobil_dicari in semua_mobil:
            tipe_punya_model = semua_mobil[tipe_mobil_dicari]
            if tipe_punya_model:
                print(f"\nBerikut list model dan harga tipe mobil {tipe_mobil_dicari}")
                for index, mobil in enumerate(semua_mobil[tipe_mobil_dicari], start=1):
                    harga_tambahan = f""
                    harga_tambahan += f" + premium color {mobil.premium_color} (opsional) " if mobil.premium_color else ""
                    harga_tambahan += f" + two-tone color {mobil.two_tone_color} (opsional) " if mobil.two_tone_color else ""
                    print(f"{index}. Kategori: {mobil.kategori}, Model: {mobil.model}, Harga: {mobil.harga}{harga_tambahan}")
                return true
        elif tipe_mobil_dicari:
            print(f"Mohon maaf, mobil {tipe_mobil_dicari} tidak tersedia.")
            return false
        else:
            print("Mohon maaf, anda belum memasukkan tipe mobil")
            return false
        
    def lihat_semua_mobil (self):
        for mobil in semua_mobil:
            self.cari_tipe_mobil(mobil)

    def pengajuan_kredit(self, jenis_kredit_dipilih):
        syarat_dokumen_perorangan = ["KTP suami + istri", "Kartu keluarga", "NPWP", "PBB / AJB Rumah", "Rekening tabungan 3 bulan terakhir", "Slip gaji (bila bekerja), SKU"]

        syarat_dokumen_perusahaan = ["Fotocopy akte pendirian & perubahannya", "Fotocopy pengesahan kehakiman", "Fotocopy SIUP", "Fotocopy NPWP", "Fotocopy SITU / Domisili, TDP", "Fotocopy Rek. Koran 3 bulan terakhir", "Fotocopy KTP direksi & komisaris"]

        dokumen_belum_lengkap = []

        if jenis_kredit_dipilih == "1":
            print("\nPengajuan Kredit Perorangan")
            for dokumen in syarat_dokumen_perorangan:
                dokumen_pembeli = input(f"Apakah sudah melengkapi {dokumen}? (y/n): ").lower()
                if dokumen_pembeli != "y":
                    dokumen_belum_lengkap.append(dokumen)
        elif jenis_kredit_dipilih == "2":
            print("\nPengajuan Kredit Perusahaan")
            for dokumen in syarat_dokumen_perusahaan:
                dokumen_pembeli = input(f"Apakah sudah melengkapi {dokumen}? (y/n): ").lower()
                if dokumen_pembeli != "y":
                    dokumen_belum_lengkap.append(dokumen)
        else:
            print("\nJenis kredit tidak valid.")

        if not dokumen_belum_lengkap:
            print("\nSelamat, pengajuan kredit diterima!")
        else:
            print("\nMaaf, pengajuan kredit ditolak. Dokumen berikut belum lengkap:")
            for dokumen in dokumen_belum_lengkap:
                print(f"- {dokumen}")

    def beli_mobil(self, tipe_mobil_dibeli):
            if self.cari_tipe_mobil(tipe_mobil_dibeli):
                urutan_mobil_dibeli = int(input("\nPilih nomor model mobil yang ingin dibeli: ")) - 1
                if 0 <= urutan_mobil_dibeli < len(semua_mobil[tipe_mobil_dibeli]):
                    self.mobil_dipilih = semua_mobil[tipe_mobil_dibeli][urutan_mobil_dibeli]
                    harga_tambahan = f""
                    if self.mobil_dipilih.premium_color:
                        harga_tambahan = f" + premium color {self.mobil_dipilih.premium_color} (opsional)"
                    elif self.mobil_dipilih.two_tone_color:
                        harga_tambahan = f" + two-tone color {self.mobil_dipilih.two_tone_color} (opsional)"
                    print(f"\nMobil yang dipilih:\nKategori: {self.mobil_dipilih.kategori}\nTipe\t: {self.mobil_dipilih.tipe}\nModel\t: {self.mobil_dipilih.model}\nHarga\t: {self.mobil_dipilih.harga}{harga_tambahan}")

                    metode_beli = input("\nJenis metode pembayaran\n1. kredit\n2. cash\nPilih metode pembayaran:")
                    if metode_beli == "1":
                        jenis_kredit = input("\nPilihan jenis kredit\n1. perorangan\n2. perusahaan\nPilih jenis kredit (1/2): ")
                        self.pengajuan_kredit(jenis_kredit)
                        
                    elif metode_beli == "2":
                        print(f"\nSelamat! Pembelian mobil dengan tipe {self.mobil_dipilih.tipe} berhasil!\nTotal harga pembelian cash : {self.mobil_dipilih.harga}{harga_tambahan}")
                    else:
                        print("\nInput nomor tidak valid! silakan pilih nomor yang sesuai")
                else:
                    print("\nNomor model mobil tidak valid.")
    
