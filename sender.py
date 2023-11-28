import zmq

# Prepare our context and PUSH socket
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5555")

message = "A message from CS361"
socket.send_string(message)
print("Sent:", message)