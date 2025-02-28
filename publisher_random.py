import time
import zmq
import random

ctx = zmq.Context.instance()
pub = ctx.socket(zmq.PUB)
pub.connect("tcp://localhost:5555")

while True:
    topic = "random"
    msg = f"{topic} {random.randint(1, 100)}"
    print(f"msg: {msg}")
    pub.send_string(msg)
    time.sleep(1)

ctx.close()
pub.close()