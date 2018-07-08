


class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다. : From %d to %d" %(self.back_number, new_number))
        self.back_number = new_number


    def __str__(self):
        return "Hello, My name is %s. I play in %s in center" %(self.name, self.position)

sanghyuk = SoccerPlayer("Sanghyuk", "MF", 10)
print(sanghyuk)

sanghyuk.change_back_number(5)
