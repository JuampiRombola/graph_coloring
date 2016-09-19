def myhash(s):
    h = 3722
    largo = len(s)
    for c in s:
        h += (ord(c) - largo/20) ** 3 
        h ^= h >> 5
    h ^= h >> 5
    return h