# Unit Converter Microservice

### Description of unit converter microservice: 
converts between C and F and F to C. Uses ZeroMQ.

### Communication Contract: 
This microservice uses ZeroMQ request-reply pattern.


### How to programmatically REQUEST data?
To request the microservice to convert temperature units, a JSON string should be sent
to the bound address (5555). 

example call: 
```JSON
context = zmq.Context()
requester = context.socket(zmq.REQ)
requester.connect("tcp://localhost:5555")

request_data = {
  "from": "F",
  "to": "C",
  "resultScale": 2,
  "values": [68, 77, 99]
}
```

### How to pragmatically RECEIVE data
```JSON
{
  "values": [ /* an array of converted values (in the same order as the request) */ ]
}

```

### UML sequence diagram

TODO





