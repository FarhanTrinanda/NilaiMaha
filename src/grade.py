from tabulate import tabulate

HEADERS = ('NIM', 'Nama', 'Jurusan', 'Pengantar Organisasi', 'Pengembangan Organisasi', 'Budaya Organisasi')



#Fungsi Menampilkan
def menampilkan(table, headers=HEADERS, title='\nTabel Daftar Nilai\n'):

    print(title)
    print(tabulate(table, headers, tablefmt="grid", showindex=False))



#Fungsi Read

#Pilihan Sub Menu Dalam Fungsi Read    
pilihan = f'''

========================= Pilih Data Yang Akan Ditampilkan: ======================= 

                            1. Tampilkan Seluruh Data
                            2. Tampilkan Data Mahasiswa
                            3. Kembali Ke Menu Utama

===================================================================================
            
'''
    
def read_data(table):

    while True:
        print(pilihan)
        menu_pilihan = input('Masukan Menu Yang Dipilih: ')
        #Untuk Menampilkan Semua Data/Table.
        if menu_pilihan == '1':
            print(menampilkan(table))
            continue
        #Untuk Menampilkan Satu Mahasiswa.
        elif menu_pilihan == '2':

            while True:
                Nim = input('Masukan Nim: ')
                if str.isalnum(Nim):
                    break
                else:
                    print('Masukan Huruf Dan Angka')

            i = 0
            for item in table:
                if Nim.capitalize() == item[0]:
                    Mahasiswa = [item[0], item[1], item[2],item[3], item[4], item[5]]
                    print(Mahasiswa)
                    i += 1
     
            if i == 0:
                print('Mahasiswa Tidak Ada! ')
        #Kembali Ke Main Menu.
        elif menu_pilihan == '3':
            return
        else:
            print('Masukan Pilihan Yang Sesuai! ')



#Fungsi Menambah

#Teks Pilihan Untuk Konfirmasi Mau Menambahkan Data Lagi Atau Tidak.           
Pilihan_tambah = f'''

Apakah Mau Menambahkan Data Lagi? (Y/N)

'''
#Pilihan Sub Menu Dalam Fungsi Menambah/Add.
Sub_menu_tambah = f'''

=================================== Pilih Menu: ===================================

                                    1. Update table
                                    2. Menu utama

===================================================================================
'''

def menambah(table):
    
    FLAG = True
    while FLAG:

        while True:

            print(Sub_menu_tambah)
            menu_pilihan = input('Masukan Menu Yang Dipilih: ')
            #Untuk Menambah Daftar Nilai Mahasiswa/Table.
            if menu_pilihan =='1':
                print(menampilkan(table))
    
                while True:
                    Nim = input('Masukan Nim: ')
                    if str.isalnum(Nim):
                        break
                    else:
                        print('Masukan Huruf Dan Angka! ')
                    break
                
                while True:
                    while True:
                        Nama = input('Masukan Nama: ')
                        if (any(x.isalpha() for x in Nama)
                                and all(x.isalpha or x.isspace for x in Nama)):
                            break
                        else:
                            print('Hanya Masukan Huruf! ')
                        continue
                    break

                while True:
                    while True:
                        Jurusan = input('Masukan Jurusan: ')
                        if str.isalpha(Jurusan):
                            break
                        else:
                            print('Hanya Masukan Huruf! ')
                        continue
                    break

                while True:
                    while True:
                        Nilai = input('Masukan Nilai Pengantar Organisasi:')
                        if str.isnumeric(Nilai):
                            break
                        else:
                            print('Masukan Hanya Angka! (0 - 100) ')
                        continue
                    break
                    
                while True:
                    if 90 <= int(Nilai) <= 100:
                        Nilai_Pengantar = 'A'
                        break
                    if 80 <= int(Nilai) <= 89:
                        Nilai_Pengantar = 'B'
                        break
                    if 70 <= int(Nilai) <= 79:
                        Nilai_Pengantar = 'C'
                        break
                    if 60 <= int(Nilai) <= 69:
                        Nilai_Pengantar = 'D'
                        break
                    else:
                        Nilai_Pengantar = 'E'
                        break

                while True:
                    while True:
                        Nilai = input('Masukan Nilai Pengembangan Organisasi:')
                        if str.isnumeric(Nilai):
                            break
                        else:
                            print('Masukan Hanya Angka! (0 - 100) ')
                        continue
                    break
                    
                while True:
                    if 90 <= int(Nilai) <= 100:
                        Nilai_Pengembangan = 'A'
                        break
                    if 80 <= int(Nilai) <= 89:
                        Nilai_Pengembangan = 'B'
                        break
                    if 70 <= int(Nilai) <= 79:
                        Nilai_Pengembangan = 'C'
                        break
                    if 60 <= int(Nilai) <= 69:
                        Nilai_Pengembangan = 'D'
                        break
                    else:
                        Nilai_Pengembangan = 'E'
                        break

                while True:
                    while True:
                        Nilai = input('Masukan Nilai Budaya Organisasi: ')
                        if str.isnumeric(Nilai):
                            break
                        else:
                            print('Masukan Hanya Angka! (0-100) ')
                        continue
                    break

                while True:
                    if 90 <= int(Nilai) <= 100:
                        Nilai_Budaya = 'A'
                        break
                    if 80 <= int(Nilai) <= 89:
                        Nilai_Budaya = 'B'
                        break
                    if 70 <= int(Nilai) <= 79:
                        Nilai_Budaya = 'C'
                        break
                    if 60 <= int(Nilai) <= 69:
                        Nilai_Budaya = 'D'
                        break
                    else:
                        Nilai_Budaya = 'E'
                        break
                #Untuk Mengetahui Mahasiswa Sudah Ada Di Table Atau Belum.
                for item in table:
                    if Nim.capitalize() == item[0] or Nama.title() == item[1]:
                        print('Mahasiswa sudah terdaftar')
                        break
                else:   
                    table.append([
                        Nim.capitalize(),
                        Nama.title(),
                        Jurusan.capitalize(),
                        Nilai_Pengantar,
                        Nilai_Pengembangan,
                        Nilai_Budaya
                    ])
                    menampilkan(table)
                    pass
                
                while True:
                    print(Pilihan_tambah)
                    menu_pilihan = input('Masukan Menu Yang Dipilih: ')
                    if str.isalpha(menu_pilihan) and menu_pilihan.upper() == 'Y':
                        break
                    elif str.isalpha(menu_pilihan) and menu_pilihan.upper() == 'N':
                        FLAG = False
                        break
                    else:
                        print('Hanya Masukan Huruf (Y atau N)! ')
                    
                break
            #Untuk Kembali Ke Main Menu.
            elif menu_pilihan == '2':
                return
            else:
                print('Masukan Pilihan Yang Sesuai! ')
            break



