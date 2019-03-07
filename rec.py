import socket
import tof_pb2

from google.protobuf.internal.encoder import _VarintEncoder
from google.protobuf.internal.decoder import _DecodeVarint


HOST = 'localhost'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def encode_varint(value):
    """ Encode an int as a protobuf varint """
    data = []
    _VarintEncoder()(data.append, value, False)
    return b''.join(data)


def decode_varint(data):
    """ Decode a protobuf varint to an int """
    return _DecodeVarint(data, 0)[0]


def send_message(conn, msg):
    """ Send a message, prefixed with its size, to a TPC/IP socket """
    data = msg #.SerializeToString()
    size = encode_varint(len(data))
    conn.sendall(size + data)

def recv_message(conn):
    # Receive the size of the message data
    data = b''
    while True:
        try:
            data = conn.recv(1)
            size = decode_varint(data)

            msg = conn.recv(size)
            m = tof_pb2.ToF()
            m.ParseFromString(msg)
            
            for sensor in m.sensors:
                print("Sensor ID:", sensor.id)
                print("  Int value:", sensor.int_ex)
                print("  Float value:", sensor.float_ex) 
                print("  Double value:", sensor.double_value)
                print("  Double time:", sensor.double_time)
            


        except IndexError:
            pass
    

recv_message(client)
client.close()