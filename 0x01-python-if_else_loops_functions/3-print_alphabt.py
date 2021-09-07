for i in range(ord('a'), ord('z') + 1):
    if i == 101 or i == 113:
        continue
    print("{}".format(chr(i)), end="")
