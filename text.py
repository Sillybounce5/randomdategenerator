import sys
import time
def sprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
def sprintpro(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
def sprintultra(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
def sprintultradash(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
       # time.sleep(0.0000)
def slowsprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)
def sprinp(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)
def sprintproe(s,r):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    for c in str(r):
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
