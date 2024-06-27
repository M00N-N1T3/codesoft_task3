# from lib import tkinter as tk
import tkinter as tk

DEFAULT_FONT = ("Arial",16)

class Calculator:


    def __init__(self):

        self.string = ""
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("300x430")
        self.root.minsize(width=300,height=430)
        self.root.maxsize(width=300,height=430)


        # self.screen.pack(padx=6,pady=6,expand=False,side=tk.TOP)

        self.aux_frame = tk.Frame(self.root)
        self.screen_frame = tk.Frame(self.aux_frame)

        # self.screen = tk.Text(self.a,font=("Arial",32),width = 11,height=1,border=2)
        self.screen = tk.Entry(self.screen_frame,font=("Arial",32),width=11)
        self.screen.focus_set()
        self.screen.bind("<KeyPress>",self.handle_input)

        self.screen.grid(row=0,padx=3,pady=2,columnspan=5)
        self.screen_frame.pack(expand=True,fill="both")
        # self.screen.pack(padx=6,pady=6,expand=False,fill="both")

        self.button_frame = tk.Frame(self.aux_frame)


        self.memory_clear = button_layout(self.button_frame,0,0,"MC")
        self.memory_plus = button_layout(self.button_frame,1,0,"M+")
        self.memory_minus = button_layout(self.button_frame,2,0,"M-")
        self.memory_recall = button_layout(self.button_frame,3,0,"MR")

        self.clicked_button = tk.IntVar(self.button_frame)

        self.clear= button_layout(self.button_frame,0,1,"C",self.clear_screen)
        self.divide = button_layout(self.button_frame,1,1,"/",lambda: self.clicked("/"))
        self.multiply= button_layout(self.button_frame,2,1,"X",lambda: self.clicked("x"))
        self.delete= button_layout(self.button_frame,3,1,"\u2190")

        self.seven= button_layout(self.button_frame,0,2,"7",lambda: self.clicked("7"))
        self.eight = button_layout(self.button_frame,1,2,"8",lambda: self.clicked("8"))
        self.nine= button_layout(self.button_frame,2,2,"9",lambda: self.clicked("9"))
        self.minus= button_layout(self.button_frame,3,2,"-",lambda: self.clicked("-"))


        self.four= button_layout(self.button_frame,0,3,"4",lambda: self.clicked("4"))
        self.five= button_layout(self.button_frame,1,3,"5",lambda: self.clicked("5"))
        self.six= button_layout(self.button_frame,2,3,"6",lambda: self.clicked("6"))
        self.plus= button_layout(self.button_frame,3,3,"+",lambda: self.clicked("+"))

        self.one= button_layout(self.button_frame,0,4,"1",lambda: self.clicked("1"))
        self.two= button_layout(self.button_frame,1,4,"2",lambda: self.clicked("2"))
        self.three= button_layout(self.button_frame,2,4,"3",lambda: self.clicked("3"))

        self.percent= button_layout(self.button_frame,0,5,"%")
        self.zero= button_layout(self.button_frame,1,5,"0",lambda: self.clicked("0"))
        self.comma= button_layout(self.button_frame,2,5,",",lambda: self.clicked(","))

        self.equal = tk.Button(self.button_frame,height=5,width=4,text="=",border=2)
        self.equal.grid(column=3,row=4,rowspan=2)


        self.button_frame.pack(expand=False,fill="both")

        self.aux_frame.pack(expand=False,fill="both",padx=10)


        self.root.mainloop()


    def calculator_string(self,text: str):
        self.string = self.string + text

    def clear_screen(self):
        try:
            self.screen.delete("0",tk.END)
        except tk.TclError as e:
            e.add_note("Nothing on the screen")
            print(e)

    def handle_input(self,event):
        accepted = ['1','2','3','4','5','6','7','8','9','0',"+",'-',','
                    ,"BackSpace","Return","KP_Add","KP_Subtract","minus","plus",
                    "\u2190","Right","Left","KP_1","KP_2","KP_3","KP_4","KP_5","KP_6"
                    ,"KP_7","KP_8","KP_9","KP_0","Delete"]

        # self.screen.configure(state=["normal"])
        print(event)
        if not event.keysym in accepted:
            self.screen.configure(state=["disabled"], disabledbackground='white', disabledforeground='Black')
        else:
            self.screen.configure(state=["normal"],disabledbackground="White",foreground="Black",background="White",disabledforeground="Black")

    def clicked(self,text):
        char_on_screen = self.screen.get()
        self.screen.focus_force()
        self.screen.insert(len(char_on_screen),text)
        self.screen.xview_moveto(1)


class button_layout:
    """
    Creates a single button widget for you
    Args:
        frame (tk.Frame): the frame the button belongs to
    """

    def __init__(self,frame:tk.Frame ,column: int,row: int,text:str,command: tk.COMMAND = None,variable :tk.Variable = None):
        btn = tk.Button(frame,height=2,width=4,text=text,command=command,border=2)
        btn.grid(column=column, row=row,padx=4,pady=4)
    pass



if __name__ == "__main__":
    calc = Calculator()

