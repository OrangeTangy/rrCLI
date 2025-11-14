from RobotRaconteur.Client import *
import sys

def cmd_call(args):
    try:
        url = args.url
        member = args.member
        inputs = args.args

        obj = RRN.ConnectService(url)

        # Get the function or property
        if hasattr(obj, member):
            target = getattr(obj, member)
        else:
            print(f"Member '{member}' does not exist.")
            return

        # If it's a property read
        if isinstance(target, str) or not callable(target):
            print(target)
            return

        # Call function with converted args
        converted = []
        for x in inputs:
            try:
                converted.append(float(x))
            except:
                converted.append(x)

        result = target(*converted)
        print(f"Result: {result}")

    except Exception as e:
        print(f"Error calling function: {e}")
        sys.exit(1)
