#!/usr/bin/env python2

import os
import sys
import yaml
import tarfile


def usage():
    script_name = sys.argv[0]
    print 'Command $ {}'.format(' '.join(sys.argv))
    print 'Usage   $ {} <src_tar_01> <src_tar_02> ...'.format(script_name)
    print 'e.g.    $ {} ~/data/calibrationdata_traffic_light_*.tar.gz'.format(script_name)
    sys.exit(-1)


def main():

    if len(sys.argv) < 3:
        usage()

    src_tar_files = [os.path.normpath(x) for x in sorted(sys.argv[1:])]

    for src_tar_file in src_tar_files:
        print "Open: {}".format(src_tar_file)
        with tarfile.open(src_tar_file) as src_tar:
            src_yaml = yaml.load(src_tar.extractfile('ost.yaml'))
            dst_yaml_file = os.path.expanduser(
                '~/{}.yaml'.format(src_yaml['camera_name']))
            with open(dst_yaml_file, 'w') as dst_yaml:
                print "Write -> {}".format(dst_yaml_file)
                dst_yaml.write(yaml.dump(src_yaml))  # just copying


if __name__ == '__main__':
    main()
