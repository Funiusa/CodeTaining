#!/bin/python3
import ipaddress
import os.path
import sys
import re

DEFAULT_INTERNAL_SUBNETS = ['10.254.196.0/24', ]
DEFAULT_EXTERNAL_SUBNETS = ['87.250.247.0/24', ]
INTERNAL_SUBNETS_FILE = 'internal_subnets.txt'
EXTERNAL_SUBNETS_FILE = 'external_subnets.txt'

ip_subnets = {"internal": [], "external": [], }


def configure_subnets():
    if os.path.exists(INTERNAL_SUBNETS_FILE):
        with open(INTERNAL_SUBNETS_FILE) as file:
            for int_subnets in file.readlines():
                ip_subnets["internal"].append(int_subnets.strip())
    if os.path.exists(EXTERNAL_SUBNETS_FILE):
        with open(EXTERNAL_SUBNETS_FILE) as file:
            for ext_subnets in file.readlines():
                ip_subnets["external"].append(ext_subnets.strip())

    if not len(ip_subnets["internal"]):
        ip_subnets["internal"].extend(DEFAULT_INTERNAL_SUBNETS)
    if not len(ip_subnets["external"]):
        ip_subnets["external"].extend(DEFAULT_EXTERNAL_SUBNETS)


def get_ip_subnet_type(ip):
    subnet_type = 'unknown'
    ip_obj = ipaddress.ip_address(ip)
    if ip_obj.is_private or ipaddress.ip_network(ip) in ip_subnets["internal"]:
        subnet_type = 'internal'
    if ip_obj.is_global or ipaddress.ip_network(ip) in ip_subnets["external"]:
        subnet_type = 'external'
    return subnet_type


def main():
    configure_subnets()

    for line in sys.stdin:
        ip_a = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", line).group(0)
        subnet_type = get_ip_subnet_type(ip_a)
        print(line.strip(), subnet_type)


if __name__ == "__main__":
    main()
