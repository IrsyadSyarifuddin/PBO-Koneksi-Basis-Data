import tkinter as tk
from koneksi import connect_database, close_database


class Ui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Koneksi Database")

        # Label dan entry untuk username
        self.label_username = tk.Label(text="Username:")
        self.entry_username = tk.Entry()

        # Label dan entry untuk password
        self.label_password = tk.Label(text="Password:")
        self.entry_password = tk.Entry(show='*')

        # Tombol untuk koneksi dan tutup
        self.button_connect = tk.Button(text="Koneksi", command=self.connect_database)
        self.button_close = tk.Button(text="Tutup", command=self.close_database)

        self.label_status = tk.Label(text="Database Terputus")

        # Menata layout
        self.label_username.grid(row=0, column=0)
        self.entry_username.grid(row=0, column=1)
        self.label_password.grid(row=1, column=0)
        self.entry_password.grid(row=1, column=1)
        self.button_connect.grid(row=2, column=0)
        self.button_close.grid(row=2, column=1)
        self.label_status.grid(row=3, column=0, columnspan=2)

        # Sesion
        self.connection = None
        self.connection_status = False

        self.window.mainloop()

    def connect_database(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        connection = connect_database(username, password)

        if connection is not None:
            print("Koneksi berhasil!")
            self.connection_status = True
            self.update_connection_status()
            
        else:
            print("Koneksi gagal!")
            self.connection_status = False
            self.update_connection_status()

    def close_database(self):
        close_database(self.connection)
        self.connection_status = False
        self.update_connection_status()
    
    def update_connection_status(self):
        if self.connection_status:
            self.label_status.config(text="Database Terhubung")
        else:
            self.label_status.config(text="Database Terputus")