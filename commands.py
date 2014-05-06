#!/usr/bin/env python
import argparse
import os.path

from nginxparser import dump, load, dumps

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--serve", type=str, action="store", dest="folder",
                        help="add the folder to the nginx location list")
    parser.add_argument("--reload", action="store_true", dest="reload",
                        help="reloads the nginx locations")
    parser.add_argument("-p", "--persistent-root", type=str, action="store", dest="persistent",
                        help="the persistent root folder")
    parser.add_argument("-r", "--root", type=str, action="store", dest="root",
                        help="the project root folder")
    args = parser.parse_args()
    return args

def serve_folder(additional, persistence, name):
    location = (
        [['location', '/' + name ],
         [['root', persistence]]])
    additional[-1][-1].append(location)
    return additional

def add_locations(config, additional):
    for conf in additional[0][1]:
        config[1][-1].append(conf)
    return config

if __name__ == "__main__":
    args = parse_args()
    config_path = os.path.join(args.root, "nginx.conf")
    additional_path = os.path.join(args.root, "nginx_additional")
    config = load(open(config_path))
    additional = load(open(additional_path))
    if args.folder:
        additional = serve_folder(additional, args.persistent, args.folder)
        dump(additional, open(additional_path, 'w'))
    if args.reload:
        config = add_locations(config, additional)
        print(dumps(config))
