# File: main.py
# Penulis: 2472008 - 2472018 - 2472048
# --- Kamus Global ---
# run: variabel untuk menyimpan status berjalan program

## Definisi fungsi deklarasi Matriks
# --- Kamus Lokal ---
#
#
def deklarasiMatriks(row,cols):
    mat = [None]*row
    for i in range(0, row):
        mat[i]=[None]*cols
    return mat

## Definisi fungsi readDB (baca data)
# --- Kamus Lokal ---
# dbFile: Variabel parameter menyimpan filename (string)
# files: Variabel menyimpan objek file (object)
# read: Variabel menyimpan string hasil read (string)
# readArr: List 2 dimensi untuk menyimpan hasil pembacaan (List string)
def readDB(dbFile):
    with open(dbFile, "rt") as files:
        read = files.read()
        readArr = read.split("\n")
        for i in range(0, len(readArr)):
            readArr[i] = readArr[i].split("||")
    return readArr

## Definisi fungsi writeDB (tulis data)
# --- Kamus Data ---
# array: Variabel parameter menyimpan array yang akan dikonversi (string)
# dbFile: variabel parameter menyimpane filename (string)
# files: variabel menyimpan objek file (object)
# processArr: list tempat data diubah menjadi string (List string)
# readyString: variabel menyimpan string yang akan ditulis ke file (string)
def writeDB(array, dbFile):
    processArr = array
    for i in range(0, len(array)):
        processArr[i] = "||".join(processArr[i])
    readyString = "\n".join(processArr)
    
    # write readyString to files
    with open(dbFile, "w") as files:
        files.write(readyString)
    return

## Definisi fungsi append data
# --- Kamus Data ---
# array: Variabel parameter menyimpan array yang akan dikonversi (string)
# dbFile: variabel parameter menyimpane filename (string)
# files: variabel menyimpan objek file (object)
# processArr: list tempat data diubah menjadi string (List string)
# readyString: variabel menyimpan string yang akan ditulis ke file (string)
def appendDB(array, dbFile):
    processArr = array

    # convert all datatype to str
    for i in range(0, len(processArr)):
        processArr[i] = str(processArr[i])

    readyString = "\n"
    readyString += "||".join(processArr)

    # append the joined string to files
    with open(dbFile, "a") as files:
        files.write(readyString)
    return

## Definisi fungsi removeDB
# --- Kamus Data ---
# lines: variabel parameter untuk menentukan baris yang ingin dihapus (integer)
# dbFile: variabel parameter untuk menentukan file database yang akan diubah (string)
# objectData: list untuk menyimpan sementara isi database (list string)
# readyList: list untuk menyimpan list yang sudah dimodifikasi (list string)
def removeDB(lines, dbFile):
    objectData = readDB(dbFile)
    readyList = [None]*(len(objectData)-1)
    
    k=0
    for i in range(0, len(objectData)):
        if (i != lines):
            readyList[k] = objectData[i]
            k += 1
    writeDB(readyList, dbFile)

    return

## Definisi fungsi bookList
# --- Kamus Lokal ---
# select: variabel untuk menyimpan pilihan pengguna (integer)
def kategori():
    print(
        "Pilih kategori",
        "1. All categories",
        "2. Pendidikan",
        "3. Biografi",
        "4. Komik",
        "5. Novel",
        "0. Kembali ke Menu",
    sep="\n")
    select = int(input("> "))
    if (select == 0):
        return
    else:
        showCategories(select)
        return

## Definisi fungsi displayBookList
# --- Kamus Lokal ---
# categories: variabel untuk menyimpan kategori pilihan (integer)
# bookList: matriks daftar buku untuk ditampilkan (matriks string)
def displayBookList(categories, bookList):
    catList = ["All categories","Pendidikan", "Biografi", "Komik", "Novel"]
    for i in range(1, len(bookList)):
        if(categories == 1):
            printDetails(i, bookList)
        else:
            if(bookList[i][4] == catList[categories-1]):
                printDetails(i, bookList)
    return