#Fungsi Menghapus
        
#Teks Pilihan Konfirmasi Untuk Menghapus Data Lagi Atau Tidak.
Pilihan_delete ='''

Apakah Mau Menghapus Data Lagi? (Y/N)

'''

#Pilihan Sub Menu Dalam Fungsi Menghapus/Delete.
Sub_menu_delete ='''

=================================== Pilih Menu: ===================================

                                    1. delete table
                                    2. Menu utama

===================================================================================

'''
def menghapus(table):
    FLAG = True
    while FLAG:
    
        while True:
            print(Sub_menu_delete)
            menu_pilihan = input('Masukan Menu Yang Dipilih: ')
            #Untuk Menghapus Daftar Nilai Mahasiswa/Table.
            if menu_pilihan =='1':
                print(menampilkan(table))

                while True:
                    Nim = input('Masukan Nim mahasiswa: ')
                    if str.isalnum(Nim):
                        break
                    else:
                        continue
                while True:
                    for item in table:
                        if Nim.capitalize() == item[0]:
                            del table[table.index(item)]
                            menampilkan(table)
                            break
                    else:
                        print('Nim Mahasiswa Tidak Ada! ')
                        break
                    break
            
                while True:
                    print(Pilihan_delete)
                    menu_pilihan = input('Masukan Menu Yang Dipilih: ')
                    if str.isalpha(menu_pilihan) and menu_pilihan.upper() == 'Y':
                        break
                    elif str.isalpha(menu_pilihan) and menu_pilihan.upper() == 'N':
                        FLAG = False
                        break
                    else:
                        print('Hanya Masukan Huruf (Y atau N)! ')   
                break
            #Kembali Ke Main Menu.
            elif menu_pilihan == '2':
                return
            else:
                print('Masukan Pilihan Yang Sesuai! ')



#Fungsi Update
                
#Teks Pilihan Konfirmasi Untuk Mengubah Data Lagi Atau Tidak.
pilihan_update = f'''

Apakah Mau Mengubah Nilai Lagi? (Y/N)

'''

#Pilihan Sub Menu Dalam Fungsi Mengubah/Update.
Sub_menu_update = f'''

==================================== Pilih Menu: ==================================

                                    1. Update Nilai
                                    2. Menu utama

===================================================================================

'''
    
