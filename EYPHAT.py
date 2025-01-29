#!/usr/bin/env python3
# ▄︻̷̿┻̿═━一  (x_x)  craxterpy/Rip70022 EDITION  (⌐■_■) ︻デ═一 - - - [EYPHAT V0.1]

"""
███████╗██╗░░░██╗██████╗░██╗░░██╗░█████╗░████████╗  █▀▀ █▀█ █▀█ █▄▀ █ █▄░█ █▀▀
██╔════╝╚██╗░██╔╝██╔══██╗██║░░██║██╔══██╗╚══██╔══╝  █▄▄ █▄█ █▄█ █░█ █ █░▀█ █▄█
█████╗░░░╚████╔╝░██████╔╝███████║███████║░░░██║░░░  
██╔══╝░░░░╚██╔╝░░██╔═══╝░██╔══██║██╔══██║░░░██║░░░   V0.1
███████╗░░░██║░░░██║░░░░░██║░░██║██║░░██║░░░██║░░░ 
╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  
"""

import os
import sys
import argparse
import zipfile
import itertools
import string
import time
import multiprocessing
from threading import Thread
from queue import Queue
from PyPDF2 import PdfFileReader
import pyzipper

# ░██████╗██╗░░██╗░█████╗░██████╗░███████╗██████╗░░██████╗
# ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
# ╚█████╗░███████║███████║██████╔╝█████╗░░██████╔╝╚█████╗░
# ░╚═══██╗██╔══██║██╔══██║██╔═══╝░██╔══╝░░██╔══██╗░╚═══██╗
# ██████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║██████╔╝
# ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░

class NuclearOption:
    def __init__(self):
        self.found = False
        self.queue = Queue()
        self.total_attempts = 0
        self.start_time = time.time()

    def print_banner(self):
        banner = r"""
        ██████╗░██╗░░░██╗██████╗░███████╗██████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
        ██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
        ██████╔╝░╚████╔╝░██████╔╝█████╗░░██████╔╝  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
        ██╔═══╝░░░╚██╔╝░░██╔═══╝░██╔══╝░░██╔══██╗  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
        ██║░░░░░░░░██║░░░██║░░░░░███████╗██║░░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
        ╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
        """
        print(banner)
        print("[+] Initializing Tachyon Breach Protocol...")
        print(f"[*] PID {os.getpid()} engaged at {time.ctime()}")
        print("[!] Warning: HELLO SIR\n")

    def build_warhead(self, min_len=1, max_len=8, charset=None):
        charset = charset or string.printable.strip()
        print(f"[+] Constructing payload matrix: {min_len}-{max_len} chars from {len(charset)} unique particles")
        for length in range(min_len, max_len + 1):
            for candidate in itertools.product(charset, repeat=length):
                yield ''.join(candidate)

    def zip_crack(self, filename, password):
        try:
            with pyzipper.AESZipFile(filename) as zf:
                zf.extractall(pwd=password.encode())
            return password
        except (RuntimeError, zipfile.BadZipFile):
            return False

    def pdf_crack(self, filename, password):
        try:
            with open(filename, 'rb') as f:
                pdf = PdfFileReader(f)
                if pdf.decrypt(password):
                    return password
        except Exception as e:
            return False

    def txt_crack(self, filename, password):
        try:
            with open(filename, 'r') as f:
                content = f.read()
                if password in content:  # Placeholder for actual encryption logic
                    return password
        except:
            return False

    def quantum_worker(self, target, attack_func):
        while not self.queue.empty() and not self.found:
            password = self.queue.get()
            self.total_attempts += 1
            if self.total_attempts % 1000 == 0:
                self.print_stats()
            result = attack_func(target, password)
            if result:
                self.found = result
                print(f"\n[+] Critical hit! Decryption key found: {result}")
                print(f"[!] Total attempts: {self.total_attempts}")
                print(f"[!] Time elapsed: {time.time() - self.start_time:.2f}s")
                sys.exit(0)

    def print_stats(self):
        print(f"[~] Attempts: {self.total_attempts} | Elapsed: {time.time() - self.start_time:.2f}s | Queue: {self.queue.qsize()}")

    def launch_sequence(self):
        parser = argparse.ArgumentParser(description="Project Craxterbomb - File Encryption Breach Toolkit")
        parser.add_argument("target", help="Target file path")
        parser.add_argument("-m", "--mode", choices=['brute', 'dict'], required=True)
        parser.add_argument("-t", "--threads", type=int, default=os.cpu_count())
        parser.add_argument("-min", "--min-length", type=int, default=1)
        parser.add_argument("-max", "--max-length", type=int, default=8)
        parser.add_argument("-c", "--charset", default=string.printable.strip())
        parser.add_argument("-d", "--dict", help="Dictionary file path")
        args = parser.parse_args()

        self.print_banner()
        print(f"[+] Target acquired: {args.target}")
        print(f"[+] Attack vector: {args.mode}")
        print(f"[+] Quantum threads engaged: {args.threads}")

        file_type = os.path.splitext(args.target)[1].lower()
        attack_func = {
            '.zip': self.zip_crack,
            '.pdf': self.pdf_crack,
            '.txt': self.txt_crack
        }.get(file_type, None)

        if not attack_func:
            print("[!] File type not recognized. Initiating protocol 0xDEADBEEF")
            sys.exit(1)

        if args.mode == 'brute':
            gen = self.build_warhead(args.min_length, args.max_length, args.charset)
            for pwd in gen:
                self.queue.put(pwd)
        else:
            if not args.dict:
                print("[!] Dictionary path required for dictionary attack")
                sys.exit(1)
            with open(args.dict, 'r', errors='ignore') as f:
                for line in f:
                    self.queue.put(line.strip())

        print("[+] Launching photon torpedoes...")
        threads = []
        for _ in range(args.threads):
            t = Thread(target=self.quantum_worker, args=(args.target, attack_func))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        if not self.found:
            print("[!] Target resisted decryption attempts. Recommend quantum annealing enhancement")

if __name__ == "__main__":
    NuclearOption().launch_sequence()

# you look rich, I NEED SOME bitcoin : bc1q5a7kufr98mgll8c39r2euln4xkrukkhanj4vuv - yeah i use Trust Wallet, what about it?
