# Nama  : Muhammad Khairu Mufid
# NIM   : 2207421031
# Kelas : TMJ-3B


class Mobil:
    def __init__(self, kategori, tipe, model, harga):
        self.kategori = kategori
        self.tipe = tipe
        self.model = model
        self.harga = harga

mobil_info = {
    "avanza": [
        Mobil("MPV", "All New Avanza", "1.3 MT","Rp 233.100.000"),
        Mobil("MPV", "All New Avanza", "1.3 CVT", "Rp 247.800.000"),
        Mobil("MPV", "All New Avanza", "1.5 GMT", "Rp 255.100.000"),
        Mobil("MPV", "All New Avanza", "1.5 G CVT", "Rp 268.800.000"),
        Mobil("MPV", "All New Avanza", "1.5 G CVT TSS", "Rp 295.800.000")
    ],
    "calya": [
        Mobil("MPV", "All New Calya", "1.2 E MT STD", "Rp 160.900.000"),
        Mobil("MPV", "All New Calya", "1.2 EMT", "Rp 163.800.000"),
        Mobil("MPV", "All New Calya", "1.2 G MT", "Rp 169.400.000"),
        Mobil("MPV", "All New Calya", "1.2 G AT", "Rp 183.600.000")
    ],
    "veloz": [
        Mobil("MPV", "All New Velloz", "1.5 MT", "Rp 286.000.000"),
        Mobil("MPV", "All New Velloz", "1.5 Q CVT", "Rp 309.100.000"),
        Mobil("MPV", "All New Velloz", "1.5 Q CVT TSS", "Rp 331.100.000")
    ],
    "alphard": [
        Mobil("MPV", "All New Alphard", "2.5 G AT", "Rp 1.344.800.000"),
    ],
    "velfire": [
        Mobil("MPV", "All New Velfire", "2.5 Velfire", "Rp 1.359.600.000")
    ],
    "innova zenix": [
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 G CVT", "Rp 419.000.000"),
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 V CVT", "Rp 467.000.000"),
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 G HV CVT", "Rp 458.000.000"),
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 V HV CVT", "Rp 532.000.000"),
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 Q HV CVT", "Rp 611.000.000")
    ],
    "rush": [
        Mobil("SUV", "All New Rush", "G MT", "Rp 278.800.000"),
        Mobil("SUV", "All New Rush", "G AT", "Rp 289.600.000"),
        Mobil("SUV", "All New Rush", "GR MT", "Rp 291.500.000"),
        Mobil("SUV", "All New Rush", "GR AT", "Rp 302.200.000")
    ],
    "raize": [
        Mobil("SUV", "All New Raize", "G MT", "Rp 232.400.000"),
        Mobil("SUV", "All New Raize", "G CVT", "Rp 247.300.000"),
        Mobil("SUV", "All New Raize", "G MT", "Rp 251.900.000"),
        Mobil("SUV", "All New Raize", "G CVT", "Rp 266.900.000"),
        Mobil("SUV", "All New Raize", "GR CVT", "Rp 280.800.000"),
        Mobil("SUV", "All New Raize", "GR CVT TSS", "Rp 302.500.000")
    ],
    "fortuner": [
        Mobil("SUV", "All New Fortuner", "VRZ (4x2)", "Rp 606.200.000"),
        Mobil("SUV", "All New Fortuner", "VRZ GR (4x2)", "Rp 624.950.000"),
        Mobil("SUV", "All New Fortuner", "VRZ GR (4x4)", "Rp 715.350.000")
    ],
    "corolla cross": [
        Mobil("SUV", "All New Corolla Cross", "Hybrid AT", "Rp 540.900.000")
    ],
    "agya": [
        Mobil("Hatchback", "All New Agya", "G MT STD", "Rp 159.700.000"),
        Mobil("Hatchback", "All New Agya", "G AT STD", "Rp 173.300.000"),
        Mobil("Hatchback", "All New Agya", "GR MT", "Rp 165.500.000"),
        Mobil("Hatchback", "All New Agya", "GR AT", "Rp 181.500.000")
    ],
    "yaris": [
        Mobil("Hatchback", "All New Yaris", "G CVT 3 AB", "Rp 295.800.000"),
        Mobil("Hatchback", "All New Yaris", "S MT GR 3 AB", "Rp 308.100.000"),
        Mobil("Hatchback", "All New Yaris", "S CVT GR 3AB", "Rp 320.300.000"),
        Mobil("Hatchback", "All New Yaris", "S CVT GR 7AB", "Rp 325.700.000")
    ],
    "corolla altis": [
        Mobil("Sedan", "All New Corolla Altis", "Hybrid AT", "Rp 514.200.000")
    ],
    "camry": [
        Mobil("Sedan", "All New Corolla Camry", "2.5 V AT", "Rp 741.700.000"),
        Mobil("Sedan", "All New Corolla Camry", "1.5 L AT", "Rp 874.600.000")
    ],
    "vios": [
        Mobil("Sedan", "All New Vios", "1.5 E MT", "Rp 314.900.000"),
        Mobil("Sedan", "All New Vios", "1.5 G CVT", "Rp 355.200.000"),
        Mobil("Sedan", "All New Vios", "1.5 G CVT TSS", "Rp 368.400.000")
    ],
    "GR 86": [
        Mobil("Sport", "All New GR 86", "GR 86 2.4L M/T", "Rp 922.000.000"),
        Mobil("Sport", "All New GR 86", "GR 86 2.4L A/T", "Rp 938.500.000")
    ],
    "supra": [
        Mobil("Sport", "All New Supra", "SUPRA 3.0L A/T", "Rp 2.051.000.000")
    ],
    "hiace": [
        Mobil("Commercial", "All New Hiace", "COMMUTER MT", "Rp 545.000.000"),
        Mobil("Commercial", "All New Hiace", "PREMIO MT", "Rp 630.000.000")
    ],
    "hilux": [
        Mobil("Commercial", "All New Hilux", "SC 2.0 MT BSN", "Rp 269.900.000"),
        Mobil("Commercial", "All New Hilux", "SC 2.4 MT DSL", "Rp 290.900.000"),
        Mobil("Commercial", "All New Hilux", "SC 2.4 MT 4x4 DSL", "Rp 393.800.000"),
        Mobil("Commercial", "All New Hilux", "DC E MT 4x4 DSL", "Rp 431.000.000"),
        Mobil("Commercial", "All New Hilux", "DC G MT 4x4 DSL", "Rp 464.000.000"),
        Mobil("Commercial", "All New Hilux", "DC V AT 4x4 DSL", "Rp 513.600.000"),
    ],
}

