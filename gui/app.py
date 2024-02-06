from tkinter import *
import customtkinter
from PIL import Image,ImageOps, ImageDraw
from speech_recongnition import SpeechRecognition
from lex_yacc import *
import copy


class App(customtkinter.CTk):
  def __init__(self,title,size):
    super().__init__()
    self.configure(fg_color="#ffffff")
    self.init_setup(title,size)
    self.create_layout()
    
    
    self.run()

  def init_setup(self,title,size):
    self._set_appearance_mode("light")
    self.title(title)
    self.geometry(f"{size[0]}x{size[1]}")
    self.minsize(size[0],size[1])
  
  def create_layout(self):
    self.columnconfigure(0,weight=2,uniform="a")
    self.columnconfigure(1,weight=3,uniform="a")
    self.rowconfigure(0,weight=1,uniform="a")

    self.chatlist = ChatList(master=self)
    self.chat     = Chat(master=self)
  
  def run(self):
    self.mainloop()

class PersonaChat(customtkinter.CTkFrame):
  def __init__(self,master,path,text,name):
    super().__init__(master=master,fg_color="#ffffff",corner_radius = 0)
    frame = customtkinter.CTkFrame(master=self,fg_color="#F4F5F9")
    frame1 = customtkinter.CTkFrame(master=frame,fg_color="#F4F5F9")
    img_label = customtkinter.CTkLabel(master=frame,text="",image=path)
    name_label = customtkinter.CTkLabel(master=frame1,text=name,                                        
                                          text_color="#212121",
                                          height=20,
                                          
                                          font=("Arial",14,'bold'))
    text_label = customtkinter.CTkLabel(master=frame1,text=text,text_color="#868E96",
                                          height=20,
                                          font=("Arial",12))
    img_label.pack(side="left",padx=10)
    frame1.pack(side="top",expand=True,fill="x"),
    name_label.grid(row=0,column=0,sticky="w")
    text_label.grid(row=1,column=0,sticky="w")
    frame.pack(fill='x',padx=15,ipady=5,pady=5)

    self.pack(fill="x")

class ChatList(customtkinter.CTkFrame):
  def __init__(self,master):
    super().__init__(master=master,fg_color="#ffffff",corner_radius = 0)
    self.load_imgs()

   
    PersonaChat(self,path=self.us_persona_img,text="your proverb is correct",name="Simon")
    PersonaChat(self,path=self.ma_persona_img,text="Lmatal s7i7",name="Mohammed")
    PersonaChat(self,path=self.sp_persona_img,text="El proverbio es cierto.",name="Andriana 🇪🇸")
    PersonaChat(self,path=self.fr_persona_img,text="le proverbe est correct",name="Raphaël 🇫🇷")

    self.grid(row=0,column=0,sticky="nsew",pady=100)

  def load_imgs(self):
    self.us_persona_img = customtkinter.CTkImage(
                                  light_image=Image.open("imgs/us_persona_img.png"),
                                  dark_image=Image.open("imgs/us_persona_img.png"),
                                  size=(45, 45)
                                  )
    self.ma_persona_img = customtkinter.CTkImage(
                                  light_image=Image.open("imgs/ma_persona_img.png"),
                                  dark_image=Image.open("imgs/ma_persona_img.png"),
                                  size=(45, 45)
                                  )
    self.sp_persona_img = customtkinter.CTkImage(
                                  light_image=Image.open("imgs/sp_persona_img.png"),
                                  dark_image=Image.open("imgs/sp_persona_img.png"),
                                  size=(45, 45)
                                  )
    self.fr_persona_img = customtkinter.CTkImage(
                                  light_image=Image.open("imgs/fr_persona_img.png"),
                                  dark_image=Image.open("imgs/fr_persona_img.png"),
                                  size=(45, 45)
                                  )
    
    
