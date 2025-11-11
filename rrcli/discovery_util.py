# rrcli/discovery_utils.py
from RobotRaconteur.Client import *
import json
import time

def init_discovery(transports=None, delay=2):
    if transports is None:
        transports = ["rr+tcp", "rr+local"]
    time.sleep(delay)
    return transports

def format_results(results, json_output=False):
    if json_output:
        return json.dumps([{
            "NodeID": str(r.NodeID),
            "NodeName": r.NodeName,
            "URLs": r.ConnectionURL
        } for r in results], indent=2)
    else:
        formatted = ""
        for r in results:
            formatted += f"\nNodeID: {r.NodeID}\nNodeName: {r.NodeName}\nURLs:\n"
            for u in r.ConnectionURL:
                formatted += f"  {u}\n"
        return formatted
