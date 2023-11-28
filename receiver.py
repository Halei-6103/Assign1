import zmq

# Prepare our context and PULL socket
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5555")

message = socket.recv_string()
print("Received:", message)