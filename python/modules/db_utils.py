import hashlib
import sqlite3

def __psswd2hash(psswd):
    h = hashlib.new("sha512", bytes(psswd, "utf-8"))

    return str(h.hexdigest())

def login_ok(user, psswd):
    psswd_hash = __psswd2hash(psswd)

    # Get a list with all users named "user" and compare
    # all its hashes with "psswd_hash"
    conn = sqlite3.connect('../db/ip_camera.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT psswd FROM users WHERE user_name=?", (user,))
    rows = cursor.fetchall()

    if(len(rows) == 0):
        return False

    found = False
    for r in rows:
        if (psswd_hash == r[0]):
            found = True
            break

    return found