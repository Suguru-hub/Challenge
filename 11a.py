# サイコロを転がすシミュレーションを行うプログラム

#0:上面 1:南 2:東 3:西 4:北 5:裏側
class Dice():

    def __init__(self):
        self.number = [i for i in range(6)]  #[0, 1, 2, 3, 4, 5]
        self.work = [i for i in range(6)]

    def setNumber(self, n0, n1, n2, n3, n4, n5):
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5


    def roll(self,loc):
        for i in range(6):
            self.work[i] = self.number[i]

        if loc == 'E':
            self.setNumber(self.work[3],self.work[1],self.work[0],self.work[5],self.work[4],self.work[2])
        elif loc == 'N':
            self.setNumber(self.work[1],self.work[5],self.work[2],self.work[3],self.work[0],self.work[4])
        elif loc == 'S':
            self.setNumber(self.work[4],self.work[0],self.work[2],self.work[3],self.work[5],self.work[1])
        elif loc == 'W':
            self.setNumber(self.work[2],self.work[1],self.work[5],self.work[0],self.work[4],self.work[3])


    def get_Top(self):
        return self.number[0]


# n = list(map(int, input().split()))
dice = Dice()
n = list(map(int, input().split()))
dice.setNumber(n[0], n[1], n[2], n[3], n[4], n[5])
directions = input()
for direction in directions:
    dice.roll(direction)
print(dice.get_Top())