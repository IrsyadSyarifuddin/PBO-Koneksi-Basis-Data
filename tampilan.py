import tkinter as tk


class Ui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Koneksi Database")

        # Label dan entry untuk username
        self.label_username = tk.Label()
        self.entry_username = tk.Entry()

        # Label dan entry untuk password
        

        # Tombol untuk koneksi dan tutup
        self.button_connect = tk.Button(text=" ", command=self.connect_database)
        

        self.label_status = tk.Label(text="Database Terputus")


        # Sesion
        self.connection = None
        self.connection_status = False

        self.window.mainloop()

    def connect_database(self):
        username = 
        password = 

        connection = connect_database( )

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