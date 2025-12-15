#re.findall() is used to find ALL occurrences (matches) of a pattern in a string.

import re    
f=open("mailtext.txt","r")
for line in f:
    s=line.strip()#removes spaces in between the text
    reg=re.findall(r"[a-zA-Z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}",s)#r is used for '\' is not considering like escape sequences
    print(reg)