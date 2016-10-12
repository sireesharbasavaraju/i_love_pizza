# absence of value indicated by "o"

class FU(object):

    def __init__(self):
        self.x_in = ["o"]
        self.y_in = ["o"]
        self.x_out = ["o"]
        self.y_out = ["o"]
        self.opr1 = ""
        self.opr2 = ""

    def fire(self):
        self.opr1 = self.x_in.pop(0) 
        self.opr2 = self.y_in.pop(0)

        if self.opr1 == "o" or self.opr2 == "o":
            #self.x_in.insert(0, opr1)
            #self.y_in.insert(0, opr2)
            self.x_out.append("o")
            self.y_out.append("o")
            return

        self.x_out.append(self.opr1)
        self.y_out.append(self.opr2)
        

