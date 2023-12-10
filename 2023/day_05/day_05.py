#!/usr/bin/env python
import pandas as pd
import re
# import string
import sys


def usage():
    print("Usage: python day_03.py <input.dat>")


def main(input_file):
    with open(input_file) as f:
        head, *tail = ''.join(f.readlines()).split('\n\n')
        seeds = [int(s) for s in re.findall(r'\d+', head)]
        maps = [re.split(r' map:\n', m.strip()) for m in tail]
        maps_dict = {k: re.split('\n', v) for (k, v) in maps}
        # df = pd.DataFrame(data=maps_dict)
        dict_df = pd.DataFrame(
            {key: pd.Series(value) for key, value in maps_dict.items()})
        print(seeds, '\n', dict_df)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