class Pembeli:
    def __init__(self):
        self.mobil_dipilih = None
    
    def cari_tipe_mobil(self, tipe_mobil):
        if tipe_mobil in mobil_info:
            print(f"\nBerikut list model dan harga mobil {tipe_mobil}")
            for index, mobil in enumerate(mobil_info[tipe_mobil], start=1):
                print(f"{index}. Kategori: {mobil.kategori}, Model: {mobil.model}, Harga: {mobil.harga}")
            return True
        else:
            print(f"Mobil {tipe_mobil} tidak tersedia.")
            return False

    def beli_mobil(self, tipe_mobil):
            if self.cari_tipe_mobil(tipe_mobil):
                urutan_mobil = int(input("\nPilih nomor model mobil yang ingin dibeli: ")) - 1
                if 0 <= urutan_mobil < len(mobil_info[tipe_mobil]):
                    self.mobil_dipilih = mobil_info[tipe_mobil][urutan_mobil]
                    print("\nMobil yang dipilih:")
                    print(f"Kategori: {self.mobil_dipilih.kategori}")
                    print(f"Tipe\t: {self.mobil_dipilih.tipe}")
                    print(f"Model\t: {self.mobil_dipilih.model}")
                    print(f"Harga\t: {self.mobil_dipilih.harga}")
                    metode_beli = input("\nJenis metode pembayaran\n1. kredit\n2. cash\nPilih metode pembayaran:")
                    if metode_beli == "1":
                        jenis_kredit = input("\nPilihan jenis kredit\n1. perorangan\n2. perusahaan\nPilih jenis kredit (1/2): ")
                        self.pengajuan_kredit(jenis_kredit)
                    elif metode_beli == "2":
                        print(f"Total harga pembelian cash : {self.mobil_dipilih.harga}")
                    else:
                        print("Input nomor tidak valid! silakan pilih nomor yang sesuai")
                else:
                    print("Nomor model mobil tidak valid.")

    def syarat_kredit(self, jenis_kredit):
        dokumen_perorangan = ["KTP suami + istri", "Kartu keluarga", "NPWP", "PBB / AJB Rumah", "Rekening tabungan 3 bulan terakhir", "Slip gaji (bila bekerja), SKU"]

        dokumen_perusahaan = ["Fotocopy akte pendirian & perubahannya", "Fotocopy pengesahan kehakiman", "Fotocopy SIUP", "Fotocopy NPWP", "Fotocopy SITU / Domisili, TDP", "Fotocopy Rek. Koran 3 bulan terakhir", "Fotocopy KTP direksi & komisaris"]
        
        if jenis_kredit == "1":
            print("\nSyarat Pengajuan Kredit Perorangan:")
            for dokumen in dokumen_perorangan:
                print(f"- {dokumen}")
        elif jenis_kredit == "2":
            print("\nSyarat Pengajuan Kredit Perusahaan:")
            for dokumen in dokumen_perusahaan:
                print(f"- {dokumen}")

    def pengajuan_kredit(self, jenis_kredit):
        dokumen_perorangan = ["KTP suami + istri", "Kartu keluarga", "NPWP", "PBB / AJB Rumah", "Rekening tabungan 3 bulan terakhir", "Slip gaji (bila bekerja), SKU"]

        dokumen_perusahaan = ["Fotocopy akte pendirian & perubahannya", "Fotocopy pengesahan kehakiman", "Fotocopy SIUP", "Fotocopy NPWP", "Fotocopy SITU / Domisili, TDP", "Fotocopy Rek. Koran 3 bulan terakhir", "Fotocopy KTP direksi & komisaris"]

        dokumen_belum_lengkap = []

        if jenis_kredit == "1":
            print("\nPengajuan Kredit Perorangan")
            for dokumen in dokumen_perorangan:
                input_pembeli = input(f"Apakah sudah melengkapi {dokumen}? (sudah/belum): ").lower()
                if input_pembeli != "sudah":
                    dokumen_belum_lengkap.append(dokumen)
        elif jenis_kredit == "2":
            print("\nPengajuan Kredit Perusahaan")
            for dokumen in dokumen_perusahaan:
                input_pembeli = input(f"Apakah sudah melengkapi {dokumen}? (sudah/belum): ").lower()
                if input_pembeli != "sudah":
                    dokumen_belum_lengkap.append(dokumen)
        else:
            print("Jenis kredit tidak valid.")

        if not dokumen_belum_lengkap:
            print("Selamat, pengajuan kredit diterima!")
        else:
            print("Maaf, pengajuan kredit ditolak. Dokumen berikut belum lengkap:")
            for dokumen in dokumen_belum_lengkap:
                print(dokumen)
    
