
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import os
import yt_dlp
import threading


def select_path():
    folder_path = filedialog.askdirectory()
    if folder_path:
        pathEntry.configure(state="normal")
        pathEntry.delete(0,ctk.END)
        pathEntry.insert(0, folder_path)
        pathEntry.configure(state="readonly")

def download_mp3_thread():
    youtube_url = urlEntry.get()
    selected_path = pathEntry.get()

    if not youtube_url:
        messagebox.showerror("Error", "Please enter a valid youtube url")
        return
    if not selected_path:
        messagebox.showerror("Error", "Please select a path")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(selected_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    messagebox.showinfo("Success","Mp3 downloaded successfully!")

def download_mp3():
    threading.Thread(target=download_mp3_thread).start()

def download_mp4_thread():
    youtube_url = urlEntry.get()
    selected_path = pathEntry.get()

    if not youtube_url:
        messagebox.showerror("Error","Please enter a valid youtube url")
        return
    if not selected_path:
        messagebox.showerror("Error", "Please select a path")
        return

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(selected_path, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    messagebox.showinfo("Success", "Video downloaded successfully!")


def download_mp4():
    threading.Thread(target=download_mp4_thread).start()

def clear_url_entry():
    urlEntry.delete(0, ctk.END)

app = ctk.CTk()
app.title("Youtube to mp3/mp4 converter")
app.geometry("430x340")

youtubeLabel = ctk.CTkLabel(app, text="youtube url:", font=("Arial", 16, "bold"))
youtubeLabel.place(x=30,y=40)

urlEntry = ctk.CTkEntry(app, width=230, justify="center")
urlEntry.place(x=130, y=40)

pathLabel = ctk.CTkLabel(app, text="select path:", font=("Arial", 16, "bold"))
pathLabel.place(x=30, y=90)

pathEntry = ctk.CTkEntry(app, width=180, justify="center", state="readonly")
pathEntry.place(x=130, y=90)

folderImage = Image.open("folder.png")
folderImg = ctk.CTkImage(folderImage)

pathButton = ctk.CTkButton(app,text="",width=38, image=folderImg, fg_color="dark blue", hover_color="dark gray", command=select_path)
pathButton.place(x=320, y=90)

mp3Image = Image.open("music-file.png")
mp3Img = ctk.CTkImage(mp3Image)

downloadButton = ctk.CTkButton(app, image=mp3Img, text="Download Mp3",command=download_mp3, font=("arial",14,"bold"), width=200, height=50, fg_color="dark blue", hover_color="gray")
downloadButton.place(x=100,y=160)

mp4Image = Image.open("youtube (1).png")
mp4Img = ctk.CTkImage(mp4Image)

downloadMp4Button = ctk.CTkButton(app, image=mp4Img, text="Download Mp4", command=download_mp4, font=("arial",14,"bold"), width=200, height=50, fg_color="dark blue", hover_color="gray")
downloadMp4Button.place(x=100, y=230)

loadingImage = Image.open("Ellipsis@1x-1.0s-200px-200px.gif")
loadingImg = ctk.CTkImage(loadingImage)

loadingLabel = ctk.CTkLabel(app, image=loadingImg, text="")
loadingLabel.place(x=185, y=280)

clearImage = Image.open("circle-xmark.png")
clearImg = ctk.CTkImage(clearImage)

clearBtn = ctk.CTkButton(app,image=clearImg, text="", width=35, fg_color="dark blue", hover_color="gray", command=clear_url_entry)
clearBtn.place(x=370, y=40)
app.mainloop()