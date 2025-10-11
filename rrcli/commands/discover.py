import json, sys, time

def cmd_discover(args):
    try:
        import RobotRaconteur as RR
    except ImportError:
        print("RobotRaconteur not installed. Run: pip install robotraconteur", file=sys.stderr)
        sys.exit(1)

    RRN = RR.RobotRaconteurNode.s

    schemes = args.schemes or ["rr+tcp", "rrs+tcp", "rr+local", "ws", "wss"]
    timeout = float(args.timeout or 1.5)
    results = []

    try:
        if args.type:
            infos = RRN.FindServiceByType(args.type, schemes)
            for i in infos:
                results.append({
                    "service": getattr(i, "Name", None),
                    "root_object_type": getattr(i, "RootObjectType", None),
                    "node": getattr(i, "NodeName", None),
                    "urls": list(getattr(i, "ConnectionURL", []) or [])
                })
        else:
            RRN.UpdateDetectedNodes(schemes)
            time.sleep(timeout)
            detected = RRN.GetDetectedNodes()
            for nodeid, node in (detected or {}).items():
                node_name = getattr(node, "NodeName", None)
                for s in (getattr(node, "Services", []) or []):
                    results.append({
                        "service": getattr(s, "Name", None),
                        "root_object_type": getattr(s, "RootObjectType", None),
                        "node": node_name,
                        "urls": list(getattr(s, "ConnectionURL", []) or [])
                    })
    except Exception as e:
        print(f"Discovery error: {e}", file=sys.stderr)
        sys.exit(2)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    if not results:
        print("No services found.")
        return

    print(f"Found {len(results)} service(s):")
    for r in results:
        url = r["urls"][0] if r.get("urls") else "(no URL)"
        print(f"- {r.get('service')} @ {url}")
