def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    prefix = strs[0]
    for i in range(1,len(strs)):
        while len(prefix) != 0:
            if strs[i].find(prefix) == 0:
                break
            else:
                prefix = prefix[0:len(prefix) - 1]
    return prefix


print(longestCommonPrefix(["flower","flow","flight"]))
