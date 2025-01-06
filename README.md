# Solana Wallet Generator

## Description
This script generates multiple Solana wallets and saves their public and private key pairs to a text file. It is designed for developers and blockchain enthusiasts who need to quickly generate and manage multiple wallets for testing or other purposes.

## Features
- Generate multiple Solana wallets in one go.
- Save wallet public and private keys securely in a text file.
- Automatically creates a `data` folder to store generated wallet files.

---

## Prerequisites
- Python 3.8 or higher installed on your system.
- Install the required dependency [`solders`](https://pypi.org/project/solders/):

  ```bash
  pip install solders
  ```

---

## Usage

1. **Clone the repository or download the script.**
   ```bash
   git clone https://github.com/your-username/solana-wallet-generator.git
   cd solana-wallet-generator
   ```

2. **Run the script.**
   Execute the script using Python:
   ```bash
   python solana_wallet_generator.py
   ```

3. **Input the required details.**
   - Enter the number of wallets you want to generate.
   - Specify the name of the output file (without the `.txt` extension). The script will save the file in the `data` folder.

   Example input:
   ```plaintext
   Masukkan jumlah wallet yang ingin dihasilkan: 5
   Masukkan nama file output (tanpa ekstensi .txt): my_wallets
   ```

4. **Check the output.**
   - The script will create a `data` folder (if it doesn't already exist).
   - Inside the `data` folder, you will find your file (`my_wallets.txt` in this case) containing the generated wallets.

   Example output file (`my_wallets.txt`):
   ```plaintext
   7eZPQ1FqckHC3duqj5G3hykQevgtRW7xDz3foKzAkFAW|5EVcUpThSGj1hvzSU6j1XaS6H3m2pRT4Q4KZ3W...
   Fy7cdDjTHNMQYZ5jNpL5DaBCuwjMHwphzRKh9Xpmv3Xp|3Gi5cXAWEmRiMkxzYZ2DwyLGcXnbVp2wrA8TZ9...
   ```

---

## Notes
- **Keep the private keys secure.** The private keys are sensitive and should not be shared or exposed publicly.
- Ensure that the `solders` library is installed and up-to-date.
- The script is intended for educational and testing purposes. Use responsibly in production environments.

---

## Troubleshooting
- If you encounter errors, ensure that:
  - Python is correctly installed.
  - The `solders` library is installed.
  - You have write permissions to the directory where the script is executed.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!
