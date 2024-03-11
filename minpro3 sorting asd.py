from prettytable import PrettyTable
import os

class PesananBunga:
    def __init__(self, id_pesanan, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman):
        self.id_pesanan = id_pesanan
        self.nama_pelanggan = nama_pelanggan
        self.jenis_bunga = jenis_bunga
        self.harga = harga
        self.jumlah = jumlah
        self.tanggal_pengiriman = tanggal_pengiriman
        self.total_harga = harga * jumlah

    def update_jenis_dan_harga(self, jenis_bunga, harga):
        self.jenis_bunga = jenis_bunga
        self.harga = harga
        self.total_harga = self.harga * self.jumlah

class Node:
    def __init__(self, pesanan):
        self.pesanan = pesanan
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, pesanan):
        node_baru = Node(pesanan)
        node_baru.next = self.head
        self.head = node_baru

    def tambah_di_akhir(self, pesanan):
        node_baru = Node(pesanan)
        if not self.head:
            self.head = node_baru
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node_baru

    def tambah_di_antara(self, id_sebelum, pesanan):
        if not self.head:
            print("+-------------------------------------------------+")
            print("| List kosong. Tidak bisa menambahkan di antara.🌼|")
            print("+-------------------------------------------------+")
            return
        node_baru = Node(pesanan)
        current_node = self.head
        while current_node:
            if current_node.pesanan.id_pesanan == id_sebelum:
                node_baru.next = current_node.next
                current_node.next = node_baru
                return
            current_node = current_node.next
        print("+----------------------------------------------------------------+")
        print("| ID Pesanan tidak ditemukan. Tidak bisa menambahkan di antara.🌼|")
        print("+----------------------------------------------------------------+")

    def hapus_di_awal(self):
        if not self.head:
            print("+--------------------------------------------+")
            print("| List kosong. Tidak ada yang bisa dihapus.🌼|")
            print("+--------------------------------------------+")
            return
        self.head = self.head.next

    def hapus_di_akhir(self):
        if not self.head:
            print("+--------------------------------------------+")
            print("| List kosong. Tidak ada yang bisa dihapus.🌼|")
            print("+--------------------------------------------+")
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def hapus_di_antara(self, id_hapus):
        if not self.head:
            print("+--------------------------------------------+")
            print("| List kosong. Tidak ada yang bisa dihapus.🌼|")
            print("+--------------------------------------------+")
            return
        if self.head.pesanan.id_pesanan == id_hapus:
            self.head = self.head.next
            return
        prev_node = self.head
        current_node = self.head.next
        while current_node:
            if current_node.pesanan.id_pesanan == id_hapus:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next
        print("+-----------------------------------------------------------+")   
        print("| ID Pesanan tidak ditemukan. Tidak ada yang bisa dihapus.🌼|")
        print("+-----------------------------------------------------------+")

    def quick_sort_id(self, arr, ascending=True):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0].id_pesanan
            lower = [pesanan for pesanan in arr[1:] if pesanan.id_pesanan < pivot]
            greater = [pesanan for pesanan in arr[1:] if pesanan.id_pesanan >= pivot]
            if ascending:
                return self.quick_sort_id(lower, ascending) + [arr[0]] + self.quick_sort_id(greater, ascending)
            else:
                return self.quick_sort_id(greater, ascending) + [arr[0]] + self.quick_sort_id(lower, ascending)

    def quick_sort_total_harga(self, arr, ascending=True):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0].total_harga
            less = [pesanan for pesanan in arr[1:] if pesanan.total_harga < pivot]
            greater = [pesanan for pesanan in arr[1:] if pesanan.total_harga >= pivot]

            if ascending:
                return self.quick_sort_total_harga(less, ascending) + [arr[0]] + self.quick_sort_total_harga(greater, ascending)
            else:
                return self.quick_sort_total_harga(greater, ascending) + [arr[0]] + self.quick_sort_total_harga(less, ascending)

    def sort_pesanan_id(self, ascending=True):
        pesanan_list = []
        current = self.head
        while current:
            pesanan_list.append(current.pesanan)
            current = current.next

        sorted_pesanan = self.quick_sort_id(pesanan_list, ascending)
        self.head = None
        for pesanan in sorted_pesanan:
            self.tambah_di_akhir(pesanan)

    def sort_pesanan_total_harga(self, ascending=True):
        pesanan_list = []
        current = self.head
        while current:
            pesanan_list.append(current.pesanan)
            current = current.next

        sorted_pesanan = self.quick_sort_total_harga(pesanan_list, ascending)
        self.head = None
        for pesanan in sorted_pesanan:
            self.tambah_di_akhir(pesanan)

