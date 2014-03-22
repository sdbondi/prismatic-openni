import os, sys

import argparse

from prismatic import viewer as pris_viewer

def get_lib_path(lib):
    cwd = os.path.dirname(__file__)
    return os.path.join(cwd, 'lib/%s/%s/' % (sys.platform, lib))

def parse_args(args):
    parser = argparse.ArgumentParser()

    # Add arguments here
    parser.add_argument('--openni2_libs', default=get_lib_path('OpenNI2'))
    parser.add_argument('--nite2_libs', default=get_lib_path('NiTE2'))
    return parser.parse_args(args)

def main(args):
    args = parse_args(args)

    viewer = pris_viewer.Window()
    if not viewer.initialize(openni2_path=args.openni2_libs, nite2_path=args.nite2_libs):
        raise "Viewer failed to initialize!"

    viewer.run()


if __name__ == '__main__':
    main(sys.argv[1:])
