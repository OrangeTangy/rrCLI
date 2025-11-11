# rrcli/commands/find.py
import argparse
from RobotRaconteur.Client import RRN
from rrcli.discovery_utils import init_discovery, format_results

def cmd_find(args):
    transports = init_discovery()

    try:
        if args.name:
            results = RRN.FindNodeByName(args.name, transports)
        elif args.service:
            results = RRN.FindServiceByType(args.service, transports)
        else:
            print("Error: please specify --name or --service")
            return
    except Exception as e:
        print(f"Discovery error: {e}")
        return

    if not results:
        print("No matching results found.")
        return

    print(format_results(results, json_output=args.json))
