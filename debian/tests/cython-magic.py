import pexpect
import sys
c = pexpect.spawn(sys.argv[1])
c.expect(".*")
c.sendline("%load_ext cythonmagic")
c.sendline("%%cython")
c.sendline("cimport cython")
c.sendline("def f():")
c.sendline("    return 'RESULT STRING'")
c.sendline("")
c.expect(".*")
c.sendline("f()")
try:
    c.expect("RESULT STRING")
except:
    c.sendeof()
    c.sendeof()
    print c.before, c.after
    raise

c.sendeof()
c.sendeof()
import time
time.sleep(1)
if c.isalive():
    c.kill(0)
