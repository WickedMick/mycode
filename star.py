#!/usr/bin/env python3
rows = input("Enter number of stars")
rows = int(rows)
for i in range(1, rows):
    for j in range(1, i + 1):
        print("* ", end='')
        print("\r")
for i in range(rows, 1, -1):
    for j in range(1, i -1):
        print("* ", end='')
        print("\r")

