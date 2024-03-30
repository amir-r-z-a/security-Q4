import sys, subprocess
text = "hello my brother"
target = "188.209.75.42"
if len(text)>16:
    print("Text too long!")
    exit()
enctext = r''.join( hex(ord(c)).split("x")[1] for c in text )
ping_count = 10
print(enctext)
for _ in range(ping_count):
    out = subprocess.check_output(["ping", "-p", enctext, "-c", "1", target])
    print(out)