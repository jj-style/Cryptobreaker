import tkinter as tk
from Caesar import *
from Affine import *
from ColumnTransposition import *
from Railfence import *
from KeywordSubstitution import *
from Vigenere import *
from Beaufort import *
from PolyalphabeticAffine import *
from Autokey import *
from IndexOfCoincidence import *
from FrequencyAnalysis import *
from Playfair import *
from DetectEnglish import *
from DictionaryBruteforce import *

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

    def read_in_text(self):
        in_text = main.input_text.get("1.0","end").strip().lower()
        try:
            punct_choice = self.punctuation_option.get()        
            if punct_choice == self.punct_options[0]:
                return in_text
            elif punct_choice == self.punct_options[1]:
                return RemovePunctuation(in_text,remove_spaces=False)
            else:
                return RemovePunctuation(in_text)
        except:
            return RemovePunctuation(in_text)
        
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
       if len(key_lengths) != 0:
           key_length_text = ""
           for length in key_lengths:
               key_length_text += "Key length {}, IOC {}\n".format(length[0],length[1])
       else:
           key_length = GetKeyLength(ciphertext)
           key_length_text = "Key length {} (+- 1)\n".format(key_length)
       tk.Label(self,text=key_length_text).pack()

class PageReverseText(Page): #Calculate key length
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Reverse Text",*args, **kwargs)

       self.submit = tk.Button(self,text="Reverse text",command=self.Decode)
       self.submit.pack()

   def Decode(self):
       text = main.input_text.get("1.0","end").strip().lower()
       reversed_text = text[::-1]
       self.show_plaintext(reversed_text)
       

class PageCaesar(Page):  #Caesar
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Caesar Shift", *args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       tk.Label(frame1,text="Shift").pack(side="left")
       self.key = tk.IntVar()
       self.shift = tk.Scale(frame1, variable=self.key, from_=0, to=26, orient="horizontal")
       self.shift.pack(side="left")

       BruteforceButton(self)
       RemovePunctuationMenu(self)

       SubmitButtons(self)
       
   def Decode(self):
       key = self.shift.get()
       ciphertext = self.read_in_text()
       bruteforce = self.bruteforce.get()
       if bruteforce == 0:
           plaintext = CaesarDecode(ciphertext,key)
       else:
           plaintext = CaesarBruteforce(ciphertext)
       self.show_plaintext(plaintext)

   def Encode(self):
       key = self.shift.get()
       plaintext = self.read_in_text()
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

       BruteforceButton(self)
       RemovePunctuationMenu(self)

       SubmitButtons(self)

   def Decode(self):
       a = self.a.get()
       b = self.b.get()
       ciphertext = self.read_in_text()
       bruteforce = self.bruteforce.get()
       if bruteforce == 0:
           plaintext = AffineDecode(ciphertext,a,b)
       else:
           plaintext = AffineBruteforce(ciphertext)
       self.show_plaintext(plaintext)

   def Encode(self):
       a = self.a.get()
       b = self.b.get()
       plaintext = self.read_in_text()
       ciphertext = AffineEncode(plaintext,a,b)
       self.show_plaintext(ciphertext)

class PageColumnTransposition(Page):  #Column Transposition
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Column Transposition", *args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       self.keyword_entry = tk.Entry(frame1)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Keyword or permutation (e.g. 2,1,3)")

       self.regular = tk.IntVar()
       self.regular_button = tk.Checkbutton(frame1,variable=self.regular,text="Regular")
       self.regular_button.pack()

       SubmitButtons(self)
       
   def Decode(self):
       keyword = self.keyword_entry.get().strip().lower()
       ciphertext = self.read_in_text()
       ciphertext = RemovePunctuation(ciphertext)
       plaintext = TranspositionDecode(ciphertext,keyword)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().strip().lower()
       plaintext = self.read_in_text()
       plaintext = RemovePunctuation(plaintext)
       if self.regular.get() == 1:
           ciphertext = TranspositionEncode(plaintext,keyword,regular=True)
       else:
           ciphertext = TranspositionEncode(plaintext,keyword)
       self.show_plaintext(ciphertext)

