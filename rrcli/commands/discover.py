# rrcli/commands/discover.py
import json
import sys
import time #sleep based waiting time

def cmd_discover(args):
    try:
        import RobotRaconteur as RR # pyright: ignore[reportMissingImports]
    except ImportError:
        print("RobotRaconteur is not installed. Run: pip install robotraconteur", file=sys.stderr)
        sys.exit(1)

    RRN = RR.RobotRaconteurNode.s

    # Default schemes to try if none were provided
    schemes = args.schemes or ["rr+tcp", "rrs+tcp", "rr+local", "ws", "wss"]
    timeout = float(args.timeout or 1.5)

    results = []

    try:
        if args.type:
            # Query services by type (fast path when you know what you're looking for)
            # Returns a list of ServiceInfo2 structures
            infos = RRN.FindServiceByType(args.type, schemes)
            for i in infos:
                results.append({
                    "service": getattr(i, "Name", None),
                    "root_object_type": getattr(i, "RootObjectType", None),
                    "node": getattr(i, "NodeName", None),
                    "nodeid": str(getattr(i, "NodeID", "")),
                    "urls": list(getattr(i, "ConnectionURL", []) or []),
                    "attributes": dict(getattr(i, "Attributes", {}) or {})
                })
        else:
            # Generic discovery (no type specified): update and read detected nodes
            # This scans the network and gathers broadcasted service info
            RRN.UpdateDetectedNodes(schemes)
            time.sleep(timeout)
            detected = RRN.GetDetectedNodes()  # dict-like: NodeID -> DetectedNode

            for nodeid, node in (detected or {}).items():
                node_name = getattr(node, "NodeName", None)
                services = getattr(node, "Services", []) or []
                for s in services:
                    results.append({
                        "service": getattr(s, "Name", None),
                        "root_object_type": getattr(s, "RootObjectType", None),
                        "node": node_name,
                        "nodeid": str(nodeid),
                        "urls": list(getattr(s, "ConnectionURL", []) or []),
                        "attributes": dict(getattr(s, "Attributes", {}) or {})
                    })
    except Exception as e:
        print(f"Discovery error: {e}", file=sys.stderr)
        sys.exit(2)

    # Output
    if args.json:
        print(json.dumps(results, indent=2))
        return

    if not results:
        print("No services found.")
        return

    print(f"Found {len(results)} service(s):")
    for r in results:
        url = r["urls"][0] if r.get("urls") else "(no URL)"
        svc = r.get("service") or "(unknown)"
        node = r.get("node") or "(unknown)"
        rtype = r.get("root_object_type") or "(unknown type)"
        print(f"- {svc} @ {url}")
        print(f"    type: {rtype}")
        print(f"    node: {node}  id: {r.get('nodeid','')}")
