from RobotRaconteur.Client import *
import sys

def cmd_types(args):
    try:
        url = args.url
        obj = RRN.ConnectService(url)

        # Get service definition
        service_name = obj.RR_service_name
        service_def = RRN.GetServiceType(service_name)

        print(f"\n=== Service Definition: {service_name} ===\n")

        # Print functions
        if hasattr(obj, "RR_func"):
            print("Functions:")
            for f in obj.RR_func:
                print(f" - {f}")
        else:
            print("No functions found.")

        # Print properties
        if hasattr(obj, "RR_prop"):
            print("\nProperties:")
            for p in obj.RR_prop:
                print(f" - {p}")
        else:
            print("\nNo properties found.")

        # Print objects
        if hasattr(obj, "RR_obj"):
            print("\nObjects:")
            for o in obj.RR_obj:
                print(f" - {o}")
        else:
            print("\nNo sub-objects found.")

        print("\nDone.\n")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
