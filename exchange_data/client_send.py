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
        for i in data_list:
            outdata = i
            print('send:'+outdata)
            s.send(outdata.encode())
        indata = s.recv(1024)
        if len(indata) == 0:
            s.close()
            print('server closed connection.')
        # print('recv:'+indata.decode())


# create sender data
data = basic_data("Peter", "Andy", "1", "new year")
data.add_data_to_list()
data.send_data()
