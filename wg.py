import base58
from solders.keypair import Keypair
import os

def main():
    try:
        # Ask the user to input the number of wallets and the output file name
        WALLETS_AMOUNT = int(input("Enter the number of wallets to generate: "))
        output_file_name = input("Enter the output file name (without the .txt extension): ") + ".txt"
        OUTPUT_FOLDER = "data"

        # Create the folder if it doesn't exist
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)

        # Path to the output file
        output_file_path = os.path.join(OUTPUT_FOLDER, output_file_name)

        # Write the wallets to the text file
        with open(output_file_path, 'w') as file:
            for x in range(WALLETS_AMOUNT):
                account = Keypair()  # Generate a new keypair
                private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')

                # Write to the text file
                file.write(f"{account.pubkey()}|{private_key}\n")

        print(f"{WALLETS_AMOUNT} wallets have been generated and saved to {output_file_path}")

    except Exception:
        print("Input error")

if __name__ == "__main__":
    main()