class Chat(customtkinter.CTkFrame):
  def __init__(self,master):
    super().__init__(master=master,fg_color="#f4f5f9",corner_radius = 0)
    self.grid(row=0,column=1,sticky="nsew")

    self.create_frames()
    self.create_widgets()
    self.place_frames()
    self.place_widgets()

    

  def create_frames(self):
    self.header    = customtkinter.CTkFrame(master=self,corner_radius=0,fg_color="#f4f5f9")

    text_data = []
    # item_height = 60
    # self.main       = ListFrame(self,text_data,item_height)
    self.main       = ListFrame(self,text_data)
    self.bottom     = customtkinter.CTkFrame(master=self,corner_radius=0,fg_color="#f4f5f9") 
    self.separator1 = Divider(master=self)
    self.separator2 = Divider(master=self)


    

  def load_imgs(self):
    self.us_persona_img = customtkinter.CTkImage(
                                  light_image=Image.open("imgs/us_persona_img.png"),
                                  dark_image=Image.open("imgs/us_persona_img.png"),
                                  size=(45, 45)
                                  )
    self.mic_img = customtkinter.CTkImage(
                                  light_image=Image.open("imgs/icons/mic_img.png"),
                                  dark_image=Image.open("imgs/icons/mic_img.png"),
                                  size=(20, 20)
                                  )
    self.chatgroup_img = customtkinter.CTkImage(
                                  light_image=Image.open("imgs/chat-group.png"),
                                  dark_image=Image.open("imgs/chat-group.png"),
                                  size=(45, 45)
                                  )

  
  def create_widgets(self):
    self.load_imgs()

    self.header_label = customtkinter.CTkLabel(master=self.header,
                                       text="    Group Chat",
                                       font=("Arial",16),
                                       text_color="#212121",
                                       image=self.chatgroup_img,
                                       compound="left" 
                                       ) 
    self.audio_button = customtkinter.CTkLabel(master=self.bottom,image=self.mic_img,text="")
    self.audio_button.bind("<Button-1>",command=self.audio_callback)
    self.chat_input    = customtkinter.CTkEntry(master=self.bottom,
                                      border_width=0,
                                      placeholder_text="Type a message here"
                                      )
    self.submit_button = customtkinter.CTkButton(master=self.bottom,
                                        text="Send",
                                        text_color="#212121",
                                        fg_color="#FFD159",
                                        hover_color="#ffec99",
                                        corner_radius=100,
                                        width=80,
                                        height=35,
                                        command=self.chat_callback
                                        )
  def place_frames(self):
    self.header.pack(fill="x")
    self.separator1.pack(fill="x")
    self.main.pack(expand=True,fill="both")
    self.separator2.pack(fill="x")
    self.bottom.pack(fill="x")


  
  def place_widgets(self):
    self.header_label.pack(side="left",padx=15,pady=5)
    self.audio_button.pack(side="left",padx=15,pady=8),
    self.chat_input.pack(side="left",expand=True,fill="x")
    self.submit_button.pack(side="left",padx=15)

  def audio_callback(self,event):
    print("audio clicked")
    text =  SpeechRecognition()
    print(text)
    result = compilation(text)
    result["message"] = text;
    if(result['situation'] == False):
      result['item_height'] = 120;
    else:
      result['item_height'] = 400;

    self.main.update(result)
    print("result = ",result)
    self.chat_input.delete(0,END)

  
  def chat_callback(self):
    message    =  self.chat_input.get()
    result = compilation(message.lower())
    result["message"] = message;
    if(result['situation'] == False):
      result['item_height'] = 120;
    else:
      result['item_height'] = 300;

    self.main.update(result)
    print("result = ",result)
    self.chat_input.delete(0,END)


