from RobotRaconteur.Client import *
import sys

def cmd_list_services(args):
    try:
        url = args.url
        obj = RRN.ConnectService(url)

        # Access service name
        service_name = obj.RR_service_name
        service_def = RRN.GetServiceType(service_name)

        print(f"\nAvailable services for node:\n  {url}\n")

        print("Service Objects:")
        for o in obj.RR_obj:
            print(f"  - {o}")

        print("\nService Functions:")
        for f in obj.RR_func:
            print(f"  - {f}")

        print("\nService Properties:")
        for p in obj.RR_prop:
            print(f"  - {p}")

        print()
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
