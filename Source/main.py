import tkinter as tk
from Caesar import *
from Affine import *
from KeywordSubstitution import *
from Vigenere import *
from Beaufort import *
from PolyalphabeticAffine import *
from Autokey import *
from IndexOfCoincidence import *
from FrequencyAnalysis import *
from Playfair import *
from DetectEnglish import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Page(tk.Frame):
    def __init__(self,name, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.page_name = name
        self.output_text = None
        
    def show(self):
        self.lift()

    def get_page_name(self):
        return self.page_name

    def show_plaintext(self,plaintext):
        if self.output_text == None:
            self.output_text = tk.Text(self,height=5,width=56)
            self.output_text.pack()
        self.output_text.delete("1.0","end")
        self.output_text.insert("end",plaintext)


class PageFrequency(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, "Frequency Analysis",*args, **kwargs)

       self.submit = tk.Button(self,text="Submit",command=self.Decode)
       self.submit.pack()

   def Decode(self):
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       freqs = FrequencyAnalysis(ciphertext)
       sorted_freqs = sorted(freqs,key=lambda x:x[1], reverse=True)
       freq_text = ""
       for i in range(len(sorted_freqs)):
           freq_text += sorted_freqs[i][0] + ":" + str(sorted_freqs[i][1]) + " "
           if i == len(sorted_freqs)//2:
               freq_text += "\n"
       tk.Label(self,text=freq_text).pack()
       graph_frame = tk.Frame(self)
       graph_frame.pack()
       x = []
       y = []
       for pair in freqs:
           x.append(pair[0])
           y.append(pair[1])
       f = Figure(figsize=(5,5), dpi=100)
       a = f.add_subplot(111)
       a.bar(x,y)
       canvas = FigureCanvasTkAgg(f, graph_frame)
       canvas.draw()
       canvas.get_tk_widget().pack()

class PageIOC(Page): #IOC
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Index Of Coincidence",*args, **kwargs)

       self.submit = tk.Button(self,text="Find IOC",command=self.Decode)
       self.submit.pack()

   def Decode(self):
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       ioc = IOC(ciphertext)
       ioc_text = "Index of coincidence: {}".format(ioc)
       tk.Label(self,text=ioc_text).pack()

class PageKeyLength(Page): #Calculate key length
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Calculate Key Length",*args, **kwargs)

       self.submit = tk.Button(self,text="Find key length",command=self.Decode)
       self.submit.pack()

   def Decode(self):
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       key_lengths = CalculateKeyLength(ciphertext)
       key_length_text = ""
       for length in key_lengths:
           key_length_text += "Key length {}, IOC {}\n".format(length[0],length[1])
       tk.Label(self,text=key_length_text).pack()

class PageCaesar(Page):  #Caesar
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Caesar Shift", *args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       tk.Label(frame1,text="Shift").pack(side="left")
       self.key = tk.IntVar()
       self.shift = tk.Scale(frame1, variable=self.key, from_=0, to=26, orient="horizontal")
       self.shift.pack(side="left")

       frame_check_button = tk.Frame(self)
       frame_check_button.pack()

       self.bruteforce = tk.IntVar()
       self.bruteforce_button = tk.Checkbutton(frame_check_button,variable=self.bruteforce,text="Bruteforce")
       self.bruteforce_button.pack()

       SubmitButtons(self)
       
   def Decode(self):
       key = self.shift.get()
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       bruteforce = self.bruteforce.get()
       if bruteforce == 0:
           plaintext = CaesarDecode(ciphertext,key)
       else:
           plaintext = CaesarBruteforce(ciphertext)
       self.show_plaintext(plaintext)

   def Encode(self):
       key = self.shift.get()
       plaintext = main.input_text.get("1.0","end").strip().lower()
       ciphertext = CaesarEncode(plaintext,key)
       self.show_plaintext(ciphertext)

class PageAffine(Page): #Affine
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Affine Shift", *args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       self.a = tk.IntVar()
       self.b = tk.IntVar()
       self.aslider = tk.Scale(frame1, variable=self.a, from_=0, to=26, orient="horizontal",label="a")
       self.bslider = tk.Scale(frame1, variable=self.b, from_=0, to=26, orient="horizontal",label="b")
       self.aslider.pack(side="left")
       self.bslider.pack(side="left")

       frame_check_button = tk.Frame(self)
       frame_check_button.pack()

       self.bruteforce = tk.IntVar()
       self.bruteforce_button = tk.Checkbutton(frame_check_button,variable=self.bruteforce,text="Bruteforce")
       self.bruteforce_button.pack()

       SubmitButtons(self)

   def Decode(self):
       a = self.a.get()
       b = self.b.get()
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       bruteforce = self.bruteforce.get()
       if bruteforce == 0:
           plaintext = AffineDecode(ciphertext,a,b)
       else:
           plaintext = AffineBruteforce(ciphertext)
       self.show_plaintext(plaintext)

   def Encode(self):
       a = self.a.get()
       b = self.b.get()
       plaintext = main.input_text.get("1.0","end").strip().lower()
       ciphertext = AffineEncode(plaintext,key)
       self.show_plaintext(ciphertext)

class PageKeywordSub(Page): #Keyword Substitution
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Keyword Substitution",*args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       self.keyword_entry = tk.Entry(frame1)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Keyword")

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       plaintext = KeywordSubstitutionDecode(ciphertext,keyword)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = main.input_text.get("1.0","end").strip().lower()
       ciphertext = KeywordSubstitutionEncode(plaintext,keyword)
       self.show_plaintext(ciphertext)

