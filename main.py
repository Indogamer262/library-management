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
    readyString = "\n"
    readyString += "||".join(processArr)

    # append the joined string to files
    with open(dbFile, "a") as files:
        files.write(readyString)
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
    for i in range(1, len(bookList)):
        if(categories == 1):
            print(bookList[i][0], "    ", bookList[i][1],
                    "\n", bookList[i][2],
                    "\n", bookList[i][3], " | Ketersediaan: ", bookList[i][5], "\n",
                    sep="")
        else:
            if(bookList[i][4] == cat[categories-1]):
                print(bookList[i][0], "    ", bookList[i][1],
                      "\n", bookList[i][2],
                      "\n", bookList[i][3], " | Ketersediaan: ", bookList[i][5], "\n",
                      sep="")
    
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
        return True
    elif(select == 3):
        return True
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
if __name__ == '__main__':
    run = True
    # Kode akan terus di eksekusi sampai keluar dari program
    while(run == True):
        run = main()