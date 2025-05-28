# File: main.py
# Penulis: 2472008 - 2472018 - 2472048
# --- Kamus Global ---
# run: variabel untuk menyimpan status berjalan program

## Definisi fungsi deklarasi Matriks
# --- Kamus Lokal ---
#
def deklarasiMatriks(row,cols):
    mat = [None]*row
    for i in range(0, row):
        mat[i]=[None]*cols
    return mat

## Definisi fungsi baca data
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

## Definisi fungsi tulis data
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

## Definisi fungsi eeeee
# --- Kamus Lokal ---
#
def bookList():
    # should we make all categories?
    Categories=["Pendidikan", "Biografi", "Komik", "Novel"]
    print(
        "Pilih kategori",
        "1. Pendidikan",
        "2. Biografi",
        "3. Komik",
        "4. Novel",
        "0. Kembali ke Menu",
    sep="\n")
    select = int(input("> "))
    if select == 0:
        main()
    else:
        readDB("data_buku.txt")
       

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
        bookList()
    return True

if __name__ == '__main__':
    run = True
    # Kode akan terus di eksekusi sampai keluar dari program
    while(run == True):
        run = main()