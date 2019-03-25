#Nama  : Astrin Indah Melliana
#Nim   : L200170013
#Kelas : A


class MhsTIF(object) :
    """ Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,um,kota,us) :
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.umur = um
        self.kotaTinggal = kota
        self.uangSaku = us

class Array(object) :
    internal_data = 11 * [None]

    def __getitem__(self, item) :
        return self.internal_data[item]
    def __setitem__(self, key, value) :
        self.internal_data[key] = value
#NO 1
    def indexKota(self, data) :
        d = []
        t = 0
        for i in self :
            if i.kotaTinggal == data :
                d.append(t)
            t += 1
        return d
#NO 2
    def uangTerkecil(self) :
        terkecil = self[0].uangSaku
        for i in self :
            if i.uangSaku < terkecil :
                terkecil = i.uangSaku
        return terkecil
#NO 3
    def uangTerkecil3(self) :
        terkecil = self[0].uangSaku
        d = []
        for i in self :
            if i.uangSaku < terkecil :
                d.append((i.nama, i.umur, i.kotaTinggal, i.uangSaku))
        return d
    
#NO 4
    def uangTerkecil4(self) :
        terkecil = 250000
        d = []
        for i in self :
            if i.uangSaku < 250000 :
                d.append((i.nama, i.umur, i.kotaTinggal, i.uangSaku))
        for i in d :
            print (i)
            
c = Array()
c[0] = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c[1] = MhsTIF("Budi", 51, "Sragen", 230000)
c[2] = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c[3] = MhsTIF("Chandra", 18, "Surakarta", 235000)
c[4] = MhsTIF("Eka", 4, "Boyolali", 240000)
c[5] = MhsTIF("Fandi", 31, "Salatiga", 250000)
c[6] = MhsTIF("Deni", 13, "Klaten", 245000)
c[7] = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c[8] = MhsTIF("Janto", 23, "Klaten", 245000)
c[9] = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c[10] = MhsTIF("Khalid", 29, "Purwodadi", 240000)


#cara memanggil no 1
c.indexKota("Klaten")
#cara memanggil no 2
c.uangTerkecil()
#cara memanggil no 3
c.uangTerkecil3()
#cara memanggil no 4
# c.uangTerkecil4()

#NO 5
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def pushAw(self, data_baru):
        node_baru = Node(data_baru)
        node_baru.next = self.head
        self.head = node_baru
    def pushAk(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self, data, pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif posisi == 0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
               prev = current
               current = current.next
               current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def search(self, v):
        current = self.head
        while current != None:
            if current.data == v:
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

#NO 6
def binSe(Daftar, Target) :
    low = 0
    high = len(Daftar) - 1

    while low <= high :
        mid = (high + low) // 2
        if Daftar [mid] == Target :
            return "Target berada pada index" + str(mid)
            break
        elif Target < Daftar [mid] :
            high = mid - 1
        else :
            low = mid + 1
    return False

listA = [12, 25, 34, 36, 57, 85, 90, 91]
Target1 = 29
Target2 = 57
print("\n6. List nya adalah", listA, "Nilai Target adalah ", Target1, "Hasil nya" , binSe(listA, Target1))
print("List nya adalah", listA, "Nilai Target adalah ", Target2, "Hasil nya" , binSe(listA, Target2))

#NO 7
def binSe1(Daftar, Target) :
    loww = 0
    highh = len(Daftar) - 1
    listx = []

    while loww <= highh :
        if Daftar[loww] == Target :
            listx.append(loww)
            loww += 1
        else :
            loww += 1
    return listx

A = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
cari = 6

print ("\n7. Posisi data", cari, "pada list", A, "adalah", binSe1(A, cari)) 

#NO 8
def binSearching(kumpulan, target):
    #Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) -1

    #Secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low <= high:
        #Temukan pertengahan runtut itu
        mid = (high + low) //2
        #Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            return mid
        elif kumpulan[mid] < target:
            high = mid +1
        else :
            low = mid -1
            
    return -1

b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

"""
untuk mencari berapa jumlah tebakan yang digunakan oleh Binary Search
yaitu dengan menggunakan Logaritma basis 2 (log2(n))
misalkan :
        // apabila terdapat elemen array berjumlah 100 maka memiliki maksimal 7 kali tebakan
           itu dikarenakan log2(100) = 6.643856189774725 sehingga diperoleh angka 7
           dapat juga diperoleh dari log2(128) = 7 karena yang mendekati dari 100 adalah 128

       //  apabila terdapat elemen array berjumlah 1000 maka memiliki maksimal 10 kali tebakan
           itu dikarenakan log2(1000) = 9.965784284662087 sehingga diperoleh angka 10
           dapat juga diperoleh dari log2(1024) = 10 karena yang mendekati dari 1000 adalah 128
""" 




