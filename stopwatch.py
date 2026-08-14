import time

start = input("Press ENTER to start...")
start_time = time.time()

input("Press ENTER to stop...")

elapsed = time.time() - start_time

minutes = int(elapsed // 60)
seconds = int(elapsed % 60)
milliseconds = int((elapsed % 1) * 1000)

print(
    f"Time: {minutes:02d}:"
    f"{seconds:02d}."
    f"{milliseconds:03d}"
)