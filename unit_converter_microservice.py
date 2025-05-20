# Author: Marina Hampton
# GitHub username: MarinaHampton
# Date: 05/19/2025
# Description: CS361 converts temperatures from C to F and F to C.
# written in Python and uses ZeroMQ
# returns a "values" array as per requirements
# example json request
"""
 {
  "from": "C",
  "to": "F",
  "values": [20, 25.5, 100]
}
"""

import zmq
import json

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5 ) + 32

def fahrenheit_to_celsius (fahrenheit):
    return (fahrenheit - 32) * 5/9

def conversion (request):
    try:
        requested_data = json.loads(request)
        from_unit = requested_data.get("from").upper() # so not case-sensitive
        to_unit = requested_data.get("to").upper()
        result_scale = int(requested_data.get("resultScale", 2))
        values = requested_data.get("values", [])
        results = [] #returns an array

        # actual conversions,
        if from_unit == "C" and to_unit == "F":
            for val in values:
                results.append(round(celsius_to_fahrenheit(val), result_scale))
        elif from_unit == "F" and to_unit == "C":
            for val in values:
                results.append(round(fahrenheit_to_celsius(val), result_scale))
        else:
            return json.dumps({"error": "Unsupported unit conversion"})

        return json.dumps({"values": results})

    # in case of errors
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON request"})
    except Exception as e:
        return json.dumps({"error": str(e)})

def main():
    context = zmq.Context()
    responder = context.socket(zmq.REP)
    responder.bind("tcp://*:5555")

    print("unit converter microservice started...")

    while True:
        request = responder.recv_string()
        print(f"Received request: {request}")
        response = conversion(request)
        responder.send_string(response)
        print(f"Sent response: {response}")

if __name__ == "__main__":
    main()