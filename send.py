import socket
import tof_pb2
import datetime
from google.protobuf.internal.encoder import _VarintEncoder
from google.protobuf.internal.decoder import _DecodeVarint


HOST = ''
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096


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
    conn.sendall(size)
    conn.sendall(msg)

def pack_data():
    tofs = tof_pb2.ToF()
    sensor1 = tofs.sensors.add()
    sensor1.id = '1234'
    sensor1.double_time = 1000 * datetime.datetime.now().timestamp() #from micro to milli s
    sensor1.int_ex = 1
    sensor1.float_ex = 1.234
    sensor1.double_value = 0.1234567

    sensor2 = tofs.sensors.add()
    sensor2.id = '5678'
    sensor2.double_time = 1000 * datetime.datetime.now().timestamp() #from micro to milli s
    sensor2.int_ex = 1
    sensor2.float_ex = 5.678
    sensor2.double_value = 0.765432
    return tofs.SerializeToString()


try:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind(ADDR)
    serv.listen(5)

    print('listening ...')
    try:
        conn = None
        while True:
            conn, addr = serv.accept()
            print('client connected ... ', addr)
            for i in range(10):
                msg = pack_data()
                send_message(conn, msg)
            conn.close()
            print('finished writing data')
           
    finally:
        if conn:
            conn.close()
finally:
    serv.close()
