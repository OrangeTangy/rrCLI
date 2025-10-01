import argparse
from .commands.discover import cmd_discover
from .commands.info import cmd_info

def build_parser():
    parser = argparse.ArgumentParser(prog="rr", description="Robot Raconteur CLI (WIP)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_disc = sub.add_parser("discover", help="Discover services")
    p_disc.set_defaults(func=cmd_discover)

    p_info = sub.add_parser("info", help="Show info about a service URL")
    p_info.add_argument("url", help="rr+tcp://host:port/?service=name")
    p_info.set_defaults(func=cmd_info)

    return parser

def app_main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    app_main()
