# A2: A Horse Race
# Minwoo Kim ( u1569354 )

from graphics import *
from Dice import *

class Horse :
    def __init__(self, speed, y , image , window):
        self.x_pos =  0
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
        # when x position pass finish line it stops
       if self.x_pos >= finish_line :
           return True

       else :
           return False





def main() :
    win = GraphWin("Horse Race", 700, 350, autoflush=False)
    # set background to see finish line clearly
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

    # make finish line before mouse click and after mouth click to show line always
    Finishline = Line(Point(600, 400), Point(600, -300))
    Finishline.draw(win)

    # make empty list to know winners more easily
    winners = []
    win.getMouse()
    while True:
        win.clear_win()

        Finishline = Line(Point(600, 400), Point(600, -300))
        Finishline.draw(win)

        horse1.move()
        horse1.draw()
        horse2.move()
        horse2.draw()
        horse3.move()
        horse3.draw()

        # add winner in empty list
        if horse1.crossed_finish_line(600):
            winners.append("Horse1")

        if horse2.crossed_finish_line(600):
            winners.append("Horse2")

        if horse3. crossed_finish_line(600):
            winners.append("Horse3")

        win.update()
        # winners can be one or two or three
        if len(winners) >= 1 :
            break

    if len(winners) == 1 :
        print(f"{winners[0]} is the winner ")

    elif len(winners) == 2 :
        print(f"Tie {winners[0]} with {winners[1]} ")

    elif len(winners) == 3 :
        print(f"Tie {winners[0]} with {winners[1]} with {winners[2]} ")




    win.update()
    #click window to close
    win.getMouse()
    win.close()




if __name__ == "__main__":
    main()
