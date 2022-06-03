#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_list = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(num_list, "" if num_list == 1 else "s", "." if num_list == 0 else ":"))
    for i in range(num_list):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
