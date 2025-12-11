from arduino.app_utils import *
import socket
import json
import traceback

HOST = "0.0.0.0"
PORT = 6000

# Internal IO state cache: { "D13": True, "D2": False, ... }
io_state = {}


def parse_value_to_bool(raw):
    """
    Convert incoming 'value' field to a Python bool.
    Accepts:
      - bool
      - strings: "true"/"false", "1"/"0", "high"/"low", "on"/"off"
    Raises ValueError if not valid.
    """
    if isinstance(raw, bool):
        return raw

    if isinstance(raw, str):
        v = raw.strip().lower()
        if v in ("1", "true", "high", "on"):
            return True
        if v in ("0", "false", "low", "off"):
            return False

    raise ValueError("value must be boolean-like (true/false/1/0/high/low/on/off)")


def bool_to_bridge_arg(b: bool):
    """
    Convert Python bool to value expected by Bridge.call.
    Here we assume the bridge wants a real bool: True / False.
    """
    return b


def handle_command(cmd_obj: dict) -> dict:
    """
    Handle a single command object (already parsed from JSON).
    Returns a dict that will be serialized to JSON.
    """
    global io_state

    cmd = cmd_obj.get("cmd")
    print("handle_command() cmd_obj =", cmd_obj)  # debug print

    # --- SET IO (requires pin) ---
    if cmd == "set_io":
        pin = cmd_obj.get("pin")

        # Validate pin
        if pin is None:
            return {"ok": False, "error": "Missing field: pin"}

        if not isinstance(pin, str):
            return {"ok": False, "error": "pin must be a string"}

        # Validate value
        if "value" not in cmd_obj:
            return {"ok": False, "error": "Missing field: value"}

        raw_value = cmd_obj.get("value")

        try:
            value_bool = parse_value_to_bool(raw_value)
        except ValueError as e:
            return {"ok": False, "error": str(e)}

        # Update internal cache
        io_state[pin] = value_bool

        # Call the bridge
        try:
            bridge_value = bool_to_bridge_arg(value_bool)
            print(f"Calling Bridge.set_pin_by_name(pin={pin}, value={bridge_value})")
            Bridge.call("set_pin_by_name", pin, bridge_value)
        except Exception as e:
            print("Error in Bridge.call(set_pin_by_name):", repr(e))
            traceback.print_exc()
            return {
                "ok": False,
                "error": f"Bridge call set_pin_by_name failed: {e}"
            }

        return {
            "ok": True,
            "event": "io_updated",
            "pin": pin,
            "value": value_bool
        }

    # --- GET IO (requires pin) ---
    elif cmd == "get_io":
        pin = cmd_obj.get("pin")

        # Validate pin
        if pin is None:
            return {"ok": False, "error": "Missing field: pin"}

        if not isinstance(pin, str):
            return {"ok": False, "error": "pin must be a string"}

        # Read from bridge
        try:
            print(f"Calling Bridge.get_pin_by_name(pin={pin})")
            value_raw = Bridge.call("get_pin_by_name", pin)
        except Exception as e:
            print("Error in Bridge.call(get_pin_by_name):", repr(e))
            traceback.print_exc()
            return {
                "ok": False,
                "error": f"Bridge call get_pin_by_name failed: {e}"
            }

        if isinstance(value_raw, bool):
            value_bool = value_raw
        else:
            value_bool = bool(value_raw)

        io_state[pin] = value_bool

        return {
            "ok": True,
            "event": "io_status",
            "pin": pin,
            "value": value_bool
        }

    # --- SET ALL IO (does NOT require pin) ---
    elif cmd == "set_all_io":
        # NO pin access here

        if "value" not in cmd_obj:
            return {"ok": False, "error": "Missing field: value"}

        raw_value = cmd_obj.get("value")
        print("set_all_io raw_value =", raw_value, "type=", type(raw_value))

        try:
            value_bool = parse_value_to_bool(raw_value)
        except ValueError as e:
            print("parse_value_to_bool error in set_all_io:", repr(e))
            return {"ok": False, "error": str(e)}

        # Call the bridge with the proper boolean value
        try:
            bridge_value = bool_to_bridge_arg(value_bool)
            print(f"Calling Bridge.set_all_io(value={bridge_value})")
            Bridge.call("set_all_io", bridge_value)
        except Exception as e:
            print("Error in Bridge.call(set_all_io):", repr(e))
            traceback.print_exc()
            return {
                "ok": False,
                "error": f"Bridge call set_all_io failed: {e}"
            }

        return {
            "ok": True,
            "event": "io_all_updated",
            "value": value_bool
        }
    
    # --- GET ANALOG (requires pin) ---
    elif cmd == "get_an":
        pin = cmd_obj.get("pin")

        # Validate pin
        if pin is None:
            return {"ok": False, "error": "Missing field: pin"}

        if not isinstance(pin, str):
            return {"ok": False, "error": "pin must be a string"}

        # Read analog value from bridge
        try:
            print(f"Calling Bridge.get_an_pin_by_name(pin={pin})")
            value_raw = Bridge.call("get_an_pin_by_name", pin)
        except Exception as e:
            print("Error in Bridge.call(get_an_pin_by_name):", repr(e))
            traceback.print_exc()
            return {
                "ok": False,
                "error": f"Bridge call get_an_pin_by_name failed: {e}"
            }

        # Normalize to int
        try:
            value_int = int(value_raw)
        except (TypeError, ValueError) as e:
            print("Error converting analog value to int:", repr(e))
            return {
                "ok": False,
                "error": f"Invalid analog value returned from bridge: {value_raw!r}"
            }

        # Optionally store it in a separate cache if you want
        # io_state_analog[pin] = value_int

        return {
            "ok": True,
            "event": "an_value",
            "pin": pin,
            "value": value_int
        }
    
    # --- LED MATRIX PRINT (does NOT require pin) ---
    elif cmd == "led_matrix_print":
        # Expect a 'text' field with the string to display
        text = cmd_obj.get("text")

        if text is None:
            return {"ok": False, "error": "Missing field: text"}

        if not isinstance(text, str):
            # Try to be forgiving: convert non-strings to string
            try:
                text = str(text)
            except Exception:
                return {"ok": False, "error": "text must be a string"}

        # Optionally you can enforce a max length
        # if len(text) > 64:
        #     text = text[:64]

        try:
            print(f"Calling Bridge.led_matrix_print(text={text!r})")
            Bridge.call("led_matrix_print", text)
        except Exception as e:
            print("Error in Bridge.call(led_matrix_print):", repr(e))
            traceback.print_exc()
            return {
                "ok": False,
                "error": f"Bridge call led_matrix_print failed: {e}"
            }

        return {
            "ok": True,
            "event": "led_matrix_updated",
            "text": text
        }


    # --- Unknown command ---
    else:
        return {
            "ok": False,
            "error": f"Unknown command: {cmd}"
        }


