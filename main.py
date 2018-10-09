import DATABASE
import GUI
import interface

class aplication:

    def __init__(self):
        self.data = DATABASE.Database()
        self.net = interface.interface()
        self.GUI = GUI.GUI(data=self.data, net=self.net)



if __name__ == '__main__':
    a = aplication()
