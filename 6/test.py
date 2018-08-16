#coding: UTF-8
if __name__ == '__main__':
        from Tkinter import *
        root = Tk()
        root.title('Canvas')
        canvas = Canvas(root,width = 400,height = 400,bg='green')
        x0 = 0
        y0 = 100
        x1 = 100
        y1 = 0
        for i in range(3):
            x0 +=5
            y0 -=5
            x1 -=5
            y1 -=5
            canvas.create_rectangle(x0,y0,x1,y1)
canvas.pack()
root.mainloop()
