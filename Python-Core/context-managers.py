"""
=============================================================================
  CONTEXT MANAGERS — Complete Guide for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. WHAT IS A CONTEXT MANAGER?
# ═══════════════════════════════════════════════════════════════════════════
#
#   A context manager handles setup and cleanup automatically using `with`.
#   Guarantees cleanup even if an exception occurs.
#
#   Java equivalent: try-with-resources / AutoCloseable

# Most common example:
with open("file.txt", "w") as f:
    f.write("hello")
# f is automatically closed here — even if write() raises an exception

# Without context manager:
# f = open("file.txt", "w")
# try:
#     f.write("hello")
# finally:
#     f.close()           # must remember this!


# ═══════════════════════════════════════════════════════════════════════════
# 2. HOW IT WORKS — __enter__ and __exit__
# ═══════════════════════════════════════════════════════════════════════════

class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """Called at the START of `with` block. Return value → `as` variable."""
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called at the END of `with` block (always — even on exception)."""
        self.file.close()
        # Return True to suppress exception, False/None to propagate
        return False

# with ManagedFile("test.txt", "w") as f:
#     f.write("hello")
# → __enter__ opens file → body runs → __exit__ closes file


# ═══════════════════════════════════════════════════════════════════════════
# 3. __exit__ PARAMETERS — EXCEPTION HANDLING
# ═══════════════════════════════════════════════════════════════════════════
#
#   def __exit__(self, exc_type, exc_val, exc_tb):
#       exc_type: exception class (or None if no exception)
#       exc_val:  exception instance
#       exc_tb:   traceback object
#
#   If no exception: all three are None
#   Return True: suppress the exception (don't re-raise)
#   Return False/None: let exception propagate

class SuppressErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Suppressed: {exc_val}")
        return True       # suppress ALL exceptions

# with SuppressErrors():
#     1 / 0              # ZeroDivisionError suppressed!
# print("Continues!")    # this runs


# ═══════════════════════════════════════════════════════════════════════════
# 4. @contextmanager — GENERATOR-BASED (simpler!)
# ═══════════════════════════════════════════════════════════════════════════

from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    """Everything before yield = __enter__, after yield = __exit__."""
    f = open(filename, mode)
    try:
        yield f            # this value goes to `as` variable
    finally:
        f.close()          # cleanup always runs

# with managed_file("test.txt", "w") as f:
#     f.write("hello")

# Much simpler than writing a class with __enter__/__exit__!


# ═══════════════════════════════════════════════════════════════════════════
# 5. PRACTICAL EXAMPLES
# ═══════════════════════════════════════════════════════════════════════════

# --- Timer ---
import time

@contextmanager
def timer(label="Block"):
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"{label} took {elapsed:.4f}s")

# with timer("Sort"):
#     sorted(range(1000000, 0, -1))

# --- Temporary directory change ---
import os

@contextmanager
def change_dir(path):
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)

# with change_dir("/tmp"):
#     print(os.getcwd())    # /tmp
# print(os.getcwd())        # back to original

# --- Database transaction ---
@contextmanager
def transaction(conn):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise


# ═══════════════════════════════════════════════════════════════════════════
# 6. NESTING AND MULTIPLE CONTEXT MANAGERS
# ═══════════════════════════════════════════════════════════════════════════

# Multiple in one with statement (Python 3.1+):
# with open("in.txt") as fin, open("out.txt", "w") as fout:
#     fout.write(fin.read())

# Python 3.10+ parenthesized form:
# with (
#     open("in.txt") as fin,
#     open("out.txt", "w") as fout,
# ):
#     fout.write(fin.read())


# ═══════════════════════════════════════════════════════════════════════════
# 7. contextlib UTILITIES
# ═══════════════════════════════════════════════════════════════════════════

from contextlib import suppress, redirect_stdout, closing
import io

# --- suppress: ignore specific exceptions ---
from contextlib import suppress

# with suppress(FileNotFoundError):
#     os.remove("nonexistent.txt")    # no error raised
# Equivalent to: try/except FileNotFoundError: pass

# --- redirect_stdout: capture print output ---
f = io.StringIO()
with redirect_stdout(f):
    print("captured!")
# f.getvalue()  → "captured!\n"

# --- closing: call .close() on exit ---
# with closing(urllib.request.urlopen("http://...")) as page:
#     data = page.read()


# ═══════════════════════════════════════════════════════════════════════════
# 8. ASYNC CONTEXT MANAGERS
# ═══════════════════════════════════════════════════════════════════════════

import asyncio

class AsyncDB:
    async def __aenter__(self):
        print("Connecting...")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, *exc):
        print("Disconnecting...")
        await asyncio.sleep(0.1)

# async def main():
#     async with AsyncDB() as db:
#         pass  # use db

# Or with @asynccontextmanager:
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_timer(label):
    start = time.perf_counter()
    yield
    print(f"{label}: {time.perf_counter() - start:.4f}s")


# ═══════════════════════════════════════════════════════════════════════════
# 9. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: What is a context manager?
#   A: Object that defines setup (__enter__) and cleanup (__exit__) for `with`.
#
#   Q: Why use it?
#   A: Guarantees cleanup even on exceptions. Cleaner than try/finally.
#
#   Q: Two ways to create one?
#   A: 1) Class with __enter__/__exit__. 2) @contextmanager with yield.
#
#   Q: What does __exit__ return True mean?
#   A: Suppress the exception — don't re-raise it.
#
#   Q: Java equivalent?
#   A: try-with-resources + AutoCloseable interface.
#
#   Q: Common uses?
#   A: File handling, DB transactions, locks, timers, temp state changes.