class PageVigenere(Page): #Vigenere
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Vigenere",*args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       self.keyword_entry = tk.Entry(frame1)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Key")

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       plaintext = VigenereDecode(ciphertext,keyword)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = main.input_text.get("1.0","end").strip().lower()
       ciphertext = VigenereEncode(plaintext,keyword)
       self.show_plaintext(ciphertext)

class PageBeaufort(Page): #Beaufort
   def __init__(self, *args, **kwargs):
       Page.__init__(self, "Beaufort",*args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       self.keyword_entry = tk.Entry(frame1)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Key")

       frame_check_button = tk.Frame(self)
       frame_check_button.pack()

       self.german = tk.IntVar()
       self.german_button = tk.Checkbutton(frame_check_button,variable=self.german,text="German Variant")
       self.german_button.pack()

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       german_variant = self.german.get()
       if german_variant == 0:
           plaintext = BeaufortDecode(ciphertext,keyword)
       else:
           plaintext = BeaufortDecode(ciphertext,keyword,german=True)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = main.input_text.get("1.0","end").strip().lower()
       german_variant = self.german.get()
       if german_variant == 0:
           ciphertext = BeaufortEncode(plaintext,keyword)
       else:
           ciphertext = BeaufortEncode(plaintext,keyword,german=True)
       self.show_plaintext(ciphertext)

class PagePolyAffine(Page): #PolyAffine
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Polyalphabetic Affine",*args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       self.keys_entry = tk.Entry(frame1)
       self.keys_entry.pack()
       self.keys_entry.insert("end","|a1,b1|a2,b2|...|")

       SubmitButtons(self)

   def Decode(self):
       keys = self.keys_entry.get()
       keys = keys.split("|")
       keys = [x for x in keys if x]
       affine_keys = []
       for key in keys:
           affine_keys.append(list(map(int(key.split(",")))))
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       plaintext = PolyAffineDecode(ciphertext,affine_keys)
       self.show_plaintext(plaintext)

   def Encode(self):
       keys = self.keys_entry.get()
       keys = keys.split("|")
       keys = [x for x in keys if x]
       affine_keys = []
       for key in keys:
           affine_keys.append(list(map(int(key.split(",")))))
       plaintext = main.input_text.get("1.0","end").strip().lower()
       ciphertext = PolyAffineEncode(plaintext,affine_keys)
       self.show_plaintext(ciphertext)

class PageAutokey(Page): #Autokey
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Autokey",*args, **kwargs)

       self.keyword_entry = tk.Entry(self)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Key")

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       plaintext = AutokeyDecode(ciphertext,keyword)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = main.input_text.get("1.0","end").strip().lower()
       ciphertext = AutokeyEncode(plaintext,keyword)
       self.show_plaintext(ciphertext)

class PagePlayfair(Page): #Playfair
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Playfair",*args, **kwargs)

       self.keyword_entry = tk.Entry(self)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Keyword")

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       plaintext = PlayfairDecode(ciphertext,keyword)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = main.input_text.get("1.0","end").strip().lower()
       ciphertext = PlayfairEncode(plaintext,keyword)
       self.show_plaintext(ciphertext)
       
def SubmitButtons(self):
    frame2 = tk.Frame(self)
    frame2.pack()

    self.encrypt_button = tk.Button(frame2,text="Encrypt",command=self.Encode)
    self.encrypt_button.pack(side="left")
   
    self.decrypt_button = tk.Button(frame2,text="Decrypt",command=self.Decode)
    self.decrypt_button.pack(side="left")

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pages = [
        PageFrequency(self),
        PageIOC(self),
        PageKeyLength(self),
        PageCaesar(self),
        PageAffine(self),
        PageKeywordSub(self),
        PageVigenere(self),
        PageBeaufort(self),
        PagePolyAffine(self),
        PageAutokey(self),
        PagePlayfair(self)
        ]

        container = tk.Frame(self)
        
        for page in self.pages:
            page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            

        self.input_text = tk.Text(self,height=5,width=56)
        self.input_text.pack()

        self.TOOLS = []
        for page in self.pages:
            self.TOOLS.append(page.get_page_name())
        self.control_variable = tk.StringVar(self)
        self.control_variable.set(self.TOOLS[0])
        self.tool = tk.OptionMenu(self,self.control_variable, *self.TOOLS,command=self.change_page)
        self.tool.pack()

        self.change_page()
        container.pack(fill="both", expand=True)

    def change_page(self, *args, **kwargs):
        selected_page = self.control_variable.get()
        root.title("Cryptobreaker | {}".format(selected_page))
        for page in self.pages:
            if selected_page == page.get_page_name():
                page.show()
                break


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
