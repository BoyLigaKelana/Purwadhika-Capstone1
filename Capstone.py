Kumpulan_mobil = []

def menu():
    while True:
        print('-'*40)
        print("PROGRAM RENTAL MOBIL".center(40,"="))
        print('-'*40)

        print('''
    1. Tambah Mobil
    2. Hapus Mobil          
    3. List Mobil          
    4. Edit          
    5. Cek Ketersediaan Mobil          
    6. Filter Transmisi
    7. Keluar          
            ''')
        print(('-'*40))

        pilihan = input('Masukan Kode Menu: ')
        if pilihan == '1' :
            tambah_mobil()
        elif pilihan == '2' :
            hapus_mobil()
        elif pilihan == '3' :
            list_mobil()
        elif pilihan == '4' :
            edit_mobil()
        elif pilihan == '5' :
            cek_ketersediaan_mobil()
        elif pilihan == '6' :
            transmisi_mobil()
        elif pilihan == '7':
            break
        else:
            break

# Tambah Mobil
def tambah_mobil():
    print('-'*40)
    print("Tambah Mobil".center(40,"="))
    print('-'*40)

    plat_nomor= input('Plat Nomor Mobil= ')
    nama_mbl = input('Masukkan Nama Mobil: ')
    tahun_mobil = input('Masukkan Tahun Keluar Mobil: ')
    transmisi_mobil = input ('Masukkan Transmisi Mobil: ')
    jns_mbl= input('Jenis Mobil= ')

    data = {
        'Plat Mobil':  plat_nomor,
        'Nama':  nama_mbl,
        'Tahun Keluaran Mobil': tahun_mobil,
        'Transmisi Mobil': transmisi_mobil,
        'Jenis Mobil': jns_mbl
    }
    Kumpulan_mobil.append(data)
    print('\nList Mobil')

    list_mobil()

    lanjut = input('Lanjut menambahkan mobil (y/n): ')
    if lanjut == 'y':
        tambah_mobil()
    else:
        menu()

# Hapus Mobil
def hapus_mobil():
    print('-'*40)
    print("Hapus Mobil".center(40,"="))
    print('-'*40)

    hapus_mbl = input ('Masukkan Plat Mobil yang ingin di hapus: ')

    for mobil in Kumpulan_mobil:
        if mobil["Plat Mobil"] == hapus_mbl:
            Kumpulan_mobil.remove(mobil)                    
            list_mobil()

            lanjut = input('Lanjut menghapus mobil (y/n): ')
            if lanjut == 'y':
                pass
            else:
                menu()
        else:
            print('mobil yang ingin anda hapus tidak tersedia!')

# Edit Mobil
def edit_mobil():
    print('-'*40)
    print("Edit Mobil".center(40,"="))
    print('-'*40)

    edit_mbl = input ('Masukkan Plat Mobil yang ingin di edit: ')

    for mobil in Kumpulan_mobil:
        if mobil["Plat Mobil"] == edit_mbl:

            plat_nomor= input('Plat Nomor Mobil ('+mobil['Plat Mobil']+'): ')
            nama_mbl = input('Masukkan Nama Mobil ('+mobil['Nama']+'): ')
            tahun_mobil = input('Masukkan Tahun Keluar Mobil ('+mobil['Tahun Keluaran Mobil']+'):')
            transmisi_mobil = input ('Masukkan Transmisi Mobil('+mobil['Transmisi Mobil']+'):')
            jns_mbl= input('Jenis Mobil ('+mobil['Jenis Mobil']+')= ')

            mobil['Plat Mobil'] = plat_nomor
            mobil['Nama'] = nama_mbl
            mobil['Tahun Keluaran Mobil'] = tahun_mobil
            mobil['Transmisi Mobil'] = transmisi_mobil
            mobil['Jenis Mobil'] = jns_mbl
            
            list_mobil()

            lanjut = input('Lanjut mengedit mobil (y/n): ')
            if lanjut == 'y':
                pass
            else:
                menu()
        else:
            print('mobil yang ingin anda edit tidak tersedia!')

#DAFTAR MOBIL
def list_mobil(list = Kumpulan_mobil):
    print('-'*40)
    print("Daftar Mobil".center(40,"="))
    print('-'*40)

    for mobil in list:
        print("Nama : "+mobil['Nama'])
        print("Plat : "+mobil['Plat Mobil'])
        print('Tahun Keluaran :'+mobil['Tahun Keluaran Mobil'])
        print('Transmisi :'+mobil["Transmisi Mobil"])
        print("Jenis : "+mobil['Jenis Mobil'])
        print("="*40)      

#KETERSEDIAAN MOBIL
def cek_ketersediaan_mobil():
    print('-'*40)
    print("Ketersediaan Mobil".center(40,"="))
    print('-'*40)

    Ketersediaan_mobil = input ('Masukkan Plat Nomor Mobil: ')

    for mobil in Kumpulan_mobil:
        if mobil["Plat Mobil"] == Ketersediaan_mobil:
            print('Mobil Tersedia')
        else:
            print("Mobil tidak tersedia")

#Filter Transmisi mobil
def transmisi_mobil():
    print('-'*40)
    print("Transmisi Mobil".center(40,"="))
    print('-'*40)

    filter_mobil = input('Masukan Jenis Transmisi: ')
    list_baru = []
    for mobil in Kumpulan_mobil:
        if mobil ['Transmisi Mobil'] == filter_mobil:
            list_baru.append(mobil)
    list_mobil(list_baru)        

def keluar():
    menu()

menu()