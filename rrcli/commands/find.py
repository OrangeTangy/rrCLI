from RobotRaconteur.Client import RRN
import argparse
import json
import time

def cmd_find(args):
    node_name = args.name
    transports = ["rr+tcp", "rr+local"]

    # Allow discovery to populate
    time.sleep(2)

    try:
        results = RRN.FindNodeByName(node_name, transports)
    except Exception as e:
        print(f"Discovery error: {e}")
        return

    if not results:
        print("No nodes found.")
        return

    if args.json:
        print(json.dumps([{
            "NodeID": str(r.NodeID),
            "NodeName": r.NodeName,
            "URLs": r.ConnectionURL
        } for r in results], indent=2))
    else:
        for r in results:
            print(f"NodeID: {r.NodeID}")
            print(f"NodeName: {r.NodeName}")
            print("URLs:")
            for u in r.ConnectionURL:
                print(f"  {u}")
            print("")
