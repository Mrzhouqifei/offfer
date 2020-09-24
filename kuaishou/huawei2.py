import re

# key, strings = map(str, input().strip().split(' '))
strings = str(input())

res = re.findall("\[addr=(0[xX][0-9a-fA-F]{1,3}),mask=(0[xX][0-9a-fA-F]{1,3}),val=(0[xX][0-9a-fA-F]{1,3})\]", strings)
if len(res) == 0:
    print("FAIL")
else:
    pres = ""
    for addr, mask, val in res:
        pres += f"{addr} {mask} {val}\r\n"
    print(pres)