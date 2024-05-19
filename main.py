import AppTabs
import customtkinter as CTk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("670x760")
        self.title("Название")
        self.resizable(False, False)

        self.tab_view = AppTabs.AppTabs(master=self, width=600, height=760)
        self.tab_view.grid(row=0, column=0, padx=0, pady=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
