import base58
from solders.keypair import Keypair
import os

def main():
    try:
        # Meminta pengguna untuk memasukkan jumlah wallet dan nama file output
        WALLETS_AMOUNT = int(input("Masukkan jumlah wallet yang ingin dihasilkan: "))
        output_file_name = input("Masukkan nama file output (tanpa ekstensi .txt): ") + ".txt"
        OUTPUT_FOLDER = "data"

        # Buat folder jika belum ada
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)

        # Path untuk file output
        output_file_path = os.path.join(OUTPUT_FOLDER, output_file_name)

        # Menulis wallet ke dalam file teks
        with open(output_file_path, 'w') as file:
            for x in range(WALLETS_AMOUNT):
                account = Keypair()  # Menghasilkan keypair baru
                private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')

                # Menulis ke file teks
                file.write(f"{account.pubkey()}|{private_key}\n")

        print(f"{WALLETS_AMOUNT} wallets have been generated and saved to {output_file_path}")

    except Exception:
        print("eror input")

if __name__ == "__main__":
    main()
