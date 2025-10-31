from RobotRaconteur import ServerNodeSetup
import time

# This creates a service node that advertises itself on the network
with ServerNodeSetup("experimental.reynard_the_robot", 53839) as node_setup:
    print("✅ Test service running as 'experimental.reynard_the_robot'")
    print("Press Ctrl+C to stop")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nService shutting down...")