## Definisi fungsi printDetails
# --- Kamus Lokal ---
# bookList: matriks daftar buku untuk ditampilkan (matriks string)
def printDetails(lines, bookList):
    print(bookList[lines][0], "    ", bookList[lines][1],
            "\n", bookList[lines][2],
            "\n", bookList[lines][3], " | Ketersediaan: ", bookList[lines][5], "\n",
            sep="")

## Definisi fungsi showCategories
# --- Kamus Lokal ---
# categories: variabel parameter untuk menyimpan kategori pilihan (integer)
# cat: array menyimpan kategori yang tersedia (array string)
# bookList: matriks menyimpan data buku dari database (matriks string)
# select: variabel untuk menyimpan pilihan pengguna (integer)
def showCategories(categories):
    cat=["All categories","Pendidikan", "Biografi", "Komik", "Novel"]
    bookList = readDB('db/data_buku.txt')
    
    print("Kategori:",cat[categories-1],"\n")
    displayBookList(categories, bookList)
    
    lagi = "Y"
    print("Ketik \"EXIT\" jika ingin membatalkan")
    
    # catat daftar buku yang terseida
    daftarKode = [None]*len(bookList)
    for i in range(1, len(bookList)):
        if(int(bookList[i][5]) > 0): # hanya mendaftarkan buku yang stoknya lebih dari 0
            daftarKode[i] = bookList[i][0]
    daftarPinjam = [None]*100
    i = 0
    # menanyakan user apa yang mau dipinjam
    while (lagi == "Y" and i<100):
        select = str(input("> Pilih kode buku yang ingin dipinjam: "))
        if(select == "EXIT"):
            return
        else:
            # mencatat pinjaman
            if((select in daftarKode) and (select not in daftarPinjam)):
                daftarPinjam[i] = select
                i += 1
            else:
                print("Kesalahan Input Buku tidak tersedia!")
            lagi = str(input("Ada lagi (Y/n)? "))
    # meneruskan ke layar konfirmasi peminjaman        
    peminjaman(daftarPinjam, i)
    return

## Definisi fungsi peminjaman
# --- Kamus Lokal ---
# 
def peminjaman(daftarPinjam, jumlah):
    judulBuku = readDB('db/data_buku.txt')
    print("Anda akan meminjam:")
    for i in range(0, jumlah):
        for j in range(1, len(judulBuku)):
            if(daftarPinjam[i] == judulBuku[j][0]):
                print(judulBuku[j][0],"\t",judulBuku[j][1])
    
    dataMember = readDB('db/data_member.txt')
    idMember = int(input("Masukkan ID Member: "))
    passwordMember = str(input("Masukkan Password Member: "))
    for i in range(1, len(dataMember)):
        if(idMember == int(dataMember[i][1])):
            if(passwordMember == dataMember[i][3]):
                # append to DB
                for j in range(0, jumlah):
                    dataArray = [str(idMember), str(date.today()), daftarPinjam[j]]
                    appendDB(dataArray, 'db/data_peminjam.txt')

                # kurangi stok
                for k in range(0, jumlah):
                    for j in range(1, len(judulBuku)):
                        if(daftarPinjam[k] == judulBuku[j][0]):
                            stokNow = int(judulBuku[j][5])-1
                            judulBuku[j][5] = str(stokNow)
                writeDB(judulBuku, 'db/data_buku.txt')

                print("Berhasil! Terima Kasih", dataMember[i][2] ,"telah Meminjam!")
            else:
                print("Password salah.")
    return

