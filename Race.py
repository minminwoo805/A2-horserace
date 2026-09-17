# A2: A Horse Race
# Minwoo Kim ( u1569354 )

from graphics import *
from Dice import *

class Horse :
    def __init__(self, speed, y , image , window):
        self.x_pos =  40
        self.y_pos = y # x , y 그림의 끝 좌표에 두기
        self.image = image
        self.window = window
        self.dice = Dice(speed)

    def move(self):
        # move each horse randomly
        self.x_pos += self.dice.roll()

    def draw(self):
        # draw it
        self.image.draw_at_pos(self.window, self.x_pos,  self.y_pos)

    def crossed_finish_line(self, finish_line):
       if self.x_pos >= finish_line :
           return True

       else :
           return False





def main() :
    win = GraphWin("Horse Race", 700, 350, autoflush=False)
    win.setBackground('white')

    img1 = Image(Point(0,0), "elephant.gif")
    horse1 = Horse(6, 50, img1, win)
    horse1.draw()

    img2 = Image(Point(0,0),"Lion.gif")
    horse2 = Horse(6, 250,img2,win)
    horse2.draw()

    img3 = Image(Point(0,0),"zebra.gif")
    horse3 = Horse(6, 150,img3,win)
    horse3.draw()

    Finishline = Line(Point(600, 400), Point(600, -300))
    Finishline.draw(win)

    winners = []
    win.getMouse()
    while True:
        win.clear_win()

        Finishline = Line(Point(600, 400), Point(600, -300))
        Finishline.draw(win)

        Horse.move(horse1)
        Horse.draw(horse1)
        Horse.move(horse2)
        Horse.draw(horse2)
        Horse.move(horse3)
        Horse.draw(horse3)

        if horse1.crossed_finish_line(600):
            winners.append("Horse1")

        if horse2.crossed_finish_line(600):
            winners.append("Horse2")

        if horse3. crossed_finish_line(600):
            winners.append("Horse3")

        if len(winners) >= 1 :
            break

        win.update()
    if len(winners) == 1 :
        print(f"{winners[0]} is the winner ")

    elif len(winners) == 2 :
        print(f"Tie {winners[0]} with {winners[1]} ")




    win.update()
    win.getMouse()
    win.close()




if __name__ == "__main__":
    main()
