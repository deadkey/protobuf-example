A small example application for sending protobuffer messages over network using sockets. 
See https://developers.google.com/protocol-buffers/docs/pythontutorial

Tested on Ubuntu 18.04 with proto3 and Python3.6.

# Getting Started

Install the protobuffer compiler
 ```bash 
 apt-get install protobuf-compiler
 ```

Clone this repository
 ```bash 
git clone https://github.com/deadkey/protobuf-example.git
 ```
and navigate to the folder in a terminal.

In the example file tof.proto, the message type is defined:
```python 
syntax = "proto3";

package kp;

message Sensor {
  string id = 1;
  int64 int_ex = 2;
  float float_ex = 3;
  double double_time = 4;
  double double_value = 5;

}

message ToF {
  repeated Sensor sensors = 1;
}
 ```
This means that each ToF message can have multiple sensors, each with an id, time and different values. 

Compile the proto-message for python
 ```bash 
 protoc -I=. --python_out=. ./tof.proto
 ```
This creates a tof_pb2.py file in the current folder.

In the send.py is an example of a socket server that sends values for two sensors in one ToF message to a client in the rec.py file.
