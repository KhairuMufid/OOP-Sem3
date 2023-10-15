# Nama  : Muhammad Khairu Mufid
# NIM   : 2207421031
# Kelas : TMJ-3B

class Mobil:
    def __init__(self, kategori, tipe, model, harga, premium_color = None , two_tone_color = None):
        self.kategori = kategori
        self.tipe = tipe
        self.model = model
        self.harga = harga 
        self.premium_color = premium_color
        self.two_tone_color = two_tone_color

# Instance Objek Mobil dan memasukkannya ke dalam list sebagai value dari key tipe mobil di dalam dictionary
semua_mobil = {
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
        Mobil("MPV", "All New Velloz", "1.5 MT", "Rp 286.000.000", premium_color="Rp 1.500.000"),
        Mobil("MPV", "All New Velloz", "1.5 Q CVT", "Rp 309.100.000", premium_color="Rp 1.500.000"),
        Mobil("MPV", "All New Velloz", "1.5 Q CVT TSS", "Rp 331.100.000", premium_color="Rp 1.500.000")
    ],
    "alphard": [
        Mobil("MPV", "All New Alphard", "2.5 G AT", "Rp 1.344.800.000", premium_color="Rp 3.100.000"),
    ],
    "velfire": [
        Mobil("MPV", "All New Velfire", "2.5 Velfire", "Rp 1.359.600.000", premium_color="Rp 3.100.000")
    ],
    "innova zenix": [
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 G CVT", "Rp 419.000.000", premium_color="Rp 3.000.000"),
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 V CVT", "Rp 467.000.000", premium_color="Rp 3.000.000"),
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 G HV CVT", "Rp 458.000.000", premium_color="Rp 3.000.000"),
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 V HV CVT", "Rp 532.000.000", premium_color="Rp 3.000.000"),
        Mobil("MPV", "All New Innova Zenix","Zenix 2.0 Q HV CVT", "Rp 611.000.000", premium_color="Rp 3.000.000")
    ],
    "rush": [
        Mobil("SUV", "All New Rush", "G MT", "Rp 278.800.000"),
        Mobil("SUV", "All New Rush", "G AT", "Rp 289.600.000"),
        Mobil("SUV", "All New Rush", "GR MT", "Rp 291.500.000"),
        Mobil("SUV", "All New Rush", "GR AT", "Rp 302.200.000")
    ],
    "raize": [
        Mobil("SUV", "All New Raize", "G MT", "Rp 232.400.000", two_tone_color="Rp 2.700.000"),
        Mobil("SUV", "All New Raize", "G CVT", "Rp 247.300.000", two_tone_color="Rp 2.700.000"),
        Mobil("SUV", "All New Raize", "G MT", "Rp 251.900.000", two_tone_color="Rp 2.700.000"),
        Mobil("SUV", "All New Raize", "G CVT", "Rp 266.900.000", two_tone_color="Rp 2.700.000"),
        Mobil("SUV", "All New Raize", "GR CVT", "Rp 280.800.000", two_tone_color="Rp 2.700.000"),
        Mobil("SUV", "All New Raize", "GR CVT TSS", "Rp 302.500.000", two_tone_color="Rp 2.700.000")
    ],
    "fortuner": [
        Mobil("SUV", "All New Fortuner", "VRZ (4x2)", "Rp 606.200.000"),
        Mobil("SUV", "All New Fortuner", "VRZ GR (4x2)", "Rp 624.950.000"),
        Mobil("SUV", "All New Fortuner", "VRZ GR (4x4)", "Rp 715.350.000")
    ],
    "corolla cross": [
        Mobil("SUV", "All New Corolla Cross", "Hybrid AT", "Rp 540.900.000", premium_color="Rp 3.800.000")
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
        Mobil("Sedan", "All New Corolla Altis", "Hybrid AT", "Rp 514.200.000" , premium_color="Rp 3.000.000")
    ],
    "camry": [
        Mobil("Sedan", "All New Corolla Camry", "2.5 V AT", "Rp 741.700.000", premium_color="Rp 3.000.000"),
        Mobil("Sedan", "All New Corolla Camry", "1.5 L AT", "Rp 874.600.000", premium_color="Rp 3.000.000")
    ],
    "vios": [
        Mobil("Sedan", "All New Vios", "1.5 E MT", "Rp 314.900.000", premium_color="Rp 1.500.000"),
        Mobil("Sedan", "All New Vios", "1.5 G CVT", "Rp 355.200.000", premium_color="Rp 1.500.000"),
        Mobil("Sedan", "All New Vios", "1.5 G CVT TSS", "Rp 368.400.000", premium_color="Rp 1.500.000")
    ],
    "gr 86": [
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
    ]
}
