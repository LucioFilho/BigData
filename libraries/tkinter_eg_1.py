import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App with Draggable Popup")
        self.root.geometry("400x300")
        
        self.popup_frame = None
        
        open_popup_button = tk.Button(self.root, text="Open Popup", command=self.open_popup)
        open_popup_button.pack(pady=20)

    def open_popup(self):
        if self.popup_frame:
            self.popup_frame.destroy()  # Remove existing popup if open
        
        # Popup container
        self.popup_frame = tk.Frame(self.root, bg="lightgray", bd=2)
        self.popup_frame.place(relx=0.5, rely=0.5, anchor="center", width=200, height=100)
        
        # Store initial popup position
        self.popup_initial_x = self.popup_frame.winfo_x()
        self.popup_initial_y = self.popup_frame.winfo_y()
        
        # Popup header
        self.header_frame = tk.Frame(self.popup_frame, bg="darkgray", bd=1)
        self.header_frame.place(relwidth=1, height=20)
        self.header_frame.bind("<Button-1>", self.start_move)  # Bind mouse click to start_move
        self.header_frame.bind("<ButtonRelease-1>", self.stop_move)  # Bind release to stop_move
        self.header_frame.bind("<B1-Motion>", self.on_move)  # Bind movement to on_move
        
        # Close button in header
        close_button = tk.Button(self.header_frame, text="X", command=self.close_popup, bg="darkgray", fg="white", bd=0)
        close_button.place(relx=0.95, rely=0.5, anchor="center")
        
        # Popup content
        popup_label = tk.Label(self.popup_frame, text="This is an inline popup", bg="lightgray")
        popup_label.place(rely=0.5, relx=0.5, anchor="center")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def on_move(self, event):
        deltax = event.x_root - self.x
        deltay = event.y_root - self.y
        new_x = self.root.winfo_pointerx() - self.popup_initial_x - self.x
        new_y = self.root.winfo_pointery() - self.popup_initial_y - self.y
        self.popup_frame.place(x=new_x, y=new_y)

    def close_popup(self):
        if self.popup_frame:
            self.popup_frame.destroy()
            self.popup_frame = None

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