pembeli = Pembeli()

while True:
    print("\nSelamat datang di program pembelian mobil Toyota!\nPilih Menu:\n1. Pencarian tipe mobil\n2. Lihat semua mobil dan harga\n3. Lihat Syarat Pengajuan kredit\n4. Beli mobil (Lihat tipe mobil terlebih dahulu)\n5. Keluar dari program")
    
    pilihan = input("Silakan pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        tipe_mobil = input("\nMasukkan tipe mobil yang ingin dicari: ").lower()
        pembeli.cari_tipe_mobil(tipe_mobil)
    elif pilihan == "2":
        for tipe_mobil in mobil_info:
            pembeli.cari_tipe_mobil(tipe_mobil)
            print("")
    elif pilihan == "3":
        jenis_kredit = input("\nPilihan jenis kredit\n1. perorangan\n2. perusahaan\npilih jenis kredit (1/2): ")
        pembeli.syarat_kredit(jenis_kredit)
    elif pilihan == "4":
        tipe_mobil = input("\nMasukkan tipe mobil yang ingin dibeli: ").lower()
        pembeli.beli_mobil(tipe_mobil)
    elif pilihan == "5":
        print("Terima kasih, program telah selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

    input_tambahan = input("Ingin kembali ke menu awal? (ya/tidak): ")
    if input_tambahan.lower() != "ya":
        print("Terima kasih, program telah selesai.")
        break