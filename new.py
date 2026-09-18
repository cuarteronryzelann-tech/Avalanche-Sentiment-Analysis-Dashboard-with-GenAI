target = "REBANZXYLL"
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
attempt = 0
found = False

def brute(current):
    global attempt, found

    if len(current) == len(target):
        attempt += 1
        if current == target:
            print(f"✅ Password found: {current}")
            print(f"Attempts: {attempt:,}")
            found = True
        return

    for char in chars:
        if found:
            return
        brute(current + char)

brute("")

if not found:
    print("❌ Password not found.")