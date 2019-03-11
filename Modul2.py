
# NO 1
class Pesan(object) :
    """ Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self) :
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self) :
        return len(self.teks)
    def cetakJumlahKarakterku(self) :
        print("Kalimatku mempunyai", len(self.teks),"karakter.")
    def perbarui(self, stringBaru) :
        self.teks = stringBaru
        
# NO 1 a
    def apakahTerkandung(self, a) :
        if a in self.teks :
            return True
        else :
            return False
        
# Kode Eksekusi
## p9 = Pesan("Indonesia adalah negeri yang indah")
## p9.apakahTerkandung("ege")
## p9.apakahTerkandung("eka")

# NO 1 b
    def hitungKonsonan(self) :
        vok = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
        jum = 0
        for i in self.teks :
            if i in vok :
                jum += 1
        return jum

# Kode Eksekusi
## p10 = Pesan("Surakarta")
## p10.hitungKonsonan()

# NO 1 c
    def hitungVokal(self) :
        vok = "AIUEOaiueo"
        jumlah = 0
        for i in self.teks:
            if i in vok :
                jumlah += 1
        return jumlah

# Kode Eksekusi
## p10.hitungVokal()

# NO 2

class Manusia(object) :
    """Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self) :
        print("Salaam, namaku", self.nama)
    def makan(self, s) :
        print("Saya baru saja makan", s)
        self.keadaan = "kenyang"
    def olahraga(self, k) :
        print("Saya baru saja latihan", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self, n) :
        return n*2

class Mahasiswa(object):
    """ Class Mahsiswa yang dibangun dari class Manusia"""
    def __init__(self, nama, NIM, kota, us) :
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(Self):
        s = self.nama + ", NIM " + str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uang saku Rp "  + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s) :
        """ Metode ini menutupi metode 'makan'-nya class Manusia.
            Mahasiswa kalau makan sambil belajar."""
        print ("Saya baru saja makan", s , "sambil belajar. ")
        self.keadaan = "kenyang"
    

# NO 2 a

    def ambilKotaTinggal(self) :
        print(self.kotaTinggal)

# NO 2 b
    def perbaruiKotaTinggal(self) :
        self.kotaTinggal = baru

# NO 2 c
    def tambahUangSaku(self) :
        self.uangsaku = self.uangsaku + uang


# NO 3

## a = input("Masukkan Nama : ")
## b = input("Masukan NIM : ")
## c = input("Masukkan Kota Tinggal : ")
## d = input("Masukkan Uang saku : ")

# Kode Eksekusi
## m1 = Mahasiswa(a,b,c,d)
## m1.ambilNama()
## m1.ambilNIM()
## m1.ambilKotaTinggal()
## m1.ambilUangSaku()

# NO 4

    listKuliah = []
    def ambilKuliah(self, kuliah) :
        self.listKuliah.append(kuliah)

# NO 5

    def hapusMakul(self, item) :
        self.listKuliah.remove(item)

# NO 6

class SiswaSMA(Manusia) :
    """ Class SiswaSMA yang dibangun dari class Manusia """
    def __init__(self, nama , no_induk , kelas , alamat):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.no = no_induk
        self.kelas = kelas
        self.alamat = alamat
    def __str__(self):
        x = "Nama : " + self.nama + '\n'
        + "No Induk : " + str(self.no) + '\n'
        + "Tinggal di : " + self.alamat + '\n'
        + "Kelas : " + str(self.kelas)
        print (x)
    def ambilNama(self):
        print (self.nama)
    def ambilNoInduk(self):
        print (self.no)
    def ambilKelas(self):
        print (self.kelas)
    def ambilAlamat(self):
        print (self.alamat)

# NO 7

class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpy(self):
        print('Python is cool.')

##Dari class Manusia:
##    1. nama
##    2. keadaan
##    3. ucapkanSalam
##    4. makan
##    5. olahraga
##    6. mengalikanDenganDua
##
##Dari class Mahasiswa:
##    1. NIM
##    2. kotaTinggal
##    3. uangsaku
##    4. ambilNama
##    5. ambilNIM
##    6. ambilUangSaku
##    7. makan
##    8. ambilKotaTinggal
##    9. perbaruiKotaTinggal
##    10. tambahUangSaku
##    11. listKuliah
##    12. ambilKuliah
##    13. hapusKuliah
##
##Dari class MhsTIF:
##    1. katakanpy
    
#Kode Eksekusi   
m9 = Mahasiswa("Astrin","L200170013","Solo",70000)
s1 = SiswaSMA("Astrin",l70013,7,"Surakarta")

## m9.ambilKotaTinggal()
## m9.perbaruiKotaTinggal('Bandung')
## m9.ambilKotaTinggal()
## m9.ambilUangSaku()
## m9.tambahUangSaku(45000)
## m9.ambilUangSaku()


