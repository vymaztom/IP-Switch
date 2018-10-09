import os
from copy import copy

class interface:

    def __init__(self):
        self.cmd_data = ""
        self.l_interface = []
        self.d_ip = {}
        self.d_mask = {}
        self.d_gate = {}

    def set_configuratin(self, interface, ip, mask, gate):

        com = 'netsh interface ip set address "' + str(interface) \
              + '" static ' + str(ip) + ' ' + str(mask) + ' ' + str(gate) + ' 1 > file.txt'
        os.system(com)
        with open("file.txt","r",encoding="852") as f:
            text = f.read()
        os.remove("file.txt")

        return text

    def get_parameters(self):
        os.system("netsh interface ipv4 show config > file.txt")
        with open("file.txt", "r", encoding='852') as f:
            for line in f:
                if line.__contains__("Configuration for interface"):
                    interface = copy(line[29:-2])
                    self.l_interface.append(copy(interface))
                    self.d_ip[copy(interface)] = "None"
                    self.d_mask[copy(interface)] = "None"
                    self.d_gate[copy(interface)] = "None"
                if line.__contains__("IP Address:"):
                    ip = copy(line[42:-1])
                    self.d_ip[copy(interface)] = copy(ip)
                if line.__contains__("Subnet Prefix:"):
                    i = 42
                    while line[i] != 'k':
                        i += 1
                    mask = copy(line[i+1:-2])
                    self.d_mask[copy(interface)] = copy(mask)
                if line.__contains__("Default Gateway:"):
                    gate = copy(line[42:-1])
                    self.d_gate[copy(interface)] = copy(gate)
        os.remove("file.txt")

    def print_data(self):
        print(self.l_interface)
        print(self.d_ip)
        print(self.d_mask)
        print(self.d_gate)

if __name__ == '__main__':
    a = interface()
    print(a.get_parameters())
    a.print_data()
