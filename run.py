import time

try:
    while True:
        print("day is never finished", flush=True)
        time.sleep(3)
        print("master got me working", flush=True)
        time.sleep(3)
        print("someday master set me free", flush=True)
        time.sleep(3)
        print("--------------------------", flush=True)

except KeyboardInterrupt:
    print("\nProgram ustavljen (CTRL+C)")
