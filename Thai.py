#REf: https://codebeautify.org/string-hex-converter
hex1 = ""
ll = []
counter = 0
h1 = "\\x{0"
t1 = "}\\s*"
msg = ""

for x in hex1:
    if x == "e":
        msg = h1+x.upper()
        counter += 1
    elif counter == 2:
        msg = msg+x.upper()+t1
        ll.append(msg)
        counter = 0
    else:
        msg = msg+x
        counter += 1
        
for y in ll:
    print(y, end="")
