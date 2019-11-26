#!/usr/bin/env python3.7

import requests
import hashlib

if __name__ == '__main__':

    SECRET     = "s3cr3t"
    ADMIN_PASS = "b5ec168843f71c6f6c30808c78b9f55d"
    url = 'http://66.172.33.148:8008/protected_area_0098'
    p = hashlib.md5((ADMIN_PASS + SECRET).encode("utf-8")).hexdigest()
    print(p)
    r = requests.get(url, headers={"ah": p})
    print(r.text)

