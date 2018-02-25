import os
import glob
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({'font.size': 15})
    

def plot_comparison(paths, names):
    y_pos = np.arange(len(names))
    height = 1 / (len(paths) + 1)
    fig = plt.figure()
    fig.subplots_adjust(left=0.21)
    for k, path in enumerate(paths):
        sizes = [os.path.getsize(os.path.join(path, name+'.jpg')) for name in names]
        plt.barh(y_pos-k*height, sizes, height=height, align='edge', alpha=0.5, label=path)
    plt.yticks(y_pos, names)
    plt.xlabel('File size (KB)')
    plt.title('Images compression')
    plt.legend()
    plt.show()


def main(path):
    paths = os.listdir(path)
    if 'Icon\r' in paths:
        paths.remove('Icon\r')
    if 'images' in paths:
        paths.remove('images')
        original = os.path.join(path, 'images')
        originals = sorted(glob.glob(os.path.join(original, '*.jpg')))
        filenames = [os.path.basename(path) for path in originals]
        names = [os.path.splitext(filename)[0] for filename in filenames[10:20]]
        paths = [os.path.join(path, folder) for folder in paths]
        plot_comparison(paths, names)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', nargs='?', help='directory path to evaluate')
    args = parser.parse_args()

    if args.path is None:
        parser.print_help()
        sys.exit()

    main(args.path)
    
