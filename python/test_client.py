#! /usr/bin/env python3

import sys
import requests
import time

def send_req(req):
    try:
        response = requests.get(req)
        print(response.json())
    except requests.exceptions.ConnectionError:
        pass

def main(args=None):
    send_req("http://127.0.0.1:8888/")

    try:
        while (True):
            inp = input("Choose one[start/stop]: ")

            if (inp == "start"):
                send_req("http://127.0.0.1:8888/start_capturing")
            elif(inp == "stop"):
                send_req("http://127.0.0.1:8888/stop_capturing")
            else:
                print("\nBad Command!\n")

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main(sys.argv)