strs = ["flower","flow","flight"]
mini, maxi = min(strs), max(strs)

for i in range(len(mini)):
    if mini[i] != maxi[i]:
        x = mini[:i]
print(mini)
# len_strs = 0
# for i in strs:
#     len_strs = len_strs+1
# short = 0
# x = 0
# i = 0
# while i+1 < 3:
#     if len(strs[x]) >= len(strs[i+1]):
#         short = len(strs[i+1])
#     else:
#         short = len(strs[x])
#     x = x + 1
#     i = i + 1
# same = strs[0]
# final = []
# g = 0
# while g < len_strs-1:
#     q = 0
#     while q < short:
#         str1 = strs[g+1]
#         if same[q] == str1[q]:
#             final.append(same[q])
#         else:
#             break
#         q = q + 1
#
#     same = ''.join(final)
#     final = []
#     short = len(same)
#     g = g + 1
#
# print(same)






