#!/usr/bin/env python3

import sys
import subprocess
import socket
import re
from termcolor import colored
from tabulate import tabulate

def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, text=True).strip()
        return result
    except subprocess.CalledProcessError:
        return ""

def get_ip(subdomain):
    output = run_command(f"host {subdomain}")
    match = re.search(r'has address (\d+\.\d+\.\d+\.\d+)', output)
    return match.group(1) if match else None

def get_domain_pointer(ip):
    output = run_command(f"host {ip}")
    match = re.search(r'domain name pointer ([^\s]+)\.', output)
    return match.group(1) if match else None

def get_whois_fields(ip):
    output = run_command(f"whois {ip}")
    orgname = ""
    organization = ""
    for line in output.splitlines():
        if not orgname and re.search(r'^OrgName\s*:', line, re.IGNORECASE):
            orgname = line.split(":", 1)[1].strip()
        elif not organization and re.search(r'^Organization\s*:', line, re.IGNORECASE):
            organization = line.split(":", 1)[1].strip()
        if orgname and organization:
            break
    return orgname, organization

def main():
    if len(sys.argv) != 2:
        print(colored("Usage: python3 script.py <subdomain_list.txt>", "red"))
        sys.exit(1)

    input_file = sys.argv[1]
    results = []

    with open(input_file, 'r') as f:
        for line in f:
            subdomain = line.strip()
            if not subdomain:
                continue

            ip = get_ip(subdomain)
            if not ip:
                results.append([subdomain, "N/A", "N/A", "N/A", "N/A"])
                continue

            domain_pointer = get_domain_pointer(ip) or "N/A"
            orgname, organization = get_whois_fields(ip)
            results.append([subdomain, ip, domain_pointer, orgname or "N/A", organization or "N/A"])

    headers = [colored("Subdomain", "red"),
               colored("IP Address", "green"),
               colored("Domain Pointer", "yellow"),
               colored("OrgName", "cyan"),
               colored("Organization", "magenta")]

    print(tabulate(results, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
    