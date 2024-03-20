#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum0 = 0
    for i in range(len(sys.argv) - 1):
        sum0 += int(sys.argv[i + 1])
    print("{}".format(sum0))
