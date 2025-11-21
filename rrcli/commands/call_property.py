from RobotRaconteur.Client import *
import sys

def cmd_call_property(args):
    try:
        url = args.url
        prop = args.property
        value = args.value

        obj = RRN.ConnectService(url)

        if not hasattr(obj, prop):
            print(f"[ERROR] property '{prop}' does not exist")
            return

        # READ property
        if value is None:
            print(getattr(obj, prop))
            return

        # WRITE property
        # Try converting to float, fallback to string
        try:
            v = float(value)
        except:
            v = value

        setattr(obj, prop, v)
        print(f"Property '{prop}' updated to: {v}")

    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
