from tkinter import *
from tkinter import filedialog
import tkinter.filedialog
import tkinter.messagebox
import customtkinter
from drawing_finder import drawing_finder
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.drawing_directory = StringVar()
        self.drawing_directory.set("E:/repos/work-app/dwg")

        # configure window
        self.title("DETEX APP")
        self.geometry(f"{1100}x{580}")

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
        self.drawing_button.grid(row=1, column=0, padx=20, pady=10)

        #Settings sidebar
        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, command=self.load_settings, text="Settings")
        self.settings_button.grid(row=7, column=0, padx=20, pady=20)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, rowspan = 3, columnspan = 3,padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        self.textbox.insert("0.0",
        """
        Version 0.0.1
        -Drawing Finder
            -Custom directory to search

        -Settings
            -Light/Dark mode
            -Scaling
        
        """)

        self.textbox.configure(state="disabled")


        #Drawing Finder frame
        self.drawing_finder_frame = customtkinter.CTkFrame(self, width=250)
        self.drawing_finder_frame.grid(row=0, column=1, rowspan = 3, columnspan = 3,padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.drawing_finder_frame.grid_columnconfigure((0,1,2), weight=0)
        self.drawing_finder_frame.grid_rowconfigure((0,1,2), weight=0)


        folder_icon = customtkinter.CTkImage(dark_image=Image.open("./assets/icons/folder_white.png"))
        self.set_dir_button = customtkinter.CTkButton(self.drawing_finder_frame, text="", command= self.set_dir, width=1, image=folder_icon)
        self.set_dir_button.grid(row=0, column=1, padx=(20,0), pady=20)

        self.drawing_dir_label = customtkinter.CTkEntry(self.drawing_finder_frame, font=("Arial", 12), width=300, textvariable=self.drawing_directory, state=DISABLED)
        self.drawing_dir_label.grid(row=0, column=2, padx=(5,10), pady=20)

        
        search_icon = customtkinter.CTkImage(dark_image=Image.open("./assets/icons/search_white.png"))
        self.search_button = customtkinter.CTkButton(self.drawing_finder_frame, text="",command= self.open_input_dialog_event, anchor="w", image= search_icon, width=1)
        self.search_button.grid(row=0, column=3, padx=0, pady=20)

        self.drawing_finder_frame.grid_forget()


        #SETTINGS FRAME
        self.settings_frame = customtkinter.CTkFrame(self, width=250)
        self.settings_frame.grid(row=0, column=1, rowspan = 3, columnspan = 3,padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.settings_frame.grid_rowconfigure((0,1,2), weight = 0)
        self.settings_frame.grid_columnconfigure((0,1,2), weight = 0)


        #Appearance section of settings
        self.appearance_label = customtkinter.CTkLabel(self.settings_frame, text="Appearance", anchor="center", font=("Arial", 20))
        self.appearance_label.grid(row=0, column=0, padx=20, pady=20)

        self.appearance_optionemenu = customtkinter.CTkOptionMenu(self.settings_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_optionemenu.grid(row=0, column=1, padx=20, pady=20)


        #Scaling 
        self.scaling_label = customtkinter.CTkLabel(self.settings_frame, text="UI Scaling", anchor="center", font=("Arial", 20))
        self.scaling_label.grid(row=1, column=0, padx=20, pady=20)
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.settings_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=1, column=1, padx=20, pady=20)

        self.settings_frame.grid_forget()


    def reset_buttons(self):
        self.drawing_button.configure(border_width=0 ,border_color="yellow")
        self.settings_button.configure(border_width=0 ,border_color="yellow")

    def reset_frames(self):
        self.drawing_finder_frame.grid_forget()
        self.settings_frame.grid_forget()

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
            print("oops")
        else:
            print(result)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a drawing number:", title="Drawing Search")

        self.find_drawing(self.drawing_directory, dialog.get_input())

    def load_drawing(self):
        self.reset_frames()
        self.reset_buttons()
        self.drawing_button.configure(border_width=3 ,border_color="yellow")
        self.drawing_finder_frame.grid(row=0, column=1, rowspan = 3, columnspan = 3,padx=(20, 20), pady=(20, 20), sticky="nsew")

    def load_settings(self):
        self.reset_frames()
        self.reset_buttons()
        self.settings_button.configure(border_width=3 ,border_color="yellow")
        self.settings_frame.grid(row=0, column=1, rowspan = 3, columnspan = 3,padx=(20, 20), pady=(20, 20), sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()