import argparse
from .commands.discover import cmd_discover
from .commands.info import cmd_info
from .commands.version import cmd_version
from .commands.ping import cmd_ping
from.commands.find_node import cmd_find_node
from commands.find import cmd_find


def build_parser():
    parser = argparse.ArgumentParser(
        prog="rr",
        description="Robot Raconteur CLI (rrCLI)"
    )

    sub = parser.add_subparsers(dest="command", required=True)


    # find-node
    p_find = subparsers.add_parser("find", help="Find nodes by name")
    p_find.add_argument("--name", type=str, required=True, help="Node name to search for")
    p_find.add_argument("--json", action="store_true", help="Output results in JSON")
    p_find.set_defaults(func=cmd_find)
    
    # discover command
    p_disc = sub.add_parser("discover", help="Discover Robot Raconteur services")
    p_disc.add_argument("-t", "--type", help="robdef type to search for (e.g., com.robotraconteur.robotics.robot.Robot)")
    p_disc.add_argument("--scheme", dest="schemes", action="append", help="Transport scheme (repeatable)")
    p_disc.add_argument("--timeout", type=float, default=1.5, help="Discovery timeout in seconds")
    p_disc.add_argument("--json", action="store_true", help="Output JSON")
    p_disc.set_defaults(func=cmd_discover)

    # info command
    p_info = sub.add_parser("info", help="Show info about a service URL")
    p_info.add_argument("url", help="rr+tcp://host:port/?service=name")
    p_info.set_defaults(func=cmd_info)

    # version command
    p_ver = sub.add_parser("version", help="Show rrCLI version")
    p_ver.set_defaults(func=cmd_version)

    # ping command
    p_ping = sub.add_parser("ping", help="Test if rrCLI is working")
    p_ping.set_defaults(func=cmd_ping)

    
    p_find = sub.add_parser("find-node", help="Find a node by name")
    p_find.add_argument("name", help="Node name to search for")
    p_find.add_argument("--json", action="store_true", help="Output in JSON format")
    p_find.set_defaults(func=cmd_find_node)

    return parser


def app_main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    app_main()
