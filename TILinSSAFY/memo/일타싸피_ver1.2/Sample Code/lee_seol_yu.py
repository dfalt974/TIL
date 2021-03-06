import socket
import time
import math
from IPython import embed

# User and Game Server Information
NICKNAME = 'Seolyu'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0    
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle = 0
    power = 0
    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    # embed()
    # gameData => 공정보
    
    # Stage 1
    # conn.send(50, 50)

    # Stage 2
    # conn.send(105, 100)

    # Stage 3
    # conn.send(105, 100)
    # conn.send(267,100)
   
    # Stage 4
    # conn.send(50, 50)
    # conn.send(86, 70)
    # conn.send(45, 10)
    # conn.send(104, 90)
    # embed()

    # Stage 5
    # embed()
    # conn.send(89, 200)
    # conn.send(185, 100)

    # Stage 6
    embed()
    # conn.send(89, 200)
    # conn.send(185, 100)

    # conn.send(290, 200)
    # conn.send(177, 100)
    # conn.send(80, 80)
    # conn.send(177, 60)

    # conn.send(44, 70)
    # conn.send(0, 40)
    # conn.send(0, 40)

    # conn.send(210, 100)
    # conn.send(45, 100)
    # conn.send(170, 50)
    # conn.send(230, 50)
    # conn.send(330, 100)
    # conn.send(330, 40)




def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
