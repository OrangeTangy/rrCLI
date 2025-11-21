# rrcli/cli.py
import argparse
from rrcli.commands.find import cmd_find
from commands.types import cmd_types
from commands.call import cmd_call
 from rrcli.commands.list_services import cmd_list_services


def build_parser():
    parser = argparse.ArgumentParser(prog="rr", description="Robot Raconteur CLI Tool")
    sub = parser.add_subparsers(dest="command")

    p_find = sub.add_parser("find", help="Find nodes or services on the network")
    p_find.add_argument("--name", type=str, help="Node name to search for")
    p_find.add_argument("--service", type=str, help="Service type to search for")
    p_find.add_argument("--json", action="store_true", help="Output as JSON")
    p_find.set_defaults(func=cmd_find)
   

    p_ls = sub.add_parser("list-services", help="List all services exposed by a node")
    p_ls.add_argument("url")
    p_ls.set_defaults(func=cmd_list_services)

    # rr types
    p_types = sub.add_parser("types", help="Inspect a service's type information")
    p_types.add_argument("url", help="Service URL to inspect")
    p_types.set_defaults(func=cmd_types)
    
    # rr call
    p_call = sub.add_parser("call", help="Call a service function has get property")
    p_call.add_argument("url", help="Service URL")
    p_call.add_argument("member", help="Function or property name")
    p_call.add_argument("args", nargs="*", help="Arguments for function")
    p_call.set_defaults(func=cmd_call)


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
