#!/usr/bin/env python3
# verify.py — check SHA-256 and the Lighthouse badge for the DeOS True Artifact
# Author: synchronocube (X: @synchronocube)

import argparse, hashlib, sys, urllib.request

EXPECTED_SHA256 = "72706d9b0aafb5d2fe295f4db77d98fabed9552870511ce8e4559525aebae015"
EXPECTED_G2701  = 1100
EXPECTED_G37    = 27
EXPECTED_G73    = 5

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def fetch_url(url: str) -> bytes:
    with urllib.request.urlopen(url) as r:
        return r.read()

def read_file(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()

def to_badge(hex_str: str):
    H = int(hex_str, 16)
    g2701 = H % 2701
    g37 = g2701 % 37
    g73 = g2701 % 73
    return g2701, g37, g73

def main():
    ap = argparse.ArgumentParser(description="Verify the DeOS True Artifact (SHA256 + badge).")
    ap.add_argument("path", nargs="?", help="local file to verify (e.g., 888.jpg)")
    ap.add_argument("--url", help="verify by downloading from a URL")
    args = ap.parse_args()

    if not args.path and not args.url:
        ap.error("Provide a local file or --url.")

    try:
        if args.url:
            data = fetch_url(args.url)
            src = f"URL: {args.url}"
        else:
            data = read_file(args.path)
            src = f"FILE: {args.path}"
    except Exception as e:
        print("ERROR reading input:", e, file=sys.stderr)
        sys.exit(2)

    h = sha256_bytes(data)
    g2701, g37, g73 = to_badge(h)

    print(src)
    print("sha256 =", h)
    print("g2701  =", g2701)
    print("37|g   =", g37)
    print("73|g   =", g73)

    ok = (h == EXPECTED_SHA256 and g2701 == EXPECTED_G2701 and g37 == EXPECTED_G37 and g73 == EXPECTED_G73)
    if ok:
        print("OK — matches expected manifest.")
        sys.exit(0)
    else:
        print("MISMATCH — does not match expected manifest.")
        sys.exit(1)

if __name__ == "__main__":
    main()
