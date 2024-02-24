from prettytable import PrettyTable
import os
os.system("cls")

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

class SistemPemesananBunga:
    def __init__(self):
        self.daftar_pesanan = []
        self.id_terakhir = 0

    def tambah_pesanan(self, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman):
        self.id_terakhir += 1
        pesanan = PesananBunga(self.id_terakhir, nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman)
        self.daftar_pesanan.append(pesanan)
        print("+---------------------------------+")
        print("| Pesanan berhasil ditambahkan.💐 |")
        print("+---------------------------------+")
        print("ID Pesanan:", self.id_terakhir)

    def hitung_total_harga(self):
        total_harga = 0
        for pesanan in self.daftar_pesanan:
            total_harga += pesanan.total_harga
        return total_harga

    def baca_semua_pesanan(self):
        if not self.daftar_pesanan:
            print("+------------------------------------+")
            print("| Belum ada pesanan yang tersedia.💐 |")
            print("+------------------------------------+")
            return
        table = PrettyTable()
        table.title = "Data Pemesanan Bunga 𓍢ִ໋🌷͙֒✧˚ ༘ ⋆｡˚♡"
        table.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Bunga", "Harga", "Jumlah", "Tanggal Pengiriman", "Total Harga"]
        for pesanan in self.daftar_pesanan:
            table.add_row([pesanan.id_pesanan, pesanan.nama_pelanggan, pesanan.jenis_bunga, pesanan.harga, pesanan.jumlah, pesanan.tanggal_pengiriman, pesanan.total_harga])
        print(table)

    def baca_pesanan(self, id_pesanan):
        for pesanan in self.daftar_pesanan:
            if pesanan.id_pesanan == id_pesanan:
                table = PrettyTable()
                table.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Bunga", "Harga", "Jumlah", "Tanggal Pengiriman", "Total Harga"]
                table.add_row([pesanan.id_pesanan, pesanan.nama_pelanggan, pesanan.jenis_bunga, pesanan.harga, pesanan.jumlah, pesanan.tanggal_pengiriman, pesanan.total_harga])
                print(table)
                return
        print("+----------------------------+")
        print("| Pesanan tidak ditemukan.💐 |")
        print("+----------------------------+")

    def update_pesanan(self, id_pesanan, jenis_bunga, harga, jumlah):
        if jenis_bunga == "" or harga == "" or jumlah == "":
            print("+------------------------------------------------+")
            print("| Input tidak boleh kosong. Silakan coba lagi.💐 |")
            print("+------------------------------------------------+")
            return
        for pesanan in self.daftar_pesanan:
            if pesanan.id_pesanan == id_pesanan:
                pesanan.update_jenis_dan_harga(jenis_bunga, float(harga))
                pesanan.jumlah = int(jumlah)
                print("+--------------------------------+")
                print("| Pesanan berhasil diperbarui.💐 |")
                print("+--------------------------------+")
                return
        print("+----------------------------+")
        print("| Pesanan tidak ditemukan.💐 |")
        print("+----------------------------+")

    def hapus_pesanan(self, id_pesanan):
        for pesanan in self.daftar_pesanan:
            if pesanan.id_pesanan == id_pesanan:
                self.daftar_pesanan.remove(pesanan)
                print("+-----------------------------+")
                print("| Pesanan berhasil dihapus.💐 |")
                print("+-------------------------- --+")
                return
        print("+----------------------------+")
        print("| Pesanan tidak ditemukan.💐 |")
        print("+----------------------------+")

def main():
    sistem_pemesanan = SistemPemesananBunga()
    while True:
        os.system("cls")
        print("+=========================================================================================+")
        print("|                    °❀⋆.ೃ࿔*:･๋࣭ ⭑⚝  Sistem Pemesanan Bunga ⭑⚝ °❀⋆.ೃ࿔*:･                    |")
        print("+=========================================================================================+")
        print("|  1. Tambah Pesanan 🌷                                                                   |")
        print("|  2. Baca Semua Pesanan 🌼                                                               |")
        print("|  3. Baca Pesanan Berdasarkan ID 🌺                                                      |")
        print("|  4. Update Pesanan 🌻                                                                   |")
        print("|  5. Hapus Pesanan 🌸                                                                    |")
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
            sistem_pemesanan.tambah_pesanan(nama_pelanggan, jenis_bunga, harga, jumlah, tanggal_pengiriman)
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
            id_pesanan = int(input("Masukkan ID Pesanan yang ingin dihapus: "))
            sistem_pemesanan.hapus_pesanan(id_pesanan)
            input("\nTekan 'Enter' untuk melanjutkan...")

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