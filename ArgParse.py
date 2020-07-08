#!/usr/bin/python3
import argparse
import requests


def main():
    if args.ip:
        ipToLookup = args.ip 
    else:
        ipToLookup = input("What is the IP address to lookup?")
    
    zresp = requests.get(f'http://ip=api.com/json/{ipToLookup}')
    print(zresp.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="The IP address to lookup via the API service")

    args = parser.parse_args()
    main()