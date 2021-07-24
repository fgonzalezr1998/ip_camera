#! /usr/bin/env python3

import sys
import hashlib
import sqlite3

def psswd2hash(psswd):
    h = hashlib.new("sha512", bytes(psswd, "utf-8"))

    return h.hexdigest()

def save_on_db(user, psswd_hash):
    conn = sqlite3.connect('../db/ip_camera.sqlite3')

def main(args=None):
    # Get username:
    user = input("Introduce Username: ")

    # Get Password:
    psswd = input("Introduce Password: ")

    # Get Hashed Password (Hexadecimal)
    psswd_hash = psswd2hash(psswd)

    save_on_db(user, psswd_hash)

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)