class SistemPemesananBunga:
    def __init__(self):
        self.daftar_pesanan = LinkedList()
        self.id_terakhir = 0

    def baca_semua_pesanan(self):
        current = self.daftar_pesanan.head
        if not current:
            print("+------------------------------------+")
            print("| Belum ada pesanan yang tersedia.💐 |")
            print("+------------------------------------+")
            return
        table = PrettyTable()
        table.title = "Data Pemesanan Bunga 𓍢ִ໋🌷͙֒✧˚ ༘ ⋆｡˚♡"
        table.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Bunga", "Harga", "Jumlah", "Tanggal Pengiriman", "Total Harga"]
        while current:
            pesanan = current.pesanan
            table.add_row([pesanan.id_pesanan, pesanan.nama_pelanggan, pesanan.jenis_bunga, pesanan.harga, pesanan.jumlah, pesanan.tanggal_pengiriman, pesanan.total_harga])
            current = current.next
        print(table)
    
    def hitung_total_harga(self):
        total_harga = 0
        current = self.daftar_pesanan.head
        while current:
            pesanan = current.pesanan
            total_harga += pesanan.total_harga
            current = current.next
        return total_harga

    def baca_pesanan(self, id_pesanan):
        current = self.daftar_pesanan
        while current:
            pesanan = current.data
            if pesanan.id_pesanan == id_pesanan:
                table = PrettyTable()
                table.title = "Data Pesanan"
                table.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Bunga", "Harga", "Jumlah", "Tanggal Pengiriman", "Total Harga"]
                table.add_row([pesanan.id_pesanan, pesanan.nama_pelanggan, pesanan.jenis_bunga, pesanan.harga, pesanan.jumlah, pesanan.tanggal_pengiriman, pesanan.total_harga])
                print(table)
                return
            current = current.next
        print("+----------------------------+")
        print("| Pesanan tidak ditemukan.💐 |")
        print("+----------------------------+")

    def update_pesanan(self, id_pesanan, jenis_bunga, harga, jumlah):
        current = self.daftar_pesanan
        while current:
            pesanan = current.data
            if pesanan.id_pesanan == id_pesanan:
                pesanan.update_jenis_dan_harga(jenis_bunga, float(harga))
                pesanan.jumlah = int(jumlah)
                print("+--------------------------------+")
                print("| Pesanan berhasil diperbarui.💐 |")
                print("+--------------------------------+")
                return
            current = current.next
        print("+----------------------------+")
        print("| Pesanan tidak ditemukan.💐 |")
        print("+----------------------------+")

    def tambah_pesanan_di_awal(self, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman):
        self.id_terakhir += 1
        pesanan = PesananBunga(self.id_terakhir, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman)
        self.daftar_pesanan.tambah_di_awal(pesanan)
        print("+---------------------------------+")
        print("| Pesanan berhasil ditambahkan.💐 |")
        print("+---------------------------------+")
        print("ID Pesanan:", self.id_terakhir)

    def tambah_pesanan_di_akhir(self, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman):
        self.id_terakhir += 1
        pesanan = PesananBunga(self.id_terakhir, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman)
        self.daftar_pesanan.tambah_di_akhir(pesanan)
        print("+---------------------------------+")
        print("| Pesanan berhasil ditambahkan.💐 |")
        print("+---------------------------------+")
        print("ID Pesanan:", self.id_terakhir)

    def tambah_pesanan_di_antara(self, id_sebelum, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman):
        self.id_terakhir += 1
        pesanan = PesananBunga(self.id_terakhir, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman)
        self.daftar_pesanan.tambah_di_antara(id_sebelum, pesanan)
        print("+---------------------------------+")
        print("| Pesanan berhasil ditambahkan.💐 |")
        print("+---------------------------------+")
        print("ID Pesanan:", self.id_terakhir)

    def hapus_pesanan_di_awal(self):
        self.daftar_pesanan.hapus_di_awal()
        print("+-----------------------------+")
        print("| Pesanan berhasil dihapus.💐 |")
        print("+-----------------------------+")

    def hapus_pesanan_di_akhir(self):
        self.daftar_pesanan.hapus_di_akhir()
        print("+-----------------------------+")
        print("| Pesanan berhasil dihapus.💐 |")
        print("+-----------------------------+")

    def hapus_pesanan_di_antara(self, id_pesanan):
        self.daftar_pesanan.hapus_di_antara(id_pesanan)
        print("+-----------------------------+")
        print("| Pesanan berhasil dihapus.💐 |")
        print("+-----------------------------+")

    def sorting_menu(self):
        while True:
            os.system("cls")
            print("+=================================================+")
            print("|         Sorting Menu - ID & Harga ༘⋆✿            |")
            print("+=================================================+")
            print("|  1. Sortir berdasarkan ID (Ascending)           |")
            print("|  2. Sortir berdasarkan ID (Descending)          |")
            print("|  3. Sortir berdasarkan Total Harga (Ascending)  |")
            print("|  4. Sortir berdasarkan Total Harga (Descending) |")
            print("|  5. Kembali ke Menu Utama                       |")
            print("+=================================================+")
            pilihan_sorting = input("Masukkan pilihan sorting: ")

            if pilihan_sorting == "1":
                self.daftar_pesanan.sort_pesanan_id(ascending=True)
                print("🌸-------------------------------------------------------------🌸")
                print("|   Sorting berhasil dilakukan berdasarkan ID secara ascending. |")
                print("|         Silahkan kembali ke menu utama untuk melihat          |")
                print("|           data pemesanan terbaru setelah di sorting           |")
                print("|                       (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧🌷                         |")
                print("🌸-------------------------------------------------------------🌸")
                input("\nTekan 'Enter' untuk melanjutkan...")
            elif pilihan_sorting == "2":
                self.daftar_pesanan.sort_pesanan_id(ascending=False)
                print("🌸-------------------------------------------------------------🌸")
                print("|  Sorting berhasil dilakukan berdasarkan ID secara descending. |")
                print("|         Silahkan kembali ke menu utama untuk melihat          |")
                print("|           data pemesanan terbaru setelah di sorting           |")
                print("|                       (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧🌷                         |")
                print("🌸-------------------------------------------------------------🌸")
                input("\nTekan 'Enter' untuk melanjutkan...")
            elif pilihan_sorting == "3":
                self.daftar_pesanan.sort_pesanan_total_harga(ascending=True)
                print("🌸----------------------------------------------------------------------🌸")
                print("|   Sorting berhasil dilakukan berdasarkan Total Harga secara ascending. |")
                print("|               Silahkan kembali ke menu utama untuk melihat             |")
                print("|                data pemesanan terbaru setelah di sorting               |")
                print("|                            (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧🌷                             |")
                print("🌸----------------------------------------------------------------------🌸")
                input("\nTekan 'Enter' untuk melanjutkan...")
            elif pilihan_sorting == "4":
                self.daftar_pesanan.sort_pesanan_total_harga(ascending=False)
                print("🌸----------------------------------------------------------------------🌸")
                print("|  Sorting berhasil dilakukan berdasarkan Total Harga secara descending. |")
                print("|               Silahkan kembali ke menu utama untuk melihat             |")
                print("|                data pemesanan terbaru setelah di sorting               |")
                print("|                            (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧🌷                             |")
                print("🌸----------------------------------------------------------------------🌸")
                input("\nTekan 'Enter' untuk melanjutkan...")
            elif pilihan_sorting == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

