
# Robot Raconteur CLI Tool  

![My Photo](assets/images/profile.jpg)



## Overview  
This project is a command-line interface (CLI) tool for interacting with [**Robot Raconteur**](https://robotraconteur.github.io/robotraconteur/doc/core/latest/getting_started/).  

It is inspired by ROS 2’s `ros2cli` and aims to provide similar functionality for Robot Raconteur services. The tool will allow developers to:  

- Discover available services on the network  
- Inspect service types and members  
- Call service functions and interact with objects  
- *(Future goal)* Detect common networking/firewall issues  

The CLI will be designed with a **plugin system** so new commands can be added easily.  

---

## Installation (Development Mode)  

Clone the repository and install it locally:  

```bash
git clone git@github.com:YOUR-USERNAME/rrcli.git
cd rrcli
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -e .
```



## Usage

For now, the tool provides the following commands:


```Robot Raconteur CLI tool (WIP)
Available commands:
  rr discover [options]	    Discover services on the network. Supports --json, --timeout, --scheme, and -t <type>.

  rr info <url>	            Show info about a specific service URL.

  rr version	              Print rrCLI version.

  rr ping	                  Test that the CLI is running. Prints a simple response.
```

# Roadmap

## Fall 2025 (Current Semester)

* Implement CLI skeleton with discover, info, version, and ping.

* Add basic JSON and table-formatted outputs.

* Improve error handling and user feedback.

## Future Goals

* Service calls: call functions or access properties on services directly from CLI.

* Firewall and connectivity checks.

* Plugin system for extending the CLI.

* Automated test suite.

## Contributing

- Fork the repository

- Create a new feature branch (git checkout -b feature/my-feature)

- Commit your changes (git commit -m "feat: add new feature")

- Push to your branch (git push origin feature/my-feature)

- Open a Pull Request


