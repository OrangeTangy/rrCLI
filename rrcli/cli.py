import argparse
from .commands.discover import cmd_discover
from .commands.info import cmd_info
from .commands.discover import cmd_discover
from .commands.info import cmd_info
from .commands.version import cmd_version
from .commands.ping import cmd_ping

def build_parser():
    parser = argparse.ArgumentParser(
        prog="rr",
        description="Robot Raconteur CLI (WIP)"
    )

    
    sub = parser.add_subparsers(dest="command", required=True)

    
    p_disc = sub.add_parser("discover", help="Discover Robot Raconteur services")
    p_disc.add_argument("-t", "--type", help="robdef type to search for (e.g., com.robotraconteur.robotics.robot.Robot)")
    p_disc.add_argument("--scheme", dest="schemes", action="append",
                        help="Transport scheme (repeatable). e.g. --scheme rr+tcp --scheme ws")
    p_disc.add_argument("--timeout", type=float, default=1.5, help="Discovery timeout in seconds")
    p_disc.add_argument("--json", action="store_true", help="Output JSON")
    p_disc.set_defaults(func=cmd_discover)

    
    p_info = sub.add_parser("info", help="Show info about a service URL")
    p_info.add_argument("url", help="rr+tcp://host:port/?service=name")
    p_info.set_defaults(func=cmd_info)

      # --- version ---
    p_ver = sub.add_parser("version", help="Show rrCLI version")
    p_ver.set_defaults(func=cmd_version)

    # --- ping ---
    p_ping = sub.add_parser("ping", help="Test the CLI is working")
    p_ping.set_defaults(func=cmd_ping)

    return parser

def app_main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    app_main()
