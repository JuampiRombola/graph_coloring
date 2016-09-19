def myhash(s):
    h = 3722
    for c in s:
        h += ord(c) ** 3
        h ^= h >> 5
    h ^= h >> 5
    return h