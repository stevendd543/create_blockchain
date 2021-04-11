import time
import socket
data_list = []


class basic_data:
    def __init__(self, sender, receiver, datanum, videoname):
        self.sender = sender
        self.receiver = receiver
        self.datanum = datanum
        self.videoname = videoname

    def add_data_to_list(self):
        data_list.append(self.sender)
        data_list.append(self.receiver)
        data_list.append(self.datanum)
        data_list.append(self.videoname)

    def send_data(self):
        HOST = '127.0.0.1'
        PORT = 3000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        outdata = data_list[0]
        print('send:'+outdata)
        s.send(outdata.encode())
        indata = s.recv(1024)
        if len(indata) == 0:
            s.close()
            print('server closed connection.')
        print('recv:'+indata.decode())


class block:
    def __init__(self, previous_hash, difficulty, miner):
        self.previous_hash = previous_hash
        self.hash = ''
        self.difficulty = difficulty
        self.nonce = 0
        self.timestamp = int(time.time())
        self.videos_data = []
        self.miner = miner


class BlockChain:
    def __init__(self):
        self.adjust_difficulty_blocks = 10
        self.difficulty = 1
        self.block_time = 30
        self.mining_rewards = 10
        self.block_limitation = 32
        self.chain = []
        self.pending_video = []