class ListFrame(customtkinter.CTkFrame):
  def __init__(self,master,text_data):
    super().__init__(master=master)
    self.init(text_data)
    

  def init(self,text_data):
    self.item_height = 0
    self.list_height = 0

    # data 
    self.list_data = text_data
    self.list_number = len(text_data)
    # self.list_height = self.list_number * item_height
    for index, item in enumerate(self.list_data):
      self.list_height += item['item_height']


    # canvas 
    self.canvas = Canvas(master=self,background="#f4f5f9",scrollregion=(0,0,self.winfo_width(),self.list_height),bd=0, highlightthickness=0, relief='ridge')
    self.canvas.pack(expand=True,fill='both')


    # main frame that canvas will draws 
    self.frame = customtkinter.CTkFrame(master=self,fg_color="#f4f5f9",corner_radius=0)
    for index,item in enumerate(self.list_data):
      self.create_item(index,item).pack(expand=True,fill='both')

    self.canvas.create_window(
      (0,0),
      window=self.frame,
      anchor="nw",
      width=self.winfo_width(),
      height=self.list_height
    )

    self.bind("<Configure>",self.update_size)

  def update_size(self,event):
    if self.list_height >= self.winfo_height():
      self.canvas.bind_all('<Button-4>', lambda event: self.canvas.yview_scroll(-int(30),"units"))
      self.canvas.bind_all('<Button-5>', lambda event: self.canvas.yview_scroll(+int(30),"units"))
    else : 
      self.canvas.unbind_all("<Button-4>")
      self.canvas.unbind_all("<Button-5>")

    self.canvas.create_window((0,0),
                              window=self.frame
                              ,anchor="nw",
                              width=self.winfo_width()
                              ,height=self.list_height)


  def update(self,message):
    self.canvas.destroy()
    new_entry = copy.copy(message)
    self.list_data.append(new_entry) 
    
    # item_height = 120 
    # self.init(self.list_data,item_height)
    self.init(self.list_data)
    if self.list_height >= self.winfo_height():
      self.canvas.bind_all('<Button-4>', lambda event: self.canvas.yview_scroll(-int(30),"units"))
      self.canvas.bind_all('<Button-5>', lambda event: self.canvas.yview_scroll(+int(30),"units"))
    self.canvas.yview_moveto( 1 )
    
  def create_item(self,index,item):
    print("item crated")
    is_correct = item['situation']
    print("is_correct = ",is_correct)



    frame = customtkinter.CTkFrame(master=self.frame,fg_color="#f4f5f9",corner_radius=0)

    frame.rowconfigure(0,weight=1)
    frame.columnconfigure((0,1),weight=1,uniform="a")

    message_label = customtkinter.CTkLabel(master=frame,
                                          text=item["message"],
                                          fg_color="#DDE3EF",
                                          text_color="#212121",
                                          font=("Arial",12),
                                          corner_radius=12
                                          
                                          )
    message_label.grid(row=index,column=1,columnspan=2,sticky="e",ipadx=8,ipady=4,padx=5,pady=5)   

    if 'origin' in item:
      language = item['origin']['langage']
      self.showAnswerGUI(frame,is_correct,index,item,language)
    


    return frame;

  def showAnswerGUI(self,frame,is_correct,index,item,language):
    print(f"--- {language} ---")
    print("codition = ",language == "Français")
    if(language == 'English'):
      label1 = "the proverb is correct" if is_correct else "did you mean this : " + item['origin']['correct_proverb'] 
      american_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
      customtkinter.CTkLabel(master=american_persona,
                                          text="Simon" ,
                                          fg_color="#ffffff",
                                          text_color="red",
                                          font=("Arial",10),
                                          corner_radius=12,
                                          height=8,                                    
                                          ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
      customtkinter.CTkLabel(master=american_persona,
                                          text=label1 ,
                                          fg_color="#ffffff",
                                          text_color="#212121",
                                          font=("Arial",12),
                                          corner_radius=12,
                                          height=16                  
                                          ).grid(row=1,column=0,sticky="w",ipadx=4)
      american_persona .grid(row=index+1,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

      if(is_correct):
        equi_frensh = item['equivalents']['Français']
        equi_darija = item['equivalents']['Darija']
        equi_espaniol = item['equivalents']['Espaniol']
        equi_italiano = item['equivalents']['Italiano']
        
        frensh_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=frensh_persona,
                                            text="Raphaël 🇫🇷" ,
                                            fg_color="#ffffff",
                                            text_color="blue",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=frensh_persona,
                                            text=equi_frensh ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        frensh_persona .grid(row=index+2,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

        darija_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=darija_persona,
                                            text="Mohammed " ,
                                            fg_color="#ffffff",
                                            text_color="orange",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=darija_persona,
                                            text=equi_darija ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        darija_persona .grid(row=index+3,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

        espaniol_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=espaniol_persona,
                                            text="Andriana 🇪🇸" ,
                                            fg_color="#ffffff",
                                            text_color="green",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=espaniol_persona,
                                            text=equi_espaniol ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        espaniol_persona .grid(row=index+4,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)
        italiano_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=italiano_persona,
                                            text="Alessandro" ,
                                            fg_color="#ffffff",
                                            text_color="pink",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=italiano_persona,
                                            text=equi_italiano ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        italiano_persona .grid(row=index+5,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

    elif(language == 'Darija'):
      label1 = "lmatal s7i7" if is_correct else "wach bghiti t9ol : " + item['origin']['correct_proverb'] 
      darija_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
      customtkinter.CTkLabel(master=darija_persona,
                                          text="Mohammed " ,
                                          fg_color="#ffffff",
                                          text_color="orange",
                                          font=("Arial",10),
                                          corner_radius=12,
                                          height=8,                                    
                                          ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
      customtkinter.CTkLabel(master=darija_persona,
                                          text=label1 ,
                                          fg_color="#ffffff",
                                          text_color="#212121",
                                          font=("Arial",12),
                                          corner_radius=12,
                                          height=16                  
                                          ).grid(row=1,column=0,sticky="w",ipadx=4)
      darija_persona.grid(row=index+1,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

      if(is_correct):
        equi_frensh = item['equivalents']['Français']
        equi_english = item['equivalents']['English']
        equi_espaniol = item['equivalents']['Espaniol']
        equi_italiano = item['equivalents']['Italiano']
        
        frensh_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=frensh_persona,
                                            text="Raphaël 🇫🇷" ,
                                            fg_color="#ffffff",
                                            text_color="blue",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=frensh_persona,
                                            text=equi_frensh ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        frensh_persona .grid(row=index+2,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

        english_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=english_persona,
                                            text="Simon " ,
                                            fg_color="#ffffff",
                                            text_color="red",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=english_persona,
                                            text=equi_english ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        english_persona.grid(row=index+3,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

        espaniol_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=espaniol_persona,
                                            text="Andriana 🇪🇸" ,
                                            fg_color="#ffffff",
                                            text_color="green",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=espaniol_persona,
                                            text=equi_espaniol ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        espaniol_persona .grid(row=index+4,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)
        italiano_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=italiano_persona,
                                            text="Alessandro" ,
                                            fg_color="#ffffff",
                                            text_color="pink",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=italiano_persona,
                                            text=equi_italiano ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        italiano_persona .grid(row=index+5,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)
    elif(language == 'Espaniol'):
      label1 = "El proverbio es cierto." if is_correct else "Quiso decir esto : " + item['origin']['correct_proverb'] 
      espaniol_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
      customtkinter.CTkLabel(master=espaniol_persona,
                                          text="Andriana 🇪🇸" ,
                                          fg_color="#ffffff",
                                          text_color="green",
                                          font=("Arial",10),
                                          corner_radius=12,
                                          height=8,                                    
                                          ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
      customtkinter.CTkLabel(master=espaniol_persona,
                                          text=label1 ,
                                          fg_color="#ffffff",
                                          text_color="#212121",
                                          font=("Arial",12),
                                          corner_radius=12,
                                          height=16                  
                                          ).grid(row=1,column=0,sticky="w",ipadx=4)
      espaniol_persona .grid(row=index+1,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

      if(is_correct):
        equi_frensh = item['equivalents']['Français']
        equi_darija = item['equivalents']['Darija']
        equi_english = item['equivalents']['English']
        equi_italiano = item['equivalents']['Italiano']
        
        frensh_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=frensh_persona,
                                            text="Raphaël 🇫🇷" ,
                                            fg_color="#ffffff",
                                            text_color="blue",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=frensh_persona,
                                            text=equi_frensh ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        frensh_persona .grid(row=index+2,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

        darija_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=darija_persona,
                                            text="Mohammed " ,
                                            fg_color="#ffffff",
                                            text_color="orange",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=darija_persona,
                                            text=equi_darija ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        darija_persona .grid(row=index+3,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

        english_persona  = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=english_persona ,
                                            text="Simon" ,
                                            fg_color="#ffffff",
                                            text_color="red",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=english_persona ,
                                            text=equi_english ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        english_persona.grid(row=index+4,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)
        italiano_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=italiano_persona,
                                            text="Alessandro" ,
                                            fg_color="#ffffff",
                                            text_color="pink",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=italiano_persona,
                                            text=equi_italiano ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        italiano_persona .grid(row=index+5,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

    elif(language == "Français"):
      print("francais elif block")
      label1 = "Le proverb est correct." if is_correct else "vouliez-vous dire : " + item['origin']['correct_proverb'] 
      frensh_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
      customtkinter.CTkLabel(master=frensh_persona,
                                            text="Raphaël 🇫🇷" ,
                                            fg_color="#ffffff",
                                            text_color="blue",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
      customtkinter.CTkLabel(master=frensh_persona,
                                            text=label1 ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
      frensh_persona .grid(row=index+1,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)


      

      if(is_correct):
        equi_espaniol = item['equivalents']['Espaniol']
        equi_darija = item['equivalents']['Darija']
        equi_english = item['equivalents']['English']
        equi_italiano = item['equivalents']['Italiano']
        
        espaniol_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=espaniol_persona,
                                            text="Andriana 🇪🇸" ,
                                            fg_color="#ffffff",
                                            text_color="green",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=espaniol_persona,
                                            text=equi_espaniol ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        espaniol_persona .grid(row=index+2,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

        darija_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=darija_persona,
                                            text="Mohammed " ,
                                            fg_color="#ffffff",
                                            text_color="orange",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=darija_persona,
                                            text=equi_darija ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        darija_persona .grid(row=index+3,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

        english_persona  = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=english_persona ,
                                            text="Andriana 🇪🇸" ,
                                            fg_color="#ffffff",
                                            text_color="green",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=english_persona ,
                                            text=equi_english ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        english_persona.grid(row=index+4,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)
        italiano_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
        customtkinter.CTkLabel(master=italiano_persona,
                                            text="Alessandro" ,
                                            fg_color="#ffffff",
                                            text_color="pink",
                                            font=("Arial",10),
                                            corner_radius=12,
                                            height=8,                                    
                                            ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
        customtkinter.CTkLabel(master=italiano_persona,
                                            text=equi_italiano ,
                                            fg_color="#ffffff",
                                            text_color="#212121",
                                            font=("Arial",12),
                                            corner_radius=12,
                                            height=16                  
                                            ).grid(row=1,column=0,sticky="w",ipadx=4)
        italiano_persona .grid(row=index+5,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)
    elif(language == "Italiano"):
          label1 = "Il proverbio è corretto." if is_correct else "intendevi :" + item['origin']['correct_proverb'] 
          italiano_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
          customtkinter.CTkLabel(master=italiano_persona,
                                              text="Alessandro" ,
                                              fg_color="#ffffff",
                                              text_color="pink",
                                              font=("Arial",10),
                                              corner_radius=12,
                                              height=8,                                    
                                              ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
          customtkinter.CTkLabel(master=italiano_persona,
                                              text=label1 ,
                                              fg_color="#ffffff",
                                              text_color="#212121",
                                              font=("Arial",12),
                                              corner_radius=12,
                                              height=16                  
                                              ).grid(row=1,column=0,sticky="w",ipadx=4)
          italiano_persona .grid(row=index+1,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)


          

          if(is_correct):
            equi_espaniol = item['equivalents']['Espaniol']
            equi_darija = item['equivalents']['Darija']
            equi_english = item['equivalents']['English']
            equi_frensh = item['equivalents']['Français']

            frensh_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
            customtkinter.CTkLabel(master=frensh_persona,
                                                  text="Raphaël 🇫🇷" ,
                                                  fg_color="#ffffff",
                                                  text_color="blue",
                                                  font=("Arial",10),
                                                  corner_radius=12,
                                                  height=8,                                    
                                                  ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
            customtkinter.CTkLabel(master=frensh_persona,
                                                  text=equi_frensh ,
                                                  fg_color="#ffffff",
                                                  text_color="#212121",
                                                  font=("Arial",12),
                                                  corner_radius=12,
                                                  height=16                  
                                                  ).grid(row=1,column=0,sticky="w",ipadx=4)
            frensh_persona .grid(row=index+2,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)
              
            espaniol_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
            customtkinter.CTkLabel(master=espaniol_persona,
                                                text="Andriana 🇪🇸" ,
                                                fg_color="#ffffff",
                                                text_color="green",
                                                font=("Arial",10),
                                                corner_radius=12,
                                                height=8,                                    
                                                ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
            customtkinter.CTkLabel(master=espaniol_persona,
                                                text=equi_espaniol ,
                                                fg_color="#ffffff",
                                                text_color="#212121",
                                                font=("Arial",12),
                                                corner_radius=12,
                                                height=16                  
                                                ).grid(row=1,column=0,sticky="w",ipadx=4)
            espaniol_persona .grid(row=index+3,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

            darija_persona = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
            customtkinter.CTkLabel(master=darija_persona,
                                                text="Mohammed " ,
                                                fg_color="#ffffff",
                                                text_color="orange",
                                                font=("Arial",10),
                                                corner_radius=12,
                                                height=8,                                    
                                                ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
            customtkinter.CTkLabel(master=darija_persona,
                                                text=equi_darija ,
                                                fg_color="#ffffff",
                                                text_color="#212121",
                                                font=("Arial",12),
                                                corner_radius=12,
                                                height=16                  
                                                ).grid(row=1,column=0,sticky="w",ipadx=4)
            darija_persona .grid(row=index+4,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)

            english_persona  = customtkinter.CTkFrame(master=frame,fg_color="#ffffff",corner_radius=12)
            customtkinter.CTkLabel(master=english_persona ,
                                                text="Andriana 🇪🇸" ,
                                                fg_color="#ffffff",
                                                text_color="green",
                                                font=("Arial",10),
                                                corner_radius=12,
                                                height=8,                                    
                                                ).grid(row=0,column=0,sticky="nw",ipadx=8,ipady=4)
            customtkinter.CTkLabel(master=english_persona ,
                                                text=equi_english ,
                                                fg_color="#ffffff",
                                                text_color="#212121",
                                                font=("Arial",12),
                                                corner_radius=12,
                                                height=16                  
                                                ).grid(row=1,column=0,sticky="w",ipadx=4)
            english_persona.grid(row=index+5,column=0,columnspan=2,sticky="w",ipadx=4,ipady=4,padx=10,pady=5)
            


class Divider(customtkinter.CTkFrame):
  def __init__(self,master):
    super().__init__(master=master,fg_color="#e9ecef",corner_radius=0,height=2)


if __name__ == '__main__':
  App("wisdom",(800,500))