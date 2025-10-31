from RobotRaconteur.Client import RRN
import argparse
import time
import json

def cmd_find_node(args):
    node_name = args.name
    transports = ["rr+local", "rr+tcp"]

    # Give discovery time to start
    time.sleep(2)

    try:
        results = RRN.FindNodeByName(node_name, transports)
        nodes_info = []

        for s in results:
            nodes_info.append({
                "NodeID": str(s.NodeID),
                "NodeName": s.NodeName,
                "ConnectionURL": s.ConnectionURL
            })

        if args.json:
            print(json.dumps(nodes_info, indent=2))
        else:
            for n in nodes_info:
                print(f"NodeID: {n['NodeID']}")
                print(f"NodeName: {n['NodeName']}")
                print(f"ConnectionURL: {n['ConnectionURL']}")
                print("---")

    except Exception as e:
        print("Error finding node:", e)
