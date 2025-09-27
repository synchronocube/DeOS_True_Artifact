# VERIFY — DeOS True Artifact

This guide offers three ways to verify the artifact.

---

## A) Verify straight from IPFS (no download)

1. Open a terminal (Mac/Linux: Terminal; Windows: PowerShell).
2. Run:

```bash
python3 verify.py --url https://ipfs.io/ipfs/bafybeibr6735o3hcjdvic4jbmodezkjppviphnv5gjv5y74q2flqmviw6m
```

You should see:

```
sha256 = 72706d9b0aafb5d2fe295f4db77d98fabed9552870511ce8e4559525aebae015
g2701  = 1100
37|g   = 27
73|g   = 5
OK — matches expected manifest.
```

If the first gateway is slow, try Cloudflare:

```bash
python3 verify.py --url https://cloudflare-ipfs.com/ipfs/bafybeibr6735o3hcjdvic4jbmodezkjppviphnv5gjv5y74q2flqmviw6m
```

---

## B) Verify a local file you downloaded

1. Save the image locally (any filename is fine, e.g. `888.jpg`).
2. Run:

```bash
python3 verify.py 888.jpg
```

Expect the same values as above.

---

## C) iPhone‑only (no Python)

1. Use the Shortcuts app:
   - Create a shortcut: **Get File** → **Hash** (SHA‑256) → **Show Result**.
   - Pick the image file.
2. Compute the badge on a website (any static page that converts hex→int
   and shows `mod 2701`, then `mod 37` and `mod 73`).

Expected:
- SHA‑256 = `72706d9b0aafb5d2fe295f4db77d98fabed9552870511ce8e4559525aebae015`
- `g2701 = 1100`
- `37|g = 27`
- `73|g = 5`

---

### How the badge works

```
H = int(sha256(bytes), 16)
g2701 = H % 2701
g37   = g2701 % 37
g73   = g2701 % 73
```

The badge is a compact “spoken checksum” that travels well in human
channels while still being rooted in the full SHA‑256.
