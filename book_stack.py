class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Buku:
    def __init__(self, title, author):
        self.title = title
        self.author = author


def tambah_buku(stack):
    judul = input("masukkan judul: ")
    pengarang = input("Masukkan pengarang: ")
    buku = Buku(judul, pengarang)
    stack.push(buku)
    print("Buku berhasil ditambahkan ke dalam tumpukan.")


def menghapus_buku(stack):
    if not stack.is_empty():
        removed_book = stack.pop()
        print(
            f"Buku '{removed_book.title}' oleh {removed_book.author} dihapus dari tumpukan.")
    else:
        print("Tumpukan kosong. Tidak ada buku yang dapat dihapus.")


def tampilan_barang_teratas(stack):
    if not stack.is_empty():
        top_book = stack.peek()
        print("Buku teratas:")
        print(f"Judul: {top_book.title}")
        print(f"Pengarang: {top_book.author}")
    else:
        print("Tumpukan kosong. Tidak ada buku yang ditampilkan.")


def main():
    stack = Stack()
    while True:
        print("\nPilih operasi:")
        print("1. Tambahkan buku")
        print("2. Hapus buku terakhir")
        print("3. Tampilkan buku teratas")
        print("4. Keluar")
        Pilihan = input("Masukkan Pilihan (1/2/3/4): ")

        if Pilihan == "1":
            tambah_buku(stack)
        elif Pilihan == "2":
            menghapus_buku(stack)
        elif Pilihan == "3":
            tampilan_barang_teratas(stack)
        elif Pilihan == "4":
            print("Program Telah Selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