def mengupdate(table):

    FLAG = True
    while FLAG:

        while True:
            print(Sub_menu_update)
            menu_pilihan = input('Masukan Menu Yang Dipilih: ')
            #Untuk Mengubah Nilai Mahasiswa/Isi Table.
            if menu_pilihan =='1':
                print(menampilkan(table))

                while True:

                    Nim_mahasiswa = input('Masukan Nim Mahasiswa Yang Akan di Ubah Nilai Nya: ')
                    if str.isalnum(Nim_mahasiswa):
                        break
                    else:
                        print('Hanya Masukan Huruf Dan Angka! ')

                for item in table:
                    if Nim_mahasiswa.capitalize() == item[0]:
                        print('''
                            
==================== Pilih Nilai Mata Kuliah Yang Mau Di Ubah: ===================
    
                            1. Pengantar Organisasi
                            2. Pengembangan Organisasi
                            3. Budaya Organisasi
                    
==================================================================================
                            ''')
                        break
                else:
                    print('Nim Tidak Ada, Masukan Ulang Nim! ')
                    continue

                while True:

                    konfirmasi = input("Pilih No: ")
                    if str.isnumeric(konfirmasi):
                        break
                    else:
                        print('Masukan Hanya Angka! (1, 2 dan 3) ')
                        continue
                    
                while True:
                    #Untuk Mengubah Nilai.
                    if konfirmasi == '1':
                        while True:
                            Nilai = input('Masukan Nilai Pengantar Organisasi Yang Baru: ')
                            if str.isnumeric(Nilai):
                                break
                            else:
                                print('Hanya Masukan Angka (0 - 100)')
                                continue

                        while True:
                            if 90 <= int(Nilai) <= 100:
                                Nilai_baru = 'A'
                                break
                            if 80 <= int(Nilai) <= 89:
                                Nilai_baru = 'B'
                                break
                            if 70 <= int(Nilai) <= 79:
                                Nilai_baru = 'C'
                                break
                            if 60 <= int(Nilai) <= 69:
                                Nilai_baru = 'D'
                                break
                            else:
                                Nilai_baru = 'E'
                                break

                        item[3]= Nilai_baru

                        menampilkan(table)
                        break
                    #Untuk Mengubah Nilai.
                    elif konfirmasi == '2':
                        while True:
                            Nilai = input('Masukan Nilai Pengembangan Organisasi Yang Baru: ')
                            if str.isnumeric(Nilai):
                                break
                            else:
                                print('Hanya Masukan Angka (0 - 100)')
                                continue

                        while True:
                            if 90 <= int(Nilai) <= 100:
                                Nilai_baru = 'A'
                                break
                            if 80 <= int(Nilai) <= 89:
                                Nilai_baru = 'B'
                                break
                            if 70 <= int(Nilai) <= 79:
                                Nilai_baru = 'C'
                                break
                            if 60 <= int(Nilai) <= 69:
                                Nilai_baru = 'D'
                                break
                            else:
                                Nilai_baru = 'E'
                                break

                        item[4]= Nilai_baru

                        menampilkan(table)
                        break
                    #Untuk Mengubah Nilai.
                    elif konfirmasi == '3':
                        while True:
                            Nilai = input('Masukan Nilai Budaya Organisasi Yang Baru: ')
                            if str.isnumeric(Nilai):
                                break
                            else:
                                print('Hanya Masukan Angka (0 - 100)')
                                continue

                        while True:
                            if 90 <= int(Nilai) <= 100:
                                Nilai_baru = 'A'
                                break
                            if 80 <= int(Nilai) <= 89:
                                Nilai_baru = 'B'
                                break
                            if 70 <= int(Nilai) <= 79:
                                Nilai_baru = 'C'
                                break
                            if 60 <= int(Nilai) <= 69:
                                Nilai_baru = 'D'
                                break
                            else:
                                Nilai_baru = 'E'
                                break

                        item[4]= Nilai_baru

                        menampilkan(table)
                        break

                    else:
                        print('Hanya Masukan Angka Yang Ada Dipilihan! ')
                        break
                    
                while True:
                    print(pilihan_update)
                    menu_pilihan = input('Masukan Menu Yang Dipilih: ')
                    if str.isalpha(menu_pilihan) and menu_pilihan.upper() == 'Y':
                        break
                    elif str.isalpha(menu_pilihan) and menu_pilihan.upper() == 'N':
                        FLAG = False
                        break
                    else:
                        print('Hanya Masukan Huruf (Y atau N)! ')
                break
            elif menu_pilihan == '2':
                return
            else:
                print('Masukan Pilihan Yang Sesuai! ')