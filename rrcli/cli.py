# rrcli/cli.py
import argparse
from rrcli.commands.find import cmd_find

def build_parser():
    parser = argparse.ArgumentParser(prog="rr", description="Robot Raconteur CLI Tool")
    sub = parser.add_subparsers(dest="command")

    p_find = sub.add_parser("find", help="Find nodes or services on the network")
    p_find.add_argument("--name", type=str, help="Node name to search for")
    p_find.add_argument("--service", type=str, help="Service type to search for")
    p_find.add_argument("--json", action="store_true", help="Output as JSON")
    p_find.set_defaults(func=cmd_find)

    return parser

def app_main():
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    app_main()
