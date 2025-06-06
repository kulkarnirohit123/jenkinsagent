# Jenkins Agent

This repository contains configurations and scripts for setting up a Jenkins agent.

## Overview

A Jenkins agent is a node that runs jobs delegated by the Jenkins master. This repository provides the necessary setup and instructions to configure a Jenkins agent.

## Features

- Automated setup scripts
- Configuration files for Jenkins agent
- Support for Docker-based agents

## Requirements

- Jenkins master server
- Java installed on the agent machine
- Docker (optional, for containerized agents)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rohit/jenkinsagent.git
2. Next Steps:

Place your quantized LLaMA model at:
```bash
./models/llama-2-7b.ggml.q4_0.bin
```
Install required packages:
```bash
pip install llama-cpp-python requests
```
Run the agent manually:
```bash
python jenkins_agent.py
cd jenkinsagent
 ```

2. Follow the setup instructions in the `docs/setup.md` file.

## Usage

- Start the Jenkins agent using the provided scripts.
- Ensure the agent is connected to the Jenkins master.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.