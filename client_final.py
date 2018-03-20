# Echo client
import socket

def Main():
    HOST = '192.168.43.199'
    PORT = 5006

    sock = socket.socket()
    sock.connect((HOST, PORT))

    while True:
        message = raw_input("-> ")
        message=str(message)
        # Send message to server
        sock.send(message.encode())
        
        # Receive echo back
        data = sock.recv(1024)
        print("Received from server: ", data.decode())

    sock.close()

if __name__ == '__main__':
    Main()
