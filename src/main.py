import grade

database = [
    ['B521', 'Muhammad Signori', 'Manajemen', 'A', 'A', 'A'],
    ['B522', 'Taufiq Purwanto', 'Manajemen', 'A', 'A', 'A'],
    ['B523', 'Muhammad Fernanda', 'Manajemen', 'A', 'A', 'A'], 
]

main_menu = f'''

==================== Daftar Nilai Mahasiswa Manajemen Kelas B ====================

                                    List Menu:

                                    1. Baca Data
                                    2. Menambah
                                    3. Menghapus
                                    4. Mengupdate
                                    5. Keluar

==================================================================================                

'''

def main():
    while True:
        choice = input(main_menu)
        if choice == '1':
            grade.read_data(database)
        elif choice == '2':
            grade.menambah(database)
        elif choice == '3':
            grade.menghapus(database)
        elif choice == '4':
            grade.mengupdate(database)
        elif choice == '5':
            while True:
                if choice == '5':
                    print('Apakah Yakin Ingin Keluar? (Y/N)')
                    menu_pilihan = input('Masukan Menu Yang Dipilih: (Y/N)' )
                    if str.isalpha(menu_pilihan.upper()) == 'N':
                        break
                    elif str(menu_pilihan.upper()) == 'Y':
                        print('Terimakasih Selamat Beraktivitas...')
                        return
                break
        else:
            print('Masukan angka sesuai pilihan (1-5)')
            continue

main()