## Definisi fungsi pengembalian
# --- Kamus Data ---
def pengembalian():
    # minta login
    idMember = int(input("Masukkan ID Member: "))
    passwordMember = str(input("Masukkan Password Member: "))

    # readDB member
    # cek id dan password
    dataMember = readDB('db/data_member.txt')
    for i in range(1, len(dataMember)):
        if(idMember == int(dataMember[i][1])):
            if(passwordMember == dataMember[i][3]):
                print("Login berhasil!")
            else:
                idMember = 0
                print("Login gagal! silahkan coba lagi!")

    # readDB peminjaman
    # readDB buku
    # pilih buku yang akan dikembalikan
    dataPeminjam = readDB('db/data_peminjam.txt')
    dataBuku = readDB('db/data_buku.txt')
    if(idMember != 0):
        print("Pilih buku yang akan dikembalikan:")
        
        # tampilkan detail buku yang dipinjam
        for i in range(0,len(dataPeminjam)):
            if(dataPeminjam[i][0] == str(idMember)):
                print(dataPeminjam[i][2], end="    ")

                # tampilkan judul buku
                for j in range(0,len(dataBuku)):
                    if(dataPeminjam[i][2] == dataBuku[j][0]):
                        print(dataBuku[j][1])
                # tampilkan batas waktu
                print("Batas waktu:", end=" ")
                deadline = (datetime.strptime(dataPeminjam[i][1], "%Y-%m-%d")+timedelta(days=7)).date()
                print(deadline, end="    ")

                # tampilkan nilai denda
                if(date.today() > deadline):
                    denda = (date.today()-deadline).days*500
                    print("(Lebih batas waktu! denda: ",denda,")",sep="")
                    
                print("\n")

        # pilih buku yang akan dikembalikan
        daftarKode = [None]*len(dataPeminjam)
        for i in range(1, len(dataPeminjam)):
            if(dataPeminjam[i][0] == str(idMember)):
                daftarKode[i] = dataPeminjam[i][2]

        select = str(input("> ID Buku: "))

        # tambah stok
        if(select in daftarKode):
            for i in range (0, len(dataBuku)):
                if(dataBuku[i][0] == select):
                    dataBuku[i][5]= str(int(dataBuku[i][5]) + 1)
        writeDB(dataBuku, 'db/data_buku.txt')

        # hapus data peminjam
        for i in range(0, len(dataPeminjam)):
            if(select == dataPeminjam[i][2] and str(idMember) == dataPeminjam[i][0]):
                removeDB(i, 'db/data_peminjam.txt')
                print("Buku berhasil dikembalikan!\n")
                return
    return

## Definisi fungsi pendaftaran
# --- Kamus Data ---
# exist: 
# kevin-krm: variabel untuk menyimpan kevin (object)
def pendaftaran():
    print ("---Form Pendaftaran---")
    # Input Data Pengguna
    NIK = int(input("Masukkan NIK: "))
    ID = int(input("Masukkan NRP: "))
    Nama = str(input("Masukkan Nama Lengkap: "))
    Password = str(input("Buat Password: "))
    cPassword = str(input("Konfirmasi Password: "))
    
    # periksa keberadaan NIK
    dataMember = readDB('db/data_member.txt')
    for i in range(0, len(dataMember)):
        if(dataMember[i][0] == str(NIK) or dataMember[i][1]):
            print("\nNIK atau NRP sudah ada\n")
            return

    # Konfirmasi Pendaftaran Member
    if(Password == cPassword):
        konfirm = str(input("Buat Akun? (Y/n): "))
        print()
        if (konfirm == "Y"):
            appendDB([NIK,ID,Nama,Password], 'db/data_member.txt')
            print("Pendaftaran Berhasil")
            print("ID Member:",ID)
            print("Nama:",Nama)
            print()
        else:
            print("Pendaftaran Dibatalkan")
            print()
    else:
        print("Password dan Konfirmasi Password tidak sama")
    return

## Definisi fungsi admin
# --- Kamus Lokal ---
# password: variabel untuk menyimpan password yang akan dicek (string)
def admin():
    print("Untuk masuk ke dalam mode admin, silahkan login terlebih dahulu")
    password = str(input("> Password: "))

    if(password == "admin123"):
        print("Autentikasi berhasil!")
        print()
        adminAccess()
    else:
        print("Autentikasi gagal!")

    return

