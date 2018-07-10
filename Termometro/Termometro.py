import serial
from tkinter import *
import math
ser=serial.Serial("COM3",9600)


class Main_Window:
    def __init__(self):
        global Window
        global Window_2
        global ser
        global Temp_Lim1
        global Temp_Lim2
        global Temp_Lim3
        global Temp_Lim4
        global Closer

        Window_2=Tk()

        Main_Frame=Frame(Window_2)
        Lim_Frame=Frame(Window_2)
        Button_Frame=Frame(Window_2)
        Main_Frame.pack()
        Lim_Frame.pack()
        Button_Frame.pack(side=RIGHT)

        self.Temp_label=Label(Main_Frame,text="A temperatura actual é:")
        self.Temp_label.pack()

        self.Lim_Label=Label(Lim_Frame,text="Os limites de temperatura definidos:\n"+str(Temp_Lim1)+"ºC\n"+str(Temp_Lim2)+"ºC\n"+str(Temp_Lim3)+"ºC\n"+str(Temp_Lim4)+"ºC\n")
        self.Lim_Label.pack()

        self.Quit_Button=Button(Button_Frame,text="Fechar",command=self.Window_Close)
        self.Quit_Button.pack(side=RIGHT)

        self.Lim_Def=Button(Button_Frame,text="Definir os Limites",command=self.DefLim)
        self.Lim_Def.pack(side=RIGHT)

        Temp=int(ser.readline())
        self.Temperature=Label(Main_Frame,text=str(Temp)+"ºC")
        self.Temperature.pack()

        while Closer:
            Temp=int(ser.readline())
            Temp=(5*Temp)/1023
            I=(5-Temp)/(4700+5050)
            R=Temp/I
            R_NTC=-1/((1/R)-(1/560))
            if(R_NTC<1200 or R_NTC>16000):
                Temp=1/(math.log(R_NTC/0.010058)/3898.2)
            else:
                Temp=1/((math.log(R_NTC/5000)+(1/298.15))/3907.632)
            Temp=int(Temp)-273.15
            if(Temp<Temp_Lim1):
                valor_arduino="1"
            elif(Temp<Temp_Lim2):
                valor_arduino="2"
            elif(Temp<Temp_Lim3):
                valor_arduino="3"
            elif(Temp<Temp_Lim4):
                valor_arduino="4"
            else:
                valor_arduino="5"
            ser.write(valor_arduino.encode())
            self.Temperature.destroy()
            self.Temperature=Label(Main_Frame,text=str(Temp)+"ºC")
            self.Temperature.pack()

            Window_2.update_idletasks()
            Window_2.update()
    def Window_Close(self):
        global Window_2
        global Closer

        Closer=False
        Window_2.destroy()
        
    def DefLim(self):
        global Window
        global Window_2
        global Closer

        Closer=False
        Window_2.destroy()
        Window=Tk()
        Start=DefLim_Window()


