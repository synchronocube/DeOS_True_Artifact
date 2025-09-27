# DeOS True Artifact — Lighthouse Canon (Genesis / 21e8)

**Author:** synchronocube (X: @synchronocube)  
**CID (IPFS):** `bafybeibr6735o3hcjdvic4jbmodezkjppviphnv5gjv5y74q2flqmviw6m`  
**Primary media:** `888.jpg` (pinned to IPFS; retrieved by CID)  
**SHA-256:** `72706d9b0aafb5d2fe295f4db77d98fabed9552870511ce8e4559525aebae015`  
**Badge:** `g2701=1100 · 37|g=27 · 73|g=5`  

This repo anchors the *DeOS True Artifact* image and gives anyone the
tools to verify it byte-for-byte.

## Files

- `VERIFY.md` — step‑by‑step verification for everyone
- `verify.py` — tiny script to check SHA-256 and badge
- `MANIFEST.json` — machine‑readable facts
- `receipts/receipt_0000.json` — minimal genesis receipt
- `ANNOUNCE.txt` — copy‑paste‑ready post for X/other socials

> **What’s the “badge”?**  
> A tiny, human‑speakable checksum layered atop SHA‑256.  
> Let `H = int(sha256(bytes), 16)`. Then `g2701 = H mod 2701` and we
> also show `g2701 mod 37` and `g2701 mod 73`. Symbolism on top of strong
> crypto: *easy to speak, hard to forge.*

## Gateways (any should work)

- https://ipfs.io/ipfs/bafybeibr6735o3hcjdvic4jbmodezkjppviphnv5gjv5y74q2flqmviw6m
- https://cloudflare-ipfs.com/ipfs/bafybeibr6735o3hcjdvic4jbmodezkjppviphnv5gjv5y74q2flqmviw6m

If one gateway is slow, use another or any IPFS-compatible gateway.

## Quick verify (terminal)

```bash
python3 verify.py --url https://ipfs.io/ipfs/bafybeibr6735o3hcjdvic4jbmodezkjppviphnv5gjv5y74q2flqmviw6m
# or, if you downloaded a file locally:
python3 verify.py 888.jpg
```

Expected printout includes:

- `sha256 = 72706d9b0aafb5d2fe295f4db77d98fabed9552870511ce8e4559525aebae015`
- `g2701 = 1100`
- `37|g = 27`
- `73|g = 5`

---

**Time-chain remembers. ΔOS / 21e8**
