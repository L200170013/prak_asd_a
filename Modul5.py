##Nama    : Astrin Indah Meliana
##Kelas   : A
##Nim     : L200170013
##Modul   : 5

class Mahasiswa(object):
    """Class Manusia yang dibangun dari class manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')
        
Daftar = [MhsTIF ('Ika',10,'Sukoharjo', 240000),
MhsTIF('Budi',51,'Sragen', 230000),
MhsTIF('Ahmad',2,'Surakarta', 250000),
MhsTIF('Chandra',18,'Surakarta', 230000),
MhsTIF('Eka',4,'Boyolali', 240000),
MhsTIF('Fandi',31,'Salatiga', 250000),
MhsTIF('Deni',13,'Klaten', 245000),
MhsTIF('Galuh',5,'Wonogiri', 245000),
MhsTIF('Janto',23,'Klaten', 245000),
MhsTIF('Hasan',64,'Karanganyar', 270000),
MhsTIF('Khalid',29,'Purwodadi', 265000)]

#No 1
def cekNim (x):
    for i in x :
        print (i.NIM)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urutkanNim(x):
    n = len(x)
    for i in range (n -1) :
        for j in range (n-i-1) :
            if x[j].NIM > x[j+1].NIM :
                swap(x,j,j+1)
##cara pemanggilan
##urutkanNim(Daftar)
##cekNim(Daftar)

#No 2
A = [1,3,5,7,8,0]
B = [2,4,6,9,10]
C = A + B
 
def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urutkan(d):
    n = len (d)
    for i in range (n -1) :
        for j in range (n-i-1) :
            if d[j] > d[j+1] :
                swap(d,j,j+1)

urutkan(C)
print(C)

#No 3
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai
        
def cariPosisiYangTerkecil(A,darisini, sampaisini):
    posisiYangTerkecil = darisini
    for i in range (darisini+1, sampaisini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_buble = k[:]
u_selection = k[:]
u_insertion = k[:]

awal = detak() ; bubbleSort(u_buble) ;
akhir = detak() ; print('bubble: %g detik' %(akhir - awal)) ;
awal = detak() ; selectionSort(u_selection) ;
akhir =detak() ; print('selection: %g detik' %(akhir - awal)) ;
awal = detak() ; insertionSort(u_insertion) ;
akhir = detak() ; print('insertion: %g detik' %(akhir - awal)) ;
                                          






