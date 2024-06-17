from tkinter import *
from tkinter import filedialog
import tkinter.filedialog
import tkinter.messagebox
import customtkinter
from CTkMessagebox import CTkMessagebox
from drawing_finder import drawing_finder
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class PDFViewer:
    def __init__(self, master):
        pass

    

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.drawing_directory = StringVar()
        self.drawing_directory.set("E:/repos/work-app/dwg")

        # configure window
        self.title("DETEX APP")
        self.geometry(f"{1358}x{764}")
        self.resizable(width=False, height=False)
        self.attributes('-topmost', True)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        #Logo
        detex_logo = customtkinter.CTkImage(dark_image=Image.open("./assets/images/detex_white.png"), size= (150,46))
        #self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="DETEX", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo = customtkinter.CTkLabel(self.sidebar_frame, image=detex_logo, text="")
        self.logo.grid(row=0, column=0, padx=0, pady=(20, 10))

        #Sidebar load drawing button
        self.drawing_button = customtkinter.CTkButton(self.sidebar_frame, command=self.load_drawing, text="Drawing Finder")
        self.drawing_button.grid(row=1, column=0, padx=20, pady=50)

        #Sidebar load drawing button
        self.formatter_button = customtkinter.CTkButton(self.sidebar_frame, command=self.load_formatter, text="Text Formatter")
        self.formatter_button.grid(row=2, column=0, padx=20, pady=0)

        #Settings sidebar
        settings_icon = customtkinter.CTkImage(dark_image=Image.open("./assets/icons/settings_white.png"))
        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, command=self.load_settings, text="", image=settings_icon, fg_color="transparent", width=1)
        self.settings_button.grid(row=7, column=0, padx=20, pady=20, sticky="w")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250, bg_color="transparent")
        self.textbox.grid(row=0, column=1, rowspan = 3, columnspan = 3, sticky="nsew")
        
        self.textbox.insert("0.0",
        """
        Version 0.0.1
        -Drawing Finder
            -Custom directory to search

        -Settings
            -Scaling
        
        """)

        self.textbox.configure(state="disabled")


        #Drawing Finder frame
        self.drawing_finder_frame = customtkinter.CTkFrame(self, fg_color="gray12")
        self.drawing_finder_frame.grid(row=0, column=1, rowspan = 3, columnspan = 3,sticky="nsew")
        self.drawing_finder_frame.grid_columnconfigure((0,1,2,3,4), weight=0)
        self.drawing_finder_frame.grid_rowconfigure((0,1,2,3,4,5), weight=0)


        folder_icon = customtkinter.CTkImage(dark_image=Image.open("./assets/icons/folder_white.png"))
        self.set_dir_button = customtkinter.CTkButton(self.drawing_finder_frame, text="", command= self.set_dir, width=1, image=folder_icon)
        self.set_dir_button.grid(row=0, column=1, padx=(20,0), pady=50, sticky="n")

        self.drawing_dir_label = customtkinter.CTkEntry(self.drawing_finder_frame, font=("Arial", 12), width=300, textvariable=self.drawing_directory, state=DISABLED)
        self.drawing_dir_label.grid(row=0, column=2, padx=(0,0), pady=50, sticky="n")

        
        search_icon = customtkinter.CTkImage(dark_image=Image.open("./assets/icons/search_white.png"))
        self.search_button = customtkinter.CTkButton(self.drawing_finder_frame, text="",command= self.open_input_dialog_event, anchor="w", image= search_icon, width=1)
        self.search_button.grid(row=0, column=3, padx=0, pady=50, sticky="n")

        self.drawing_finder_frame.grid_forget()

        #-------------------TEXT FORMATTER---------------------#
        self.text_formatter_frame = customtkinter.CTkFrame(self, fg_color="gray12")
        self.text_formatter_frame.grid(row=0, column=1, rowspan = 3, columnspan = 3,sticky="nsew")
        self.text_formatter_frame.grid_columnconfigure((0,1,2,3,4), weight=0)
        self.text_formatter_frame.grid_rowconfigure((0,1,2,3,4,5), weight=0)

        self.formatter_label = customtkinter.CTkLabel(self.text_formatter_frame, font = ("Arial", 24),text="Enter notes below\nPreferably in the format shown")
        self.formatter_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.text_box = customtkinter.CTkTextbox(self.text_formatter_frame, width=500, height=500, border_width=2, border_color= "cyan")
        self.text_box.insert(index=INSERT ,text="Call# 123456\nWO 02123456\nHD 0001",tags=None)
        self.text_box.grid(row=1, column=0, columnspan=2, rowspan=3, padx=(20,0))

        self.submit_button = customtkinter.CTkButton(self.text_formatter_frame, text="submit", fg_color="green", text_color="gray12")
        self.submit_button.grid(row=4, column=1, sticky="e", pady=20)


        self.call_label = customtkinter.CTkLabel(self.text_formatter_frame, text="Call#")
        self.call_label.grid(row=1, column=2, padx=(20,0), sticky="n")
        self.call_entry = customtkinter.CTkEntry(self.text_formatter_frame)
        self.call_entry.grid(row=1, column=3, padx=(10,0), sticky="n")

        self.work_order_label = customtkinter.CTkLabel(self.text_formatter_frame, text="Work Order")
        self.work_order_label.grid(row=2, column=2, padx=(20,0), sticky="n")
        self.work_order_entry = customtkinter.CTkEntry(self.text_formatter_frame)
        self.work_order_entry.grid(row=2, column=3, padx=(10,0), sticky="n")

        self.text_formatter_frame.grid_forget()


        #SETTINGS FRAME
        self.settings_frame = customtkinter.CTkFrame(self, fg_color="gray12")
        self.settings_frame.grid(row=0, column=1, rowspan = 3, columnspan = 3,padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.settings_frame.grid_rowconfigure((0,1,2), weight = 0)
        self.settings_frame.grid_columnconfigure((0,1,2), weight = 0)

        #Scaling 
        self.scaling_label = customtkinter.CTkLabel(self.settings_frame, text="UI Scaling", anchor="center", font=("Arial", 20))
        self.scaling_label.grid(row=0, column=0, padx=20, pady=20)
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.settings_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=0, column=1, padx=20, pady=20)

        self.settings_frame.grid_forget()



    def reset_buttons(self):
        self.drawing_button.configure(border_width=0 ,border_color="")
        self.settings_button.configure(border_width=0 ,border_color="")
        self.formatter_button.configure(border_width=0 ,border_color="")

    def reset_frames(self):
        self.drawing_finder_frame.grid_forget()
        self.settings_frame.grid_forget()
        self.text_formatter_frame.grid_forget()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def set_dir(self):
        new_dir = tkinter.filedialog.askdirectory()

        if(new_dir != ""):
            self.drawing_directory.set(new_dir)
        

    def find_drawing(self, dir, pattern):
        result = drawing_finder(dir, pattern)

        if len(result) == 0:
            CTkMessagebox(title="Error", message="File " + pattern + " could not be found", icon="cancel")
        else:
            print(result)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a drawing number:", title="Drawing Search")

        self.find_drawing(self.drawing_directory.get(), dialog.get_input())

    def load_drawing(self):
        self.reset_frames()
        self.reset_buttons()
        self.drawing_button.configure(border_width=3 ,border_color="cyan")
        self.drawing_finder_frame.grid(row=0, column=1, rowspan = 5, columnspan = 5,sticky="nsew")

    def load_formatter(self):
        self.reset_frames()
        self.reset_buttons()
        self.formatter_button.configure(border_width=3 ,border_color="cyan")
        self.text_formatter_frame.grid(row=0, column=1, rowspan = 5, columnspan = 5,sticky="nsew")

    def load_settings(self):
        self.reset_frames()
        self.reset_buttons()
        self.settings_button.configure(border_width=3 ,border_color="cyan")
        self.settings_frame.grid(row=0, column=1, rowspan = 3, columnspan = 3, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()