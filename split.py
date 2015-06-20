#!/usr/bin/env python
# $Id: split.py,v 2.2 2004/07/17 11:09:18 zeller Exp $

def split(data, n):
    list = []
    nextline = '\n'

    if len(data) == 0:
        return []

    data = data.splitlines()

    length=int(len(data)/n)

    if length == 0:
        #assert length > 0
        return []

    start = 0
    for i in range(0, n):
        list.append(nextline.join(data[start:start+length]))
        start = start+length

    return list

