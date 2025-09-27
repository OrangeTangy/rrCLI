Robot Raconteur CLI Tool
Overview

This project is a command-line interface (CLI) tool for interacting with Robot Raconteur
. It aims to provide functionality similar to ROS 2’s ros2cli, but for Robot Raconteur. The tool will allow developers to:

Discover available services on the network

Inspect service types and members

Call service functions and interact with objects

(Future goal) Detect common networking/firewall issues

The CLI will be designed with a plugin system so new commands can be added easily.

Installation (Development Mode)

Clone the repo and install it locally:

git clone git@github.com:YOUR-USERNAME/rrcli.git
cd rrcli
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -e .

Usage

For now, the tool just provides a placeholder command:

rrcli --help


Output:

Robot Raconteur CLI tool (WIP)
Available commands:
  discover   Discover available Robot Raconteur services
  info       Show information about a service
