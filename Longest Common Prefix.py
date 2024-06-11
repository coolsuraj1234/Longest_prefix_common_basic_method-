strs = ["flower","flow","flight"]
len_strs = 0
for i in strs:
    len_strs = len_strs+1
    
short = min(len(s) for s in strs)

same = strs[0]
final = []
g = 0

while g < len_strs-1:
    q = 0
    while q < short:
        str1 = strs[g+1]
        if same[q] == str1[q]:
            final.append(same[q])
        else:
            break
        q = q + 1

    same = ''.join(final)
    final = []
    short = len(same)
    g = g + 1

print(same)






