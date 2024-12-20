from tkinter import *

s = Tk()
s.title("Deepak's Management")
s.geometry("500x500")
s.config(bg="#355DCB")
s.resizable(False,False)

try:
    photo = PhotoImage(file='Portfolio.png')
    s.iconphoto(True, photo)
except Exception as e:
    print(f"Error loading icon: {e}")

btn = Button(s, text="Deepak Bhai", font=("Time New Roman",30,"bold"), bg="#355DCB", cursor="plus")
btn.place(x=140,y=100,height=120,width=230)

s.mainloop()

# import os
# import requests
# from tkinter import *

# s = Tk()
# s.title("Deepak's Management")
# s.geometry("500x500")
# s.config(bg="#355DCB")
# s.resizable(False, False)

# # Download the image dynamically
# image_url = 'icon.png'
# local_image_path = 'icon.png'

# try:
#     response = requests.get(image_url)
#     with open(local_image_path, 'wb') as file:
#         file.write(response.content)
#     photo = PhotoImage(file=local_image_path)
#     s.iconphoto(True, photo)
# except Exception as e:
#     print(f"Error loading icon: {e}")

# btn = Button(s, text="Deepak Bhai", font=("Times New Roman", 30, "bold"), bg="#355DCB", cursor="plus")
# btn.place(x=140, y=100, height=120, width=230)

# s.mainloop()

# # Cleanup downloaded file (optional)
# os.remove(local_image_path)
