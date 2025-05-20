# Author: Marina Hampton
# GitHub username: MarinaHampton
# Date: 05/19/2025

import zmq
import json


def send_request(port, message):
    context = zmq.Context()
    requester = context.socket(zmq.REQ)
    requester.connect(f"tcp://localhost:{port}")
    print(f"Sending request: {message}")
    requester.send_string(message)
    reply = requester.recv_string()
    print(f"Received reply: {reply}")
    requester.close()
    context.term()
    return reply


if __name__ == "__main__":
    port = 5555

    print("testing Celsius to Fahrenheit")
    request_c_to_f = json.dumps({"from": "C", "to": "F", "values": [0, 10, 20]})
    send_request(port, request_c_to_f)

    print("\ntesting Fahrenheit to Celsius")
    request_f_to_c = json.dumps({"from": "F", "to": "C", "values": [68, 32]})
    send_request(port, request_f_to_c)

    print("\ntesting with resultScale")
    request_with_scale = json.dumps({"from": "C", "to": "F", "resultScale": 1, "values": [25.5]})
    send_request(port, request_with_scale)

    print("\ntesting unsupported conversion")
    request_unsupported = json.dumps({"from": "K", "to": "C", "values": [273.15]})
    send_request(port, request_unsupported)

    print("\ntesting invalid JSON request")
    request_invalid_json = '{"invalid": "json who?"'
    send_request(port, request_invalid_json)

    print("\ntesting with an empty values array")
    request_empty_values = json.dumps({"from": "C", "to": "F", "values": []})
    send_request(port, request_empty_values)
