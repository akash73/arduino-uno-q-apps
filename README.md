# Arduino Uno Q Apps

A collection of applications developed and optimized exclusively for the **Arduino Uno Q** platform.

This repository provides ready-to-use sketches and companion applications that leverage the advanced capabilities of the Uno Q for various projects, including IoT, modular development, and multimedia.

##  Applications and Features

This repository bundles several different projects, each focusing on a unique application on the **Uno Q**. You can explore the directories for detailed code and specific hardware setup.

| Directory | Description |
| :--- | :--- |
| **`4-relay-shield`** | Code for controlling a 4-channel relay shield, integrated with the Uno Q. |
| **`detect-objects-to-sketch`** | An application involving object detection (via a companion app) that generates or influences an output sketch running on the Uno Q. |
| **`mood-detector`** | A project focused on detecting or indicating 'mood' based on sensor data or interaction with the Uno Q. |
| **`uno-q-video-player`** | Code that utilizes the capabilities of the **Uno Q** to play video content on an attached screen. |
| **`modulino-buzz`** | Control of a buzzer module using the `Modulino` framework for the Uno Q. |
| **`rpc-call-buzz`** | Demonstrates how to trigger the buzzer on the Uno Q using a Remote Procedure Call (RPC) mechanism. |
| **`modulino-pixel-only`** | Basic control of addressable LED pixels (like NeoPixels or similar), structured with the Modulino library for the Uno Q. |
| **`monitor-example`** | A simple sketch demonstrating basic input/output functionality, often used with the Uno Q's monitoring features. |
| **` double-bridge`** |  Example that shows how to control a **dual H-bridge motor driver** with UNO Q.  The app demonstrates forward, reverse, and stop control of two motors by sending commands from the Linux side to the MCU, making it easy to understand motor control patterns for robotics or automation. |
| **`4-relay-ui `** | UI-focused example for a 4-channel relay shield. This app adds a simple graphical interface in App Lab to toggle each relay individually, showing how to connect a user interface running on the UNO Q with real-world actuators driven by the MCU. |


##  Prerequisites

To use these applications, you will need:

1.  **Arduino Uno Q Board:** This collection is designed specifically for this device.
2.  **Required Hardware Modules:** Depending on the specific app (e.g., 4-channel relay shield, buzzer, addressable LED strip, display for video player, etc.).
3.  **Network Access:** The Uno Q device must be connected to the internet to run the installation script.

## How to Install and Use

These shell scripts are designed to be executed directly on the **Arduino Uno Q** device to download and install the applications into the correct project structure.
Run this command directly in the shell environment of your **Arduino Uno Q** to install all available applications:

```bash
curl -sSL https://github.com/akash73/arduino-uno-q-apps/blob/main/app-install.sh | bash
```



## Contributing to arduino-uno-q-apps

This repository is a collection of example applications for Arduino UNO Q.
Contributions are welcome, whether you want to fix an example, improve documentation, or add a completely new application.

Everything below follows a simple and standard GitHub workflow.

# Fork the repository

Open the repository on GitHub:

https://github.com/akash73/arduino-uno-q-apps

Click the Fork button in the top-right corner of the page.
This creates a personal copy of the repository under your GitHub account.

Clone your fork locally

Clone your fork to your local machine so you can work on it:

git clone https://github.com/<your-username>/arduino-uno-q-apps.git
cd arduino-uno-q-apps


Replace <your-username> with your GitHub username.

Create a branch for your application

Create a dedicated branch for your work. This keeps changes clean and easy to review.

git checkout -b my-new-app


Use a branch name that reflects the application you are adding.

## Add your own application

Each application lives in its own directory at the root of the repository.
Create a new folder and follow the same structure used by the existing examples.

my-new-app/

├── sketch/        # Arduino sketch running on the MCU

├── app/           # App Lab / Linux-side application

└── README.md      # Description, usage, and requirements


The README.md should explain what the application does, what hardware is required, and how to run it on Arduino UNO Q.

Keeping the structure consistent makes it easier for others to understand and reuse your work.

Commit and push your changes

Once your application is ready, commit it and push it to your fork:

git add .
git commit -m "Add new UNO Q app: my-new-app"
git push origin my-new-app

Open a pull request

Go to your fork on GitHub.
You will see a prompt to create a Pull Request from your branch.

Open the pull request against the main branch of the original repository and add a short description of your application and its purpose.
This allows maintainers to review and merge your contribution.

Keep your fork up to date

If you plan to contribute regularly, keep your fork aligned with the original repository:

git remote add upstream https://github.com/akash73/arduino-uno-q-apps.git
git fetch upstream
git checkout main
git merge upstream/main


This ensures your work is always based on the latest version of the project.

By following this workflow, you can experiment with new ideas on Arduino UNO Q and share them back with the community.
