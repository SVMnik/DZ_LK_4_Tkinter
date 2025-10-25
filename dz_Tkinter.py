import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
import os

class MainWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.geometry("960x660+100+100")
        self.title("User hello GUI")
        self.setUpMainWindow()
        
    def setUpMainWindow(self):
        hello_label = tk.Label(self, text="Добро пожаловать в тестовое окно!", bg='SystemButtonFace')
        hello_label.place(x=400, y=10)
        
        image_path = "images/hello.jpg"
        try:
            if os.path.exists(image_path):
                self.world_image = ImageTk.PhotoImage(Image.open(image_path))
                world_label = tk.Label(self, image=self.world_image)
                world_label.place(x=-2, y=40)
        except Exception as error:
            print(f"Image not found.\nError: {error}")
            
        gif_path = "images/russia-saul-goodman.gif"
        try:
            if os.path.exists(gif_path):
                self.gif_frames = []
                gif = Image.open(gif_path)
                for frame in ImageSequence.Iterator(gif):
                    frame = frame.resize((100, 100), Image.Resampling.LANCZOS)
                    self.gif_frames.append(ImageTk.PhotoImage(frame))
                
                self.gif_label = tk.Label(self, bg='#C8BFE7')
                self.gif_label.place(x=0, y=570)
                
                self.current_frame = 0
                self.animate_gif()
                
        except Exception as error:
            print(f"Ошибка загрузки GIF: {error}")
            
    def animate_gif(self):
        if hasattr(self, 'gif_frames'):
            self.gif_label.configure(image=self.gif_frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
            self.after(100, self.animate_gif)

class MainWindowProfile(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.images = {} 
        self.initializeUI()
        
    def initializeUI(self):
        self.geometry("250x400+50+50")
        self.title("User Profile GUI")
        self.setUpMainWindow()
        
    def createImageLabels(self):
        images = ["images/light_purple.png", "images/profile_image.png"]
        for image in images:
            try:
                if os.path.exists(image):
                    self.images[image] = ImageTk.PhotoImage(Image.open(image))
                    label = tk.Label(self, image=self.images[image])
                    
                    if image == "images/light_purple.png":
                        label.place(x=0, y=0)
                    elif image == "images/profile_image.png":
                        label.place(x=0, y=45)
                        
            except Exception as error:
                print(f"Image not found.\nError: {error}")
                
    def setUpMainWindow(self):
        self.createImageLabels()
        
        user_label = tk.Label(self, text="Щуров Никита", font=("Arial", 20), bg='#C8BFE7')
        user_label.place(x=35, y=3)
        
        bio_label = tk.Label(self, text="Биография", font=("Arial", 17), bg='#C8BFE7')
        bio_label.place(x=15, y=215)
        
        about_text = "Я инженер-программист с 0-летним опытом создания потрясающего кода."
        about_label = tk.Label(self, text=about_text, wraplength=220, justify="left", bg='#C8BFE7')
        about_label.place(x=15, y=240)
        about_label.configure(width=30, height=3)
        
        skills_label = tk.Label(self, text="Умения", font=("Arial", 17), bg='#C8BFE7')
        skills_label.place(x=15, y=280)
        
        languages_label = tk.Label(self, text="Python | Gaming | SQL | C++", bg='#C8BFE7')
        languages_label.place(x=15, y=305)
        
        experience_label = tk.Label(self, text="Опыт", font=("Arial", 17), bg='#C8BFE7')
        experience_label.place(x=15, y=325)
        
        developer_label = tk.Label(self, text="Python Разработчик", bg='#C8BFE7')
        developer_label.place(x=15, y=360)
        
        driver_dates_label = tk.Label(self, text="oct 25 2025 - oct 26 2025", font=("Arial", 10), bg='#C8BFE7')
        driver_dates_label.place(x=15, y=380)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно
    
    window1 = MainWindow()
    window2 = MainWindowProfile()
    
    root.mainloop()