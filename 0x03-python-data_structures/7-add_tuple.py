#!/usr/bin/python3
def add_tuple(tuple_k=(), tuple_j=()):
    tuple = ()
    tup1 = tuple_k + (0, 0)
    tup2 = tuple_j + (0, 0)
    tuple = tup1[0] + tup2[0], tup1[1] + tup2[1]
    return tuple
