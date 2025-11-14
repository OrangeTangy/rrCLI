from RobotRaconteur.Service import *
import time

# Simple service object with a function and property
class TestObject:
    def add_numbers(self, a, b):
        return a + b

    @property
    def message(self):
        return "Hello from RR!"

def main():
    RRN.RegisterServiceType("""
    service test.example

    object TestObject
        function double add_numbers(double a, double b)
        property string message
    end
    """)

    obj = TestObject()
    node = RRN.RegisterService(
        "test_service",
        "test.example.TestObject",
        obj
    )

    print("Service running on rr+tcp://localhost:52222/?service=test_service")
    RRN.SetupTcpServer(52222)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
