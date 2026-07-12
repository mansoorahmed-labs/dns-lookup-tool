#!/usr/bin/env python3

import socket
import dns.resolver

def resolve_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n[+] IPv4 Address : {ip}")
    except socket.gaierror:
        print("\n[-] Unable to resolve IP address.")

def get_dns_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        print(f"\n{record_type} Records:")
        for answer in answers:
            print(f"  - {answer}")
    except Exception:
        print(f"\nNo {record_type} records found.")

def main():
    print("=" * 50)
    print("          DNS Lookup Tool")
    print("=" * 50)

    domain = input("Enter a domain (example.com): ").strip()

    print(f"\nScanning DNS records for: {domain}")

    resolve_ip(domain)

    record_types = ["A", "AAAA", "MX", "NS", "CNAME"]

    for record in record_types:
        get_dns_records(domain, record)

    print("\nScan Completed.")

if __name__ == "__main__":
    main()
