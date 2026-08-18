"""
=============================================================================
  ASYNC, THREADING & MULTIPROCESSING — Complete Guide for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. THE BIG PICTURE — WHEN TO USE WHAT
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Task Type    | Problem              | Solution              | Why                      |
#   |--------------|----------------------|-----------------------|--------------------------|
#   | I/O-bound    | Network, file, DB    | asyncio / threading   | Waiting, not computing   |
#   | CPU-bound    | Math, processing     | multiprocessing       | Need true parallelism    |
#   | Simple I/O   | Few concurrent tasks | threading             | Simpler than asyncio     |
#   | Many I/O     | 1000s of connections | asyncio               | Scales better than threads|
#
#   KEY: Python's GIL prevents threads from running CPU code in parallel.
#        But GIL is released during I/O → threads work fine for I/O.


# ═══════════════════════════════════════════════════════════════════════════
# 2. THREADING — CONCURRENT (not parallel)
# ═══════════════════════════════════════════════════════════════════════════

import threading
import time

def download(url):
    print(f"Downloading {url}...")
    time.sleep(2)                      # simulates I/O wait
    print(f"Done: {url}")

# Sequential: 6 seconds total
# download("url1"); download("url2"); download("url3")

# Threaded: ~2 seconds total (all wait concurrently)
threads = []
for url in ["url1", "url2", "url3"]:
    t = threading.Thread(target=download, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()           # wait for all threads to finish


# ═══════════════════════════════════════════════════════════════════════════
# 3. THREAD SAFETY — LOCKS
# ═══════════════════════════════════════════════════════════════════════════

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:                     # acquire → release automatically
            counter += 1

# Without lock: counter might be < 200000 (race condition)
# With lock: always exactly 200000

# Other sync primitives:
# threading.RLock()       — reentrant lock (same thread can acquire multiple times)
# threading.Semaphore(n)  — allow up to n threads at once
# threading.Event()       — signal between threads
# threading.Condition()   — wait/notify pattern


# ═══════════════════════════════════════════════════════════════════════════
# 4. MULTIPROCESSING — TRUE PARALLELISM
# ═══════════════════════════════════════════════════════════════════════════

from multiprocessing import Process, Pool

def cpu_heavy(n):
    """Simulate CPU work."""
    return sum(i * i for i in range(n))

# --- Using Process ---
# p1 = Process(target=cpu_heavy, args=(10_000_000,))
# p2 = Process(target=cpu_heavy, args=(10_000_000,))
# p1.start(); p2.start()
# p1.join(); p2.join()

# --- Using Pool (easier for map-style work) ---
# with Pool(4) as pool:
#     results = pool.map(cpu_heavy, [10_000_000] * 4)

# Each process has its OWN Python interpreter → no GIL issue
# Trade-off: more memory, slower to start, can't share state easily


# ═══════════════════════════════════════════════════════════════════════════
# 5. concurrent.futures — HIGH-LEVEL API (recommended)
# ═══════════════════════════════════════════════════════════════════════════

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# --- Thread pool for I/O ---
def fetch(url):
    time.sleep(1)
    return f"Result from {url}"

# with ThreadPoolExecutor(max_workers=5) as executor:
#     futures = [executor.submit(fetch, f"url{i}") for i in range(5)]
#     for f in futures:
#         print(f.result())      # blocks until done

# --- Process pool for CPU ---
# with ProcessPoolExecutor(max_workers=4) as executor:
#     results = list(executor.map(cpu_heavy, [10**7] * 4))

# Why concurrent.futures is better:
# - Same API for threads and processes (just swap executor)
# - Built-in Future objects with .result(), .done(), .exception()
# - Automatic cleanup with context manager


# ═══════════════════════════════════════════════════════════════════════════
# 6. ASYNCIO — COOPERATIVE CONCURRENCY
# ═══════════════════════════════════════════════════════════════════════════

import asyncio

async def fetch_data(url, delay):
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)         # non-blocking sleep (yields control)
    return f"Data from {url}"

async def main():
    # Run tasks concurrently
    results = await asyncio.gather(
        fetch_data("api/users", 2),
        fetch_data("api/posts", 1),
        fetch_data("api/comments", 3),
    )
    # All 3 run concurrently → total time ≈ 3 seconds (not 6)
    return results

# asyncio.run(main())

# Key concepts:
#   async def  → declares a coroutine
#   await      → pause here, let other tasks run
#   asyncio.gather() → run multiple coroutines concurrently
#   asyncio.run()    → entry point (starts event loop)


# ═══════════════════════════════════════════════════════════════════════════
# 7. ASYNCIO PATTERNS
# ═══════════════════════════════════════════════════════════════════════════

# --- Task creation ---
async def pattern_example():
    # Create task (starts immediately)
    task = asyncio.create_task(fetch_data("url", 1))
    # Do other work here...
    result = await task      # get result when needed

# --- Timeout ---
async def with_timeout():
    try:
        result = await asyncio.wait_for(
            fetch_data("slow_api", 10),
            timeout=5.0
        )
    except asyncio.TimeoutError:
        print("Timed out!")

# --- Semaphore (limit concurrency) ---
async def limited_concurrency():
    sem = asyncio.Semaphore(3)         # max 3 concurrent

    async def limited_fetch(url):
        async with sem:
            return await fetch_data(url, 1)

    tasks = [limited_fetch(f"url{i}") for i in range(10)]
    return await asyncio.gather(*tasks)


# ═══════════════════════════════════════════════════════════════════════════
# 8. THREADING vs ASYNCIO vs MULTIPROCESSING
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Feature            | Threading         | Asyncio            | Multiprocessing    |
#   |--------------------|-------------------|--------------------|--------------------|
#   | Parallelism?       | No (GIL)          | No (single thread) | Yes (separate PIDs)|
#   | Best for           | I/O-bound         | I/O-bound (many)   | CPU-bound          |
#   | Memory             | Shared             | Shared             | Separate (copied)  |
#   | Overhead           | Medium             | Low                | High               |
#   | Scalability        | ~100s threads      | ~10,000s tasks     | ~CPU cores         |
#   | Sync mechanism     | Locks              | await              | Queues/Pipes       |
#   | Preemptive?        | Yes (OS switches)  | No (cooperative)   | Yes (OS)           |
#   | Race conditions?   | Yes                | Rare (single thrd) | No (separate mem)  |


# ═══════════════════════════════════════════════════════════════════════════
# 9. GIL — DEEPER UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════
#
#   What: Global Interpreter Lock — mutex in CPython
#   Why: Protects CPython's memory management (reference counting)
#   Effect: Only ONE thread executes Python bytecode at a time
#
#   GIL is RELEASED during:
#   - I/O operations (file, network, sleep)
#   - C extensions (numpy operations)
#   - Waiting on locks
#
#   GIL is HELD during:
#   - Pure Python computation
#   - Object creation/destruction
#
#   Solutions for CPU parallelism:
#   1. multiprocessing — separate processes, each with own GIL
#   2. C extensions — numpy releases GIL for array operations
#   3. Cython / C — write critical code in C
#   4. Python 3.13+ — experimental free-threaded mode (no GIL)


# ═══════════════════════════════════════════════════════════════════════════
# 10. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: What's the GIL?
#   A: CPython lock allowing only one thread to run Python bytecode at a time.
#
#   Q: How to achieve true parallelism?
#   A: multiprocessing (separate processes, each with own GIL).
#
#   Q: Threading vs asyncio?
#   A: Threading = preemptive (OS switches), asyncio = cooperative (you yield).
#      Asyncio scales better (10000s tasks vs 100s threads).
#
#   Q: When do threads help despite GIL?
#   A: I/O-bound tasks — GIL released during I/O waits.
#
#   Q: What's async/await?
#   A: async def = coroutine. await = suspend here, let others run.
#
#   Q: What's a race condition?
#   A: Two threads modify shared state simultaneously → corrupted data.
#      Fix: use locks, or use asyncio (single-threaded).
#
#   Q: concurrent.futures advantage?
#   A: Same API for threads and processes. Just swap the executor class.
