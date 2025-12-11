# Arduino Uno Q Apps

A collection of applications developed and optimized exclusively for the **Arduino Uno Q** platform.

This repository provides ready-to-use sketches and companion applications that leverage the advanced capabilities of the Uno Q for various projects, including IoT, modular development, and multimedia.

## 🚀 Applications and Features

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

## ⚙️ Prerequisites

To use these applications, you will need:

1.  **Arduino Uno Q Board:** This collection is designed specifically for this device.
2.  **Required Hardware Modules:** Depending on the specific app (e.g., 4-channel relay shield, buzzer, addressable LED strip, display for video player, etc.).
3.  **Network Access:** The Uno Q device must be connected to the internet to run the installation script.

## 💻 How to Install and Use

These shell scripts are designed to be executed directly on the **Arduino Uno Q** device to download and install the applications into the correct project structure.

### Option 1: Install All Applications (Recommended)

Run this command directly in the shell environment of your **Arduino Uno Q** to install all available applications:

```bash
curl -sSL [https://raw.githubusercontent.com/akash73/arduino-uno-q-apps/refs/heads/main/install.sh](https://raw.githubusercontent.com/akash73/arduino-uno-q-apps/refs/heads/main/install.sh) | bash
