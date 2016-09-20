def myhash(s):
    h = 3722
    oper = (len(s)-7)/13
    for c in s:
        h += (ord(c) - oper/13) ** 3 + oper * 3
        h ^= h >> 5
    h ^= h >> 5
    return h
