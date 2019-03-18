#NO 1
matA = [[2,6], [5,7]]
matB = [[5,7], [7,8]]
matC = [[7,4,2], [1,3,7], [4,6,2]]
matD = [[5,2], [3,7], [5,7]]
matE = [[3,2,5], [6,2,0]]
matF = [[1,4,"a"], [8,4]]

#A
def cekMatriks(m) :
    a = len(m[0])
    b = 0
    for i in range(len(m)) :
        if (len(m[i]) == a) :
            b += 1
    if (b == len(m)) :
        print ("Matriks Konsisten")
    else :
        print ("Matriks tidak Konsisten")
cekMatriks(matA)
cekMatriks(matC)
cekMatriks(matF)

def cekInt(m):
    x = 0
    y = 0
    for i in m:
        for j in i:
            y+=1
            if (str(j).isdigit()==False):
                print("Tidak semua isi matriks berupa Angka")
                break
            else:
                x+=1
    if(x==y):
        print("Semua isi matriks berupa Angka")

cekInt(matA)
cekInt(matB)
cekInt(matF)

#B
def ukMatriks(u) :
    x,y = 0,0
    for i in range(len(u)):
        x+=1
        y = len(u[i])
    print("mempunyai ordo "+str(x)+"x"+str(y))

ukMatriks(matA)
ukMatriks(matB)
ukMatriks(matD)

#C
def jumlahMatriks(a,b) :
    x,y = 0,0
    for i in range(len(a)):
        x+=1
        y = len(a[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(a)==len(b)):
        for i in range(len(a)):
            if(len(a[i]) == len(b[i])):
                z+=1
    if(z==len(a) and z==len(b)):
        print("Ukuran sama")
        for i in range(len(a)):
            for j in range(len(a[i])):
                xy[i][j] = a[i][j] + b[i][j]
        print(xy)
    else:
        print("ukuran beda")

jumlahMatriks(matA,matB)
jumlahMatriks(matA,matD)

#D
def kaliMatriks(a,b) :
    c = 0
    x,y = 0,0
    for i in range(len(a)):
        x+=1
        y = len(a[i])
    t,u = 0,0
    for i in range(len(b)):
        t += 1
        u = len(b[i])
        
    if(y == t):
        print("bisa dikalikan")
        tuxy = [[0 for j in range(u)] for i in range(x)]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    #print(a[i][k], b[k][j])
                    tuxy[i][j] += a[i][k] * b[k][j]
        print(tuxy)
            
    else:
        print("Tidak memenuhi syarat.")

d = [[1,2,3],[1,2,3]]
e = [[1],[2],[3]]
kaliMatriks(d,e)
kaliMatriks(matA,matB)
kaliMatriks(matA,matE)
kaliMatriks(matC,d)

#E
def determHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                Ay = A 
                Ay = Ay[1:] 
                height = len(Ay) 
                for i in range(height): 
                    Ay[i] = Ay[i][0:fc] + Ay[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determHitung(Ay)
                total += sign * A[0][fc] * sub_det
        else:
            return "Tidak bisa dihitung determinan, bukan matriks bujursangkar"
    else:
        return "Tidak bisa dihitung determinan, bukan matriks bujursangkar"
    return total


z = [[3,5],[1,4]]
x = [[1,2,5],[6,6,2],[0,3,4]]
v = [[4,-2,0,0],[5,3,-3,1],[1,0,6,3],[1,3,-6,4]]
r = [[10,3,-5,11,2],[1,2,4,0,1],[1,2,1,4,3],[5,2,1,4,0],[1,3,5,2,7]]
print(determHitung(z))
print(determHitung(x))
print(determHitung(v))
print(determHitung(r))
print(determHitung(matD))
print(determHitung(matE))

#2
#A
def buatNol(m ,n = None):
    if(n == None):
        n = m
    print("Membuat matriks 0 dengan ordo "+str(m)+"x"+str(n))
    print([[0 for j in range(n)] for i in range(m)])

buatNol(2,4)
buatNol(3)

#B
def buatIdentitas(q):
    print("Membuat matriks identitas dengan ordo" + str(q) + "x" + str(q))
    print([[1 if j == i else 0 for j in range(q)] for i in range(q)])

buatIdentitas(3)
buatIdentitas(2)

#3
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def cari(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
    def tambahDepan(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    def tambahAkhir(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def tambah(self, data, pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
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
    def hapus(self, posisi): 
        if self.head == None: 
            return 
        temp = self.head 
        if posisi == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(posisi -1 ): 
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next
        temp.next = None
        temp.next = next 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next   
    
Linklist = LinkedList() 
Linklist.tambahDepan(4)
Linklist.tambahDepan(26)
Linklist.tambahDepan(7)
Linklist.tambahDepan(18)
Linklist.tambahAkhir(2)
Linklist.tambahDepan(17)
Linklist.tambahAkhir(9)
Linklist.hapus(0)
Linklist.tambah(1,6)
print(Linklist.cari(4))
print(Linklist.cari(29))
Linklist.display()

#4
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.prev = None
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
    def awal(self, new_data):
        print("menambahkan suatu simpul di awal", new_data)
        new_node = Node(new_data) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node 
    def akhir(self, new_data):
        print("menambahkan suatu simpul di akhir", new_data)
        new_node = Node(new_data) 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        last = self.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 
        return
    def printList(self, node): 
        print("\nDari Depan :")
        while(node is not None): 
            print(" % d" %(node.data))
            last = node 
            node = node.next
        print("\nDari Belakang :")
        while(last is not None): 
            print(" % d" %(last.data)) 
            last = last.prev 
Dlist = DoublyLinkedList() 
Dlist.awal(7)  
Dlist.awal(4)
Dlist.akhir(2)
Dlist.akhir(6) 
Dlist.printList(Dlist.head)