def main():
    sistem_pemesanan = SistemPemesananBunga()
    while True:
        print("+=========================================================================================+")
        print("|                    °❀⋆.ೃ࿔*:･๋࣭ ⭑⚝  Sistem Pemesanan Bunga ⭑⚝ °❀⋆.ೃ࿔*:･                    |")
        print("+=========================================================================================+")
        print("|  1. Tambah Pesanan 🌷                                                                   |")
        print("|  2. Baca Semua Pesanan 🌼                                                               |")
        print("|  3. Baca Pesanan Berdasarkan ID 🌺                                                      |")
        print("|  4. Update Pesanan 🌻                                                                   |")
        print("|  5. Hapus Pesanan 🌸                                                                    |")
        print("|  6. Sorting 🌹                                                                          |")
        print("|  0. Keluar 🌷                                                                           |")
        print("+=========================================================================================+")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            os.system("cls")
            print("+=============================================+")
            print("|         Input Data Pemesanan Bunga 🌷       |")
            print("+=============================================+")
            nama_pelanggan = input("Masukkan Nama Pelanggan: ")
            jenis_bunga = input("Masukkan Jenis Bunga : ")
            while len(jenis_bunga) < 2 or len(jenis_bunga) > 20:
                print("+---------------------------------------------------------------------------+")
                print("| Jenis Bunga harus memiliki minimal 2 karakter dan maksimal 20 karakter.🌺 |")
                print("+---------------------------------------------------------------------------+")
                jenis_bunga = input("Masukkan Jenis Bunga: ")

            harga = float(input("Masukkan Harga : "))
            while harga < 500 or harga > 500000:
                print("+-------------------------------------------------------------+")
                print("| Harga harus minimal Rp.500,00 dan maksimal Rp.500.000,00.🌺 |")
                print("+-------------------------------------------------------------+")
                harga = float(input("Masukkan Harga: "))

            jumlah = int(input("Masukkan Jumlah : "))
            while jumlah < 1:
                print("+---------------------------+")
                print("| Jumlah harus minimal 1.🌺 |")
                print("+---------------------------+")
                jumlah = int(input("Masukkan Jumlah: "))

            tanggal_pengiriman = input("Masukkan Tanggal Pengiriman: ")
            print("+=============================================+")
            print("|  1. Tambah di Awal                           |")
            print("|  2. Tambah di Akhir                          |")
            print("|  3. Tambah di Antara                         |")
            print("+=============================================+")
            tambah_pilihan = input("Pilih cara penambahan: ")

            if tambah_pilihan == "1":
                sistem_pemesanan.tambah_pesanan_di_awal(nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman)
            elif tambah_pilihan == "2":
                sistem_pemesanan.tambah_pesanan_di_akhir(nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman)
            elif tambah_pilihan == "3":
                id_sebelum = int(input("Masukkan ID Pesanan sebelumnya: "))
                sistem_pemesanan.tambah_pesanan_di_antara(id_sebelum, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman)
            else:
                print("+------------------------------------+")
                print("| Pilihan tidak valid. Ulangi lagi.💐|")
                print("+------------------------------------+")

            input("\nTekan 'Enter' untuk melanjutkan...")

        elif pilihan == "2":
            os.system("cls")
            sistem_pemesanan.baca_semua_pesanan()
            print("Total Harga Semua Pesanan 💐 :", sistem_pemesanan.hitung_total_harga())
            input("\nTekan 'Enter' untuk melanjutkan...")

        elif pilihan == "3":
            os.system("cls")
            print("+=============================================+")
            print("|      Data Pemesanan Bunga Sesuai ID 🌷      |")
            print("+=============================================+")
            id_pesanan = int(input("Masukkan ID Pesanan yang ingin dibaca: "))
            sistem_pemesanan.baca_pesanan(id_pesanan)
            input("\nTekan 'Enter' untuk melanjutkan...")

        elif pilihan == "4":
            os.system("cls")
            print("+=============================================+")
            print("|       Perbarui Data Pemesanan Bunga 🌷      |")
            print("+=============================================+")
            id_pesanan = int(input("Masukkan ID Pesanan yang ingin diperbarui: "))
            jenis_bunga = input("Masukkan Jenis Bunga Baru : ")
            while len(jenis_bunga) < 2 or len(jenis_bunga) > 20:
                print("+---------------------------------------------------------------------------+")
                print("| Jenis Bunga harus memiliki minimal 2 karakter dan maksimal 20 karakter.🌺 |")
                print("+---------------------------------------------------------------------------+")
                jenis_bunga = input("Masukkan Jenis Bunga Baru: ")

            harga = float(input("Masukkan Harga Baru : "))
            while harga < 500 or harga > 500000:
                print("+-------------------------------------------------------------+")
                print("| Harga harus minimal Rp.500,00 dan maksimal Rp.500.000,00.🌺 |")
                print("+-------------------------------------------------------------+")
                harga = float(input("Masukkan Harga Baru: "))

            jumlah = int(input("Masukkan Jumlah Baru : "))
            while jumlah < 1:
                print("+---------------------------+")
                print("| Jumlah harus minimal 1.🌺 |")
                print("+---------------------------+")
                jumlah = int(input("Masukkan Jumlah Baru: "))

            sistem_pemesanan.update_pesanan(id_pesanan, jenis_bunga, harga, jumlah)
            input("\nTekan 'Enter' untuk melanjutkan...")

        elif pilihan == "5":
            os.system("cls")
            print("+=============================================+")
            print("|         Hapus Data Pemesanan Bunga 🌷       |")
            print("+=============================================+")
            print("|  1. Hapus di Awal                            |")
            print("|  2. Hapus di Akhir                           |")
            print("|  3. Hapus di Antara                          |")
            print("+=============================================+")
            hapus_pilihan = input("Pilih cara penghapusan: ")

            if hapus_pilihan == "1":
                sistem_pemesanan.hapus_pesanan_di_awal()
            elif hapus_pilihan == "2":
                sistem_pemesanan.hapus_pesanan_di_akhir()
            elif hapus_pilihan == "3":
                id_pesanan = int(input("Masukkan ID Pesanan yang ingin dihapus: "))
                sistem_pemesanan.hapus_pesanan_di_antara(id_pesanan)
            else:
                print("+------------------------------------+")
                print("| Pilihan tidak valid. Ulangi lagi.💐|")
                print("+------------------------------------+")

            input("\nTekan 'Enter' untuk melanjutkan...")

        elif pilihan == "6":
            sistem_pemesanan.sorting_menu()

        elif pilihan == "0":
            os.system("cls")
            print("+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")
            print("+🌸   🌼   🌺   🌻   🌹   💐   🌷   🏵️   🌸   🌼   🌺   🌻   🌹   💐   🌷   🏵️    🌸  +")
            print("+                                                                                   +")
            print("+                                   Terima Kasih.                                   +")
            print("+                                 Sampai Jumpa Lagi!                                +")
            print("+                                                                                   +")
            print("+🌸   🌼   🌺   🌻   🌹   💐   🌷   🏵️   🌸   🌼   🌺   🌻   🌹   💐   🌷   🏵️    🌸  +")
            print("+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")
            break

        else:
            print("+------------------------------------------+")
            print("| Pilihan tidak valid. Silakan coba lagi.💐|")
            print("+------------------------------------------+")

main()