class PageRailfence(Page):  #Railfence
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Railfence", *args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       tk.Label(frame1,text="Number of lines").pack(side="left")
       self.lines = tk.IntVar()
       self.lines_scale = tk.Scale(frame1, variable=self.lines, from_=1, to_=50,orient="horizontal")
       self.lines_scale.pack(side="left",fill="x",expand=True)
       
       SubmitButtons(self)
       
   def Decode(self):
       lines = self.lines.get()
       ciphertext = self.read_in_text()
       plaintext = RailfenceDecode(ciphertext,lines)
       self.show_plaintext(plaintext)

   def Encode(self):
       lines = self.lines.get()
       plaintext = self.read_in_text()
       ciphertext = RailfenceEncode(plaintext,lines)
       self.show_plaintext(ciphertext)

class PageKeywordSub(Page): #Keyword Substitution
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Keyword Substitution",*args, **kwargs)

       frame1 = tk.Frame(self)
       frame1.pack()

       self.keyword_entry = tk.Entry(frame1)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Keyword")

       self.shift = tk.IntVar()
       self.shift_slider = tk.Scale(frame1, variable=self.shift, from_=0, to=26, orient="horizontal",label="alphabet shift")
       self.shift_slider.pack(side="left")

       BruteforceButton(self)
       RemovePunctuationMenu(self)

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = self.read_in_text()
       bruteforce = self.bruteforce.get()
       shift = self.shift.get()
       if bruteforce == 0:
           plaintext = KeywordSubstitutionDecode(ciphertext,keyword,default_alph_shift=shift)
       else:
           plaintext, key_used = BruteforceDictionaryAttack(ciphertext,self.get_page_name(),alph_shift=shift)
           self.keyword_entry.delete("0","end")
           self.keyword_entry.insert("end",key_used)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = self.read_in_text()
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

       BruteforceButton(self)
       RemovePunctuationMenu(self)

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = self.read_in_text()
       bruteforce = self.bruteforce.get()
       if bruteforce == 0:
           plaintext = VigenereDecode(ciphertext,keyword)
       else:
           plaintext, key_used = BruteforceDictionaryAttack(ciphertext,self.get_page_name())
           self.keyword_entry.delete("0","end")
           self.keyword_entry.insert("end",key_used)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = self.read_in_text()
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

       self.german = tk.IntVar()
       self.german_button = tk.Checkbutton(frame1,variable=self.german,text="German Variant")
       self.german_button.pack()

       BruteforceButton(self)
       RemovePunctuationMenu(self)

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = self.read_in_text()
       german_variant = self.german.get()
       bruteforce = self.bruteforce.get()
       if german_variant == 0:
           if bruteforce == 0:
               plaintext = BeaufortDecode(ciphertext,keyword)
           else:
               plaintext, key_used = BruteforceDictionaryAttack(ciphertext,self.get_page_name())
               self.keyword_entry.delete("0","end")
               self.keyword_entry.insert("end",key_used)
       else:
           if bruteforce == 0:
               plaintext = BeaufortDecode(ciphertext,keyword,german=True)
           else:
               plaintext, key_used = BruteforceDictionaryAttack(ciphertext,self.get_page_name(),german=True)
               self.keyword_entry.delete("0","end")
               self.keyword_entry.insert("end",key_used)
           
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = self.read_in_text()
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

       RemovePunctuationMenu(self)

       SubmitButtons(self)

   def Decode(self):
       keys = self.keys_entry.get()
       keys = keys.split("|")
       keys = [x for x in keys if x]
       affine_keys = []
       for key in keys:
           affine_keys.append(list(map(int,key.split(","))))
       ciphertext = self.read_in_text()
       plaintext = PolyAffineDecode(ciphertext,affine_keys)
       self.show_plaintext(plaintext)

   def Encode(self):
       keys = self.keys_entry.get()
       keys = keys.split("|")
       keys = [x for x in keys if x]
       affine_keys = []
       for key in keys:
           affine_keys.append(list(map(int,key.split(","))))
       plaintext = self.read_in_text()
       ciphertext = PolyAffineEncode(plaintext,affine_keys)
       self.show_plaintext(ciphertext)