## Definisi fungsi adminAccess
# --- Kamus Lokal ---
# select: variabel untuk menyimpan pilihan aksi (integer)
def adminAccess():
    print("Saat ini anda sedang dalam mode Admin")
    print("Pilih aksi:",
          "1. Edit detail buku",
          "2. Tambah katalog buku",
          "3. Hapus katalog buku",
          "4. Periksa anggota",
          "0. Keluar dari Admin",
          sep="\n")

    select = int(input("> aksi: "))    
    print()
    if(select == 1):
        adminEdit()
    elif(select == 2):
        adminAddCatalog()
    elif(select == 3):
        adminDeleteCatalog()
    elif(select == 4):
        adminCheckMember()
    return

## definisi fungsi adminEdit
# --- Kamus Lokal ---
# bookList: matriks menyimpan data buku (matriks string)
# select: variabel untuk menyimpan pilihan aksi (integer)
# editID: variabel untuk menyimpan hasil pencarian (integer)
def adminEdit():
    bookList = readDB('db/data_buku.txt')
    
    displayBookList(1, bookList)
    select = str(input("> Pilih kode buku untuk di sunting: "))
    print()
    
    # tampilkan status buku saat ini
    print("Saat ini anda sedang menyunting:")
    editID = -1
    for i in range(0, len(bookList)):
        if(bookList[i][0] == select):
            editID = i
    if(editID != -1):
        print("Kategori:", bookList[editID][4])
        printDetails(editID, bookList)

        print("Menyunting, biarkan kosong jika tidak ingin mengubah!")
        judul = str(input("> Judul baru: "))
        deskripsi = str(input("> Deskripsi baru: "))
        penulis = str(input("> Kategori baru: "))
        kategori = str(input("> Kategori baru: "))
        stok = str(input("> Stok baru: "))

        # apply changes
        changes = False
        if(judul != ""):
            bookList[editID][1] = judul
            print("Judul diubah!")
            changes = True
        if(deskripsi != ""):
            bookList[editID][2] = deskripsi
            print("Deksripsi diubah!")
            changes = True
        if(penulis != ""):
            bookList[editID][3] = penulis
            print("Penulis diubah!")
            changes = True
        if(kategori != ""):
            bookList[editID][4] = kategori
            print("Kategori diubah!")
            changes = True
        if(stok != ""):
            bookList[editID][5] = stok
            print("Stok diubah!")
            changes = True

        if(changes):
            writeDB(bookList, 'db/data_buku.txt')
            print("Data yang diubah telah disimpan!")
        else:
            print("Tidak ada perubahan!")

    else:
        print("Kesalahan! Buku tidak ditemukan!")

    print()
    return

## definisi fungsi adminEdit
# --- Kamus Lokal ---
def adminAddCatalog():
    return

## definisi fungsi adminEdit
# --- Kamus Lokal ---
def adminDeleteCatalog():
    return

## definisi fungsi adminEdit
# --- Kamus Lokal ---
def adminCheckMember():
    return

## Program utama 
# --- Kamus Lokal ---
# select: variabel untuk select (integer)
def main():
    print("Selamat datang di Kevin Library, pilih menu:",
          "1. Lihat Daftar buku",
          "2. Kembalikan Buku",
          "3. Pendaftaran Member",
          "0. Keluar dari Program",
    sep="\n")
    select = int(input("> "))
    if (select == 1):
        kategori()
    elif(select == 2):
        pengembalian()
    elif(select == 3):
        pendaftaran()
    elif(select == 99):
        admin()
    elif(select == 0):
        return False
    
    ## Perintah Debug
    #debugArr = readDB('db/data_member.txt')
    #for i in range(1, len(debugArr)):
    #    for j in range(0, len(debugArr[0])):
    #        print(debugArr[i][j], end="    ")
    #    print()
    return True

from datetime import date
from datetime import timedelta
from datetime import datetime
if __name__ == '__main__':
    run = True
    # Kode akan terus di eksekusi sampai keluar dari program
    while(run == True):
        run = main()