def handle_client(conn, addr):
    print("New connection from", addr)
    buffer = ""

    # Optional: set a timeout on this client connection (in seconds)
    conn.settimeout(5.0)  # adjust if needed

    try:
        while True:
            try:
                data = conn.recv(1024)
            except socket.timeout:
                print("Socket timeout waiting for data from", addr)

                # If there is partial data in buffer, try to handle it as a single message
                if buffer.strip():
                    print("Partial data in buffer on timeout:", buffer)
                    try:
                        cmd_obj = json.loads(buffer)
                    except json.JSONDecodeError as e:
                        print("JSON decode error on timeout:", repr(e))
                        resp_obj = {
                            "ok": False,
                            "error": "Timeout waiting for complete line (missing newline or invalid JSON)"
                        }
                    else:
                        try:
                            resp_obj = handle_command(cmd_obj)
                        except Exception as e:
                            print("Unhandled error in handle_command (timeout path):", repr(e))
                            traceback.print_exc()
                            resp_obj = {
                                "ok": False,
                                "error": f"Internal error: {e.__class__.__name__}: {e}"
                            }

                    # Try to send the error/response, then close
                    try:
                        resp_line = json.dumps(resp_obj) + "\n"
                        conn.sendall(resp_line.encode("utf-8"))
                    except Exception as e:
                        print("Error while sending timeout response:", repr(e))

                # In any case, break this client loop on timeout
                break

            if not data:
                print("Client disconnected:", addr)

                # Client closed the connection: if we still have data in buffer without '\n',
                # try to interpret it as a single JSON message
                if buffer.strip():
                    print("Partial data in buffer on disconnect:", buffer)
                    try:
                        cmd_obj = json.loads(buffer)
                    except json.JSONDecodeError as e:
                        print("JSON decode error on disconnect:", repr(e))
                        resp_obj = {
                            "ok": False,
                            "error": "Client disconnected with incomplete or invalid JSON (missing newline?)"
                        }
                    else:
                        try:
                            resp_obj = handle_command(cmd_obj)
                        except Exception as e:
                            print("Unhandled error in handle_command (disconnect path):", repr(e))
                            traceback.print_exc()
                            resp_obj = {
                                "ok": False,
                                "error": f"Internal error: {e.__class__.__name__}: {e}"
                            }

                    # Try to send the error/response, then close
                    try:
                        resp_line = json.dumps(resp_obj) + "\n"
                        conn.sendall(resp_line.encode("utf-8"))
                    except Exception as e:
                        print("Error while sending disconnect response:", repr(e))

                break  # exit loop after handling disconnect

            buffer += data.decode("utf-8")

            # Normal, line-based processing
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                if not line:
                    continue

                print("Received line:", line)

                try:
                    cmd_obj = json.loads(line)
                except json.JSONDecodeError as e:
                    print("JSON decode error:", repr(e))
                    resp_obj = {"ok": False, "error": "Invalid JSON"}
                else:
                    try:
                        resp_obj = handle_command(cmd_obj)
                    except Exception as e:
                        print("Unhandled error in handle_command:", repr(e))
                        traceback.print_exc()
                        resp_obj = {
                            "ok": False,
                            "error": f"Internal error: {e.__class__.__name__}: {e}"
                        }

                try:
                    resp_line = json.dumps(resp_obj) + "\n"
                    conn.sendall(resp_line.encode("utf-8"))
                except Exception as e:
                    print("Error while sending response:", repr(e))
                    # If we can't send, stop processing this client
                    break

    finally:
        conn.close()



def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)


if __name__ == "__main__":
    main()
