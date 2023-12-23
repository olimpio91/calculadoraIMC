from tkinter import *

class App(Tk):
    def __init__(self,title,geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.minsize(width=400,height=200)
        self.configure(background="#A6B1E1")
        self.mainFrame()
        self.entrys()
        self.labels()
        self.buttons()


    def mainFrame(self):
        self.frame = Frame(self,bd=1, highlightbackground="#546A7B", highlightthickness=2)
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    
    def entrys(self):
        self.labelTitle = Label(self.frame, text="CALCULADORA DE IMC", font=("Roboto", 18))
        self.labelTitle.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.2)

        self.entryAltura = Entry(self.frame)
        self.entryAltura.place(relx=0.18, rely=0.45, relwidth=0.2, relheight=0.12)

        self.entryPeso = Entry(self.frame)
        self.entryPeso.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.12)

        self.entryResultado = Entry(self.frame)
        self.entryResultado.place(relx=0.62, rely=0.45, relwidth=0.2, relheight=0.12)

    def labels(self):
        self.labelAltura = Label(self.frame, text="altura")
        self.labelAltura.place(relx=0.01, rely=0.35, relwidth=0.45, relheight=0.1)

        self.labelPeso = Label(self.frame, text="Peso")
        self.labelPeso.place(relx=0.4, rely=0.35, relwidth=0.1, relheight=0.1)

        self.labelResultado = Label(self.frame, text="Resultado")
        self.labelResultado.place(relx=0.62, rely=0.35, relwidth=0.15, relheight=0.1)

        self.labelInfo = Label(self.frame, font=("Roboto", 10))
        self.labelInfo.place(relx=0.25, rely=0.57, relwidth=0.5, relheight=0.1)

    def buttons(self):
        self.buttonResultado = Button(self.frame, text="Calcular", command=self.calcular)
        self.buttonResultado.place(relx=0.3, rely=0.7, relwidth=0.2, relheight=0.15)

        self.buttonLimpar = Button(self.frame, text="Limpar", command=self.limpar)
        self.buttonLimpar.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.15)

    #evento calcular IMC com base Peso e altura.
    def calcular(self):
        altura = float(self.entryAltura.get())
        peso = float(self.entryPeso.get())
        imc = peso / (altura ** 2)
        self.entryResultado.insert(0,'{:.2f}'.format(imc))
        
        if imc < 17:
            self.labelInfo.configure(text=" Muito abaixo do peso",fg="#9e2a2b")
        elif 17 < imc < 18.49:
            self.labelInfo.configure(text="Abaixo do peso",fg="#faa307")
        elif 15.5 < imc < 24.99:
            self.labelInfo.configure(text="Peso normal",fg="#55a630")
        elif 25 < imc < 29.99:
            self.labelInfo.configure(text="Acima do peso",fg="#faa307")
        else:
            self.labelInfo.configure(text="Obsidade",fg="red")


    def limpar(self):
        self.entryAltura.delete(0,"end")
        self.entryPeso.delete(0,"end")
        self.entryResultado.delete(0,"end")
        self.labelInfo.configure(text="")

janela = App("Calculadora de IMC", '400x200')
janela.mainloop()