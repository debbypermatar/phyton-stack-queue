class Transaction:
    def __init__(self, customer_name, transaction_type):
        self.customer_name = customer_name
        self.transaction_type = transaction_type


class TransactionQueue:
    def __init__(self):
        self.queue = []

    def add_transaction(self, customer_name, transaction_type):
        transaction = Transaction(customer_name, transaction_type)
        self.queue.append(transaction)

    def remove_transaction(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def next_transaction(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None


def main():
    transaction_queue = TransactionQueue()

    while True:
        print("=== Menu ===")
        print("1. Tambahkan transaksi ke antrian")
        print("2. Hapus transaksi yang telah dilayani")
        print("3. Tampilkan transaksi berikutnya")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            customer_name = input("Masukkan nama pelanggan: ")
            transaction_type = input("Masukkan jenis transaksi: ")
            transaction_queue.add_transaction(customer_name, transaction_type)
            print("Transaksi berhasil ditambahkan ke antrian.")
            print()

        elif choice == "2":
            removed_transaction = transaction_queue.remove_transaction()
            if removed_transaction:
                print(
                    f"Transaksi yang dihapus: {removed_transaction.customer_name} - {removed_transaction.transaction_type}")
            else:
                print("Antrian transaksi kosong.")
            print()

        elif choice == "3":
            next_transaction = transaction_queue.next_transaction()
            if next_transaction:
                print(
                    f"Transaksi berikutnya: {next_transaction.customer_name} - {next_transaction.transaction_type}")
            else:
                print("Antrian transaksi kosong.")
            print()

        elif choice == "0":
            print("Program selesai.")
            break


if __name__ == "__main__":
    main()
