## 4-relay-ui — Application overview

`4-relay-ui` is an Arduino UNO Q App Lab example that shows how to build a simple but powerful control interface for a 4-channel relay shield. The goal of the application is to demonstrate how the UNO Q can combine a user-friendly UI running on Linux with precise, real-time control of physical outputs handled by the microcontroller.

This example is intentionally practical: it turns the UNO Q into a small control panel that can switch external devices such as lamps, motors, valves, or other loads connected to the relay shield.

## How the application is structured

The application is split into two coordinated parts, which is a core concept of the UNO Q architecture.

On the Linux side, the App Lab application provides the user interface. This is where buttons, labels, and logic live. The UI lets the user turn each relay channel on or off with a simple interaction, without worrying about pins or timing.

On the microcontroller side, a sketch runs on the MCU and is responsible for directly driving the relay shield pins. This part of the application guarantees deterministic behavior when switching relays, which is essential when interacting with real hardware.

The two sides communicate using the UNO Q RPC (Remote Procedure Call) mechanism. From the developer’s point of view, this feels like calling a function, but under the hood it safely bridges Linux and the MCU.

## How it works at runtime

When the app starts, both the Linux application and the MCU sketch are launched together as a single App Lab project.

When a user presses a button in the UI, the Linux application sends an RPC command specifying which relay channel should change state and whether it should be turned on or off.

The MCU receives this command and maps it to the correct GPIO pin connected to the relay shield. It then sets the pin to the appropriate logic level, energizing or releasing the relay coil. The relay contacts switch the external load, while keeping the low-voltage UNO Q electronics electrically isolated.

Optionally, the UI can reflect the current state of each relay, giving immediate visual feedback to the user.

## What this example demonstrates

This example is a clear illustration of the UNO Q development model. Linux is used where it makes sense, for UI and application logic, while the microcontroller handles real-time hardware control. The RPC bridge keeps everything synchronized without forcing the developer to manage complex inter-process communication.

`4-relay-ui` is especially useful as a starting point for home automation panels, industrial control prototypes, educational demos, or any project where a simple dashboard needs to control physical outputs.

In short, it shows how quickly you can move from a concept to a working, touchable application using Arduino UNO Q and App Lab.




