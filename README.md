# Unit Converter Microservice

### Description of unit converter microservice: 
This microservice converts between C and F and F to C using ZeroMQ.

### Communication Contract: 
This microservice uses ZeroMQ request-reply pattern.


### How to programmatically REQUEST data?
To request the microservice to convert temperature units, a JSON string should be sent
to the bound address (5555). 

example call: 
```python
import zmq
import json

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
The unit converter microservice will respond with a JSON string (an example is shown below). The client will need to receive
the sting and parse it as a JSON object. 
```
{
  "values": [ 45.54 , 10.55, 20.33 ]
}

```

### UML sequence diagram
![UML Sequence Diagram](UML_microservice_a.png)

