# Brute Force MD5 CTF Solver

This is a simple Python solution to brute-force an MD5 hash for CTF challenges using asynchronous HTTP requests. The code sends HTTP GET requests to a target URL, testing each possible MD5 hash character (hexadecimal) and then tries to find the flag from the server.

## Requirements

- Python 3.x
- `httpx` library
- `asyncio` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kn0x0x/brute-force-md5.git
    ```

2. Install the required dependencies:
    ```bash
    pip install httpx
    ```

## Usage

1. Update the `base_url` in the `main()` function to point to the server you are trying to solve.
2. Run the script:
    ```bash
    python3 solve.py
    ```

The script will brute-force the MD5 hash of the flag by sending asynchronous requests to the server. Once the MD5 hash is fully constructed, it will attempt to fetch the flag.

## Notes

- This script uses the `httpx` library to send HTTP GET requests asynchronously to improve speed.
- It brute-forces each character of the MD5 hash and then appends the `flag.txt` path to retrieve the flag once the hash is fully discovered.
  

