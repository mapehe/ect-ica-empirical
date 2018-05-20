import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('ifile', metavar='ifile', type=str,
                    help='input file')
parser.add_argument('threshold', metavar='threshold', type=int,
                    help='threshold value (k_n)')
parser.add_argument('ww', metavar='window_width', type=int,
                    help='rolling window width')
parser.add_argument('ws', metavar='window_shift', type=int,
                    help='rolling window shift')


def hill(sample, k):
    k = min(k, len(sample))
    sample = sorted(sorted(np.array(sample), reverse=True)[:k])
    sample = np.log(sample)-np.log(sample[0])
    return np.mean(sample[1:])


def main():
    args = parser.parse_args()
    d = pd.DataFrame.from_csv(args.ifile)

    length = len(d["Date"])
    iters = int(np.floor((length-args.ww)/args.ws))
    print(iters)
    for i in range(iters):
        for key in d.keys():
            if(key.startswith("Series")):
                a = args.ws*i
                b = args.ww+args.ws*i
                print(hill(d[key][a:b],
                           args.threshold))


if __name__ == "__main__":
    main()