class DefLim_Window:
    def __init__(self):
        global Window
        global Temp_Lim1
        global Temp_Lim2
        global Temp_Lim3
        global Temp_Lim4

        Title_Frame=Frame(Window)
        DefLim_Frame1=Frame(Window)
        DefLim_Frame2=Frame(Window)
        Button_Frame=Frame(Window)
        self.Aviso_Frame=Frame(Window)
        
        Title_Frame.pack()
        DefLim_Frame1.pack()
        DefLim_Frame2.pack()
        self.Aviso_Frame.pack()
        Button_Frame.pack(side=RIGHT)

        self.Title_Label=Label(Title_Frame,text="Introduza o valor e carregue no botão para definir:")
        self.Title_Label.pack()

        self.Button_Def_Temp1=Button(DefLim_Frame1,text="Definir Limite 1",command=self.GetLim1)
        self.Button_Def_Temp1.pack(side=LEFT)

        self.Entry_Def_Temp1=Entry(DefLim_Frame1)
        self.Entry_Def_Temp1.pack(side=LEFT)

        self.Button_Def_Temp2=Button(DefLim_Frame1,text="Definir Limite 2",command=self.GetLim2)
        self.Button_Def_Temp2.pack(side=LEFT)

        self.Entry_Def_Temp2=Entry(DefLim_Frame1)
        self.Entry_Def_Temp2.pack(side=LEFT)

        self.Button_Def_Temp3=Button(DefLim_Frame2,text="Definir Limite 3",command=self.GetLim3)
        self.Button_Def_Temp3.pack(side=LEFT)

        self.Entry_Def_Temp3=Entry(DefLim_Frame2)
        self.Entry_Def_Temp3.pack(side=LEFT)

        self.Button_Def_Temp4=Button(DefLim_Frame2,text="Definir Limite 4",command=self.GetLim4)
        self.Button_Def_Temp4.pack(side=LEFT)

        self.Entry_Def_Temp4=Entry(DefLim_Frame2)
        self.Entry_Def_Temp4.pack(side=LEFT)

        self.Aviso_Label=Label(self.Aviso_Frame,text="")
        self.Aviso_Label.pack()

        self.Quit_Button=Button(Button_Frame,text="Fechar",command=Window.destroy)
        self.Quit_Button.pack(side=RIGHT)

        self.Main_Button=Button(Button_Frame,text="Próximo",command=self.Go_To_Main)
        self.Main_Button.pack(side=RIGHT)

        Window.mainloop()

    def GetLim1(self):
        global Temp_Lim1
        global Temp_Lim2
        global Temp_Lim3
        global Temp_Lim4

        Cofre=Temp_Lim1
        Temp_Lim1=int(self.Entry_Def_Temp1.get())
        Teste=True

        if(Temp_Lim2!=-40):
            if(Temp_Lim2<Temp_Lim1):
                Teste=False
        if(Temp_Lim3!=-40):
            if(Temp_Lim3<Temp_Lim1):
                Teste=False
        if(Temp_Lim4!=-40):
            if(Temp_Lim4<Temp_Lim1):
                Teste=False
        if(Temp_Lim1<-40 or Temp_Lim1>125):
            Teste=False
        if(Teste):
            self.Aviso_Label.destroy()
            self.Aviso_Label=Label(self.Aviso_Frame,text="O limite 1 é bem definido!")
            self.Aviso_Label.pack()
        else:
            self.Aviso_Label.destroy()
            self.Aviso_Label=Label(self.Aviso_Frame,text="O limite que tentou definir não é válido!")
            self.Aviso_Label.pack()
            Temp_Lim1=Cofre

    def GetLim2(self):
        global Temp_Lim1
        global Temp_Lim2
        global Temp_Lim3
        global Temp_Lim4

        Cofre=Temp_Lim2
        Temp_Lim2=int(self.Entry_Def_Temp2.get())
        Teste=True

        if(Temp_Lim1!=-40):
            if(Temp_Lim2<Temp_Lim1):
                Teste=False
        if(Temp_Lim3!=-40):
            if(Temp_Lim3<Temp_Lim2):
                Teste=False
        if(Temp_Lim4!=-40):
            if(Temp_Lim4<Temp_Lim2):
                Teste=False
        if(Temp_Lim2<-40 or Temp_Lim2>125):
            Teste=False
        if(Teste):
            self.Aviso_Label.destroy()
            self.Aviso_Label=Label(self.Aviso_Frame,text="O limite 2 é bem definido!")
            self.Aviso_Label.pack()
        else:
            self.Aviso_Label.destroy()
            self.Aviso_Label=Label(self.Aviso_Frame,text="O limite que tentou definir não é válido!")
            self.Aviso_Label.pack()

            Temp_Lim2=Cofre
                
    def GetLim3(self):
        global Temp_Lim1
        global Temp_Lim2
        global Temp_Lim3
        global Temp_Lim4

        Cofre=Temp_Lim3
        Temp_Lim3=int(self.Entry_Def_Temp3.get())
        Teste=True

        if(Temp_Lim1!=-40):
            if(Temp_Lim3<Temp_Lim1):
                Teste=False
        if(Temp_Lim2!=-40):
            if(Temp_Lim3<Temp_Lim2):
                Teste=False
        if(Temp_Lim4!=-40):
            if(Temp_Lim4<Temp_Lim3):
                Teste=False
        if(Temp_Lim3<-40 or Temp_Lim3>125):
            Teste=False
        if(Teste):
            self.Aviso_Label.destroy()
            self.Aviso_Label=Label(self.Aviso_Frame,text="O limite 3 é bem definido!")
            self.Aviso_Label.pack()
        else:
            self.Aviso_Label.destroy()
            self.Aviso_Label=Label(self.Aviso_Frame,text="O limite que tentou definir não é válido!")
            self.Aviso_Label.pack()

            Temp_Lim3=Cofre
                                
    def GetLim4(self):
        global Temp_Lim1
        global Temp_Lim2
        global Temp_Lim3
        global Temp_Lim4

        Cofre=Temp_Lim4
        Temp_Lim4=int(self.Entry_Def_Temp4.get())
        Teste=True

        if(Temp_Lim1!=-40):
            if(Temp_Lim4<Temp_Lim1):
                Teste=False
        if(Temp_Lim2!=-40):
            if(Temp_Lim4<Temp_Lim2):
                Teste=False
        if(Temp_Lim3!=-40):
            if(Temp_Lim4<Temp_Lim3):
                Teste=False
        if(Temp_Lim4<-40 or Temp_Lim4>125):
            Teste=False
        if(Teste):
            self.Aviso_Label.destroy()
            self.Aviso_Label=Label(self.Aviso_Frame,text="O limite 4 é bem definido!")
            self.Aviso_Label.pack()
        else:
            self.Aviso_Label.destroy()
            self.Aviso_Label=Label(self.Aviso_Frame,text="O limite que tentou definir não é válido!")
            self.Aviso_Label.pack()

            Temp_Lim4=Cofre

    def Go_To_Main(self):
        global Window
        global Closer
        global Temp_Lim1
        global Temp_Lim2
        global Temp_Lim3
        global Temp_Lim4

        if(Temp_Lim2==-40 or Temp_Lim3==-40 or Temp_Lim4==-40):
            self.Aviso_Label.destroy()
            if(Temp_Lim2==-40):
                Alerta2=" 2"
            if(Temp_Lim3==-40):
                Alerta3=" 3"
            if(Temp_Lim4==-40):
                Alerta4=" 4"
            self.Aviso_Label=Label(self.Aviso_Frame,text="Por Favor defina todos os limites.\n"+"Não tem os limites"+Alerta2+Alerta3+Alerta4+" definido!")
            self.Aviso_Label.pack()
        else:
            Window.destroy()
            Closer=True
            Start=Main_Window()
        
Temp_Lim1=-40
Temp_Lim2=-40
Temp_Lim3=-40
Temp_Lim4=-40
Closer=True

Window=Tk()
Start=DefLim_Window()