class PageAutokey(Page): #Autokey
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Autokey",*args, **kwargs)

       self.keyword_entry = tk.Entry(self)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Key")

       BruteforceButton(self)
       RemovePunctuationMenu(self)

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = self.read_in_text()
       bruteforce = self.bruteforce.get()
       if bruteforce == 0:
           plaintext = AutokeyDecode(ciphertext,keyword)
       else:
           plaintext, key_used = BruteforceDictionaryAttack(ciphertext,self.get_page_name())
           self.keyword_entry.delete("0","end")
           self.keyword_entry.insert("end",key_used)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = self.read_in_text()
       ciphertext = AutokeyEncode(plaintext,keyword)
       self.show_plaintext(ciphertext)

class PagePlayfair(Page): #Playfair
   def __init__(self, *args, **kwargs):
       Page.__init__(self,"Playfair",*args, **kwargs)

       self.keyword_entry = tk.Entry(self)
       self.keyword_entry.pack()
       self.keyword_entry.insert("end","Keyword")

       BruteforceButton(self)

       SubmitButtons(self)

   def Decode(self):
       keyword = self.keyword_entry.get().lower()
       ciphertext = main.input_text.get("1.0","end").strip().lower()
       ciphertext = RemovePunctuation(ciphertext)
       bruteforce = self.bruteforce.get()
       if bruteforce == 0:
           plaintext = PlayfairDecode(ciphertext,keyword)
       else:
           plaintext, key_used = BruteforceDictionaryAttack(ciphertext,self.get_page_name())
           self.keyword_entry.delete("0","end")
           self.keyword_entry.insert("end",key_used)
       self.show_plaintext(plaintext)

   def Encode(self):
       keyword = self.keyword_entry.get().lower()
       plaintext = main.input_text.get("1.0","end").strip().lower()
       plaintext = RemovePunctuation(plaintext)
       ciphertext = PlayfairEncode(plaintext,keyword)
       self.show_plaintext(ciphertext)

def BruteforceButton(self):
    frame_check_button = tk.Frame(self)
    frame_check_button.pack()
    self.bruteforce = tk.IntVar()
    self.bruteforce_button = tk.Checkbutton(frame_check_button,variable=self.bruteforce,text="Bruteforce")
    self.bruteforce_button.pack()

def RemovePunctuationMenu(self):
    self.punct_options = ["Retain punctuation and spaces","Remove punctuation and keep spaces","Remove punctuation and spaces"]
    self.punctuation_option = tk.StringVar(self)
    self.punctuation_option.set(self.punct_options[0])
    self.punctuation_menu = tk.OptionMenu(self,self.punctuation_option, *self.punct_options)
    self.punctuation_menu.pack()

    
       
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
        PageReverseText(self),
        PageCaesar(self),
        PageAffine(self),
        PageColumnTransposition(self),
        PageRailfence(self),
        PageKeywordSub(self),
        PageVigenere(self),
        PageBeaufort(self),
        PagePolyAffine(self),
        PageAutokey(self),
        PagePlayfair(self)
        ]

        self.container = tk.Frame(self)
        
        for page in self.pages:
            page.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
            

        main_frame = tk.Frame(self)
        main_frame.pack()
        self.input_text = tk.Text(main_frame,height=5)
        self.input_text.pack(fill="x")

        self.TOOLS = []
        for page in self.pages:
            self.TOOLS.append(page.get_page_name())
        self.control_variable = tk.StringVar(self)
        self.control_variable.set(self.TOOLS[0])
        self.tool = tk.OptionMenu(main_frame,self.control_variable, *self.TOOLS,command=self.change_page)
        self.tool.pack()
        
        self.change_page()
        self.container.pack(fill="both", expand=True)

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
