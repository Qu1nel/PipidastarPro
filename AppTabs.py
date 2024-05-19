import customtkinter as CTk
import client
import socket


class AppTabs(CTk.CTkTabview):
    class StudentReview:
        def __init__(self, main_frame):
            self.student_labels_dict = dict()

            # Обзор. Добавление фреймов
            self.top_frame = CTk.CTkFrame(master=main_frame, width=640, height=115,
                                          fg_color="transparent")
            self.top_frame.grid(row=0, column=0, padx=(3, 3), pady=(3, 0), sticky="nsew")

            # Тело
            self.mid_frame = CTk.CTkFrame(master=main_frame, width=640, height=550,
                                          fg_color="transparent")
            self.mid_frame.grid(row=1, column=0, padx=(3, 3), pady=(3, 0), sticky="nsew")

            # Кнопки
            self.bottom_frame = CTk.CTkFrame(master=main_frame, width=640, height=70,
                                             fg_color="transparent")
            self.bottom_frame.grid(row=2, column=0, padx=(3, 3), pady=(3, 3), sticky="nsew")

            # Посиковая строка
            self.search_entry_frame = CTk.CTkFrame(master=self.top_frame, width=200, height=34, fg_color="transparent")
            self.search_entry_frame.grid(row=0, column=0, padx=(360, 3), pady=(10, 10), sticky="nsew")
            self.search_entry = CTk.CTkEntry(self.search_entry_frame, placeholder_text="Поиск", width=200,
                                             height=34, corner_radius=20)
            self.search_entry.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

            self.search_btn_frame = CTk.CTkFrame(master=self.top_frame, width=70, height=34, fg_color="transparent")
            self.search_btn_frame.grid(row=0, column=1, padx=(7, 7), pady=(10, 10), sticky="nsew")
            self.search_btn = CTk.CTkButton(self.search_btn_frame, width=70, height=24,
                                            text="Найти", command=self.search_btn_event, corner_radius=20)
            self.search_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")

            # Поля с инфой
            self.name_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.name_frame.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.name = CTk.CTkLabel(self.name_frame, text="ФИО:", font=CTk.CTkFont(size=15))
            self.name.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.name_data = CTk.CTkLabel(self.name_frame, text="Иванов Иван Иванович", font=CTk.CTkFont(size=15))
            self.name_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["name"] = self.name_data

            self.phone_number_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.phone_number_frame.grid(row=1, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.phone_number = CTk.CTkLabel(self.phone_number_frame, text="Телефон:", font=CTk.CTkFont(size=15))
            self.phone_number.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.phone_number_data = CTk.CTkLabel(self.phone_number_frame, text="+7(999)100-55-77",
                                                  font=CTk.CTkFont(size=15))
            self.phone_number_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["phone"] = self.phone_number_data

            self.social_media_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.social_media_frame.grid(row=2, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.social_media = CTk.CTkLabel(self.social_media_frame, text="Соцсети:", font=CTk.CTkFont(size=15))
            self.social_media.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.social_media_data = CTk.CTkLabel(self.social_media_frame, text="@Serega", font=CTk.CTkFont(size=15))
            self.social_media_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["social_media"] = self.social_media_data

            self.date_age_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.date_age_frame.grid(row=3, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.date_age = CTk.CTkLabel(self.date_age_frame, text="Дата рождения:", font=CTk.CTkFont(size=15))
            self.date_age.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.date_age_data = CTk.CTkLabel(self.date_age_frame, text="09.07.1800", font=CTk.CTkFont(size=15))
            self.date_age_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["date"] = self.date_age_data

            self.age_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.age_frame.grid(row=4, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.age = CTk.CTkLabel(self.age_frame, text="Возраст:", font=CTk.CTkFont(size=15))
            self.age.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.age_data = CTk.CTkLabel(self.age_frame, text="19", font=CTk.CTkFont(size=15))
            self.age_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["age"] = self.age_data

            self.status_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.status_frame.grid(row=5, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.status = CTk.CTkLabel(self.status_frame, text="Статус:", font=CTk.CTkFont(size=15))
            self.status.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.status_data = CTk.CTkLabel(self.status_frame, text="Ребенок в семье", font=CTk.CTkFont(size=15))
            self.status_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["status"] = self.status_data

            self.events_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.events_frame.grid(row=6, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.events = CTk.CTkLabel(self.events_frame, text="События:", font=CTk.CTkFont(size=15))
            self.events.grid(row=0, column=0, padx=(5, 0), pady=(5, 0))

            self.student_history_frame = CTk.CTkFrame(master=self.mid_frame, width=610, height=150,
                                                      fg_color="transparent")
            self.student_history_frame.grid(row=7, column=0, padx=(5, 0), pady=(5, 5), sticky="nsew")
            self.student_history = CTk.CTkTextbox(master=self.student_history_frame, width=610, corner_radius=10)
            self.student_history.grid(row=0, column=0, sticky="nsew")
            self.student_history.insert("0.0", "[00:00:00]: Архивная запись такая-то\n\n" * 20)
            self.student_labels_dict["student_history"] = self.student_history

        def search_btn_event(self):
            s = socket.socket()
            print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
            s.connect((client.SERVER_HOST, client.SERVER_PORT))
            print("[+] Connected.")
            request = f"200:{self.search_entry.get()}"
            s.send(request.encode())
            message = None
            while message is None:
                message = s.recv(1024).decode()
            print(data := message.lstrip('[').lstrip('(').rstrip(')').rstrip(']').split(','), 'end')
            for key, text in zip(self.student_labels_dict, data):
                try:
                    print(key, text, len(text))
                    self.student_labels_dict[key].configure(text=text.strip()[1:-1]) if len(text) > 3 else \
                        self.student_labels_dict[key].configure(text=text)

                except ValueError:
                    self.student_labels_dict[key].delete('1.0', CTk.END)
                    self.student_history.insert("0.0", f"{text[2:-2]}\n\n" * 20)

    class VolunteerReview:
        def __init__(self, main_frame):
            self.volunteer_labels_dict = dict()

            # Обзор. Добавление фреймов
            self.top_frame = CTk.CTkFrame(master=main_frame, width=640, height=115,
                                          fg_color="transparent")
            self.top_frame.grid(row=0, column=0, padx=(3, 3), pady=(3, 0), sticky="nsew")

            # Тело
            self.mid_frame = CTk.CTkFrame(master=main_frame, width=640, height=550,
                                          fg_color="transparent")
            self.mid_frame.grid(row=1, column=0, padx=(3, 3), pady=(3, 0), sticky="nsew")

            # Кнопки
            self.bottom_frame = CTk.CTkFrame(master=main_frame, width=640, height=70,
                                             fg_color="transparent")
            self.bottom_frame.grid(row=2, column=0, padx=(3, 3), pady=(3, 3), sticky="nsew")

            # Посиковая строка
            self.search_entry_frame = CTk.CTkFrame(master=self.top_frame, width=200, height=34, fg_color="transparent")
            self.search_entry_frame.grid(row=0, column=0, padx=(360, 3), pady=(10, 10), sticky="nsew")
            self.search_entry = CTk.CTkEntry(self.search_entry_frame, placeholder_text="Поиск", width=200,
                                             height=34, corner_radius=20)
            self.search_entry.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

            self.search_btn_frame = CTk.CTkFrame(master=self.top_frame, width=70, height=34, fg_color="transparent")
            self.search_btn_frame.grid(row=0, column=1, padx=(7, 7), pady=(10, 10), sticky="nsew")
            self.search_btn = CTk.CTkButton(self.search_btn_frame, width=70, height=24,
                                            text="Найти", command=self.search_btn_event, corner_radius=20)
            self.search_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")

            # Поля с инфой
            self.name_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.name_frame.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.name = CTk.CTkLabel(self.name_frame, text="ФИО:", font=CTk.CTkFont(size=15))
            self.name.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.name_data = CTk.CTkLabel(self.name_frame, text="Иванов Иван Иванович", font=CTk.CTkFont(size=15))
            self.name_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["name"] = self.name_data

            self.date_age_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.date_age_frame.grid(row=1, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.date_age = CTk.CTkLabel(self.date_age_frame, text="Дата рождения:", font=CTk.CTkFont(size=15))
            self.date_age.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.date_data = CTk.CTkLabel(self.date_age_frame, text="09.07.1800", font=CTk.CTkFont(size=15))
            self.date_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["date"] = self.date_data

            self.phone_number_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.phone_number_frame.grid(row=2, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.phone_number = CTk.CTkLabel(self.phone_number_frame, text="Телефон:", font=CTk.CTkFont(size=15))
            self.phone_number.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.phone_number_data = CTk.CTkLabel(self.phone_number_frame, text="+7(999)100-55-77",
                                                  font=CTk.CTkFont(size=15))
            self.phone_number_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["phone"] = self.phone_number_data

            self.social_media_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.social_media_frame.grid(row=3, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.social_media = CTk.CTkLabel(self.social_media_frame, text="Почта:", font=CTk.CTkFont(size=15))
            self.social_media.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.social_media_data = CTk.CTkLabel(self.social_media_frame, text="test@mail.ru", font=CTk.CTkFont(size=15))
            self.social_media_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["email"] = self.social_media_data

            self.status_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.status_frame.grid(row=4, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.status = CTk.CTkLabel(self.status_frame, text="Регион:", font=CTk.CTkFont(size=15))
            self.status.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.status_data = CTk.CTkLabel(self.status_frame, text="Архангельск", font=CTk.CTkFont(size=15))
            self.status_data.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["region"] = self.status_data

        def search_btn_event(self):
            s = socket.socket()
            print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
            s.connect((client.SERVER_HOST, client.SERVER_PORT))
            print("[+] Connected.")
            request = f"210:{self.search_entry.get()}"
            s.send(request.encode())
            message = None
            while message is None:
                message = s.recv(1024).decode()
            print(data := message.lstrip('[').lstrip('(').rstrip(')').rstrip(']').split(','), 'end')
            for key, text in zip(self.volunteer_labels_dict, data):
                print(key, text)
                try:
                    self.volunteer_labels_dict[key].configure(text=text.strip()[1:-1])
                except ValueError:
                    pass

    class StudentEdit:
        def __init__(self, main_frame):
            self.student_labels_dict = dict()

            # Обзор. Добавление фреймов
            self.top_frame = CTk.CTkFrame(master=main_frame, width=640, height=115,
                                          fg_color="transparent")
            self.top_frame.grid(row=0, column=0, padx=(3, 3), pady=(3, 0), sticky="nsew")

            # Тело
            self.mid_frame = CTk.CTkFrame(master=main_frame, width=640, height=550,
                                          fg_color="transparent")
            self.mid_frame.grid(row=1, column=0, padx=(3, 3), pady=(3, 0), sticky="nsew")

            # Кнопки
            self.bottom_frame = CTk.CTkFrame(master=main_frame, width=640, height=70,
                                             fg_color="transparent")
            self.bottom_frame.grid(row=2, column=0, padx=(3, 3), pady=(3, 3), sticky="nsew")

            self.create_btn_frame = CTk.CTkFrame(master=self.bottom_frame, width=100, height=34,
                                                 fg_color="transparent", corner_radius=20)
            self.create_btn_frame.grid(row=0, column=0, padx=(435, 0), pady=(10, 3), sticky="nsew")
            self.create_btn = CTk.CTkButton(self.create_btn_frame, width=100, height=34,
                                            text="Создать", command=self.create_btn_event, corner_radius=20,
                                            font=CTk.CTkFont(size=14))
            self.create_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")

            self.update_btn_frame = CTk.CTkFrame(master=self.bottom_frame, width=100, height=34,
                                                 fg_color="transparent", corner_radius=20)
            self.update_btn_frame.grid(row=0, column=1, padx=(10, 0), pady=(10, 3), sticky="nsew")
            self.update_btn = CTk.CTkButton(self.update_btn_frame, width=100, height=34,
                                            text="Обновить", command=self.update_btn_event, corner_radius=20,
                                            font=CTk.CTkFont(size=14))
            self.update_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")

            # Посиковая строка
            self.search_entry_frame = CTk.CTkFrame(master=self.top_frame, width=200, height=34, fg_color="transparent")
            self.search_entry_frame.grid(row=0, column=0, padx=(360, 3), pady=(10, 10), sticky="nsew")
            self.search_entry = CTk.CTkEntry(self.search_entry_frame, placeholder_text="Поиск", width=200,
                                             height=34, corner_radius=20)
            self.search_entry.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

            self.search_btn_frame = CTk.CTkFrame(master=self.top_frame, width=70, height=34, fg_color="transparent")
            self.search_btn_frame.grid(row=0, column=1, padx=(7, 7), pady=(10, 10), sticky="nsew")
            self.search_btn = CTk.CTkButton(self.search_btn_frame, width=70, height=24,
                                            text="Найти", command=self.search_btn_event, corner_radius=20)
            self.search_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")

            # Поля с инфой
            self.name_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.name_frame.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.name = CTk.CTkLabel(self.name_frame, text="ФИО:", font=CTk.CTkFont(size=15))
            self.name.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.name_entry = CTk.CTkEntry(self.name_frame, placeholder_text="Иванов Иван Иванович", width=200,
                                           height=25, corner_radius=20)
            self.name_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["name"] = self.name_entry

            self.phone_number_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.phone_number_frame.grid(row=1, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.phone_number = CTk.CTkLabel(self.phone_number_frame, text="Телефон:", font=CTk.CTkFont(size=15))
            self.phone_number.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.phone_number_entry = CTk.CTkEntry(self.phone_number_frame, placeholder_text="+7(966)100-10-73",
                                                   width=200, height=25, corner_radius=20)
            self.phone_number_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["phone"] = self.phone_number_entry

            self.social_media_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.social_media_frame.grid(row=2, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.social_media = CTk.CTkLabel(self.social_media_frame, text="Соцсети:", font=CTk.CTkFont(size=15))
            self.social_media.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.social_media_entry = CTk.CTkEntry(self.social_media_frame, placeholder_text="@Serega",
                                                   width=200, height=25, corner_radius=20)
            self.social_media_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["social"] = self.social_media_entry

            self.date_age_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.date_age_frame.grid(row=3, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.date_age = CTk.CTkLabel(self.date_age_frame, text="Дата рождения:", font=CTk.CTkFont(size=15))
            self.date_age.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.data_entry = CTk.CTkEntry(self.date_age_frame, placeholder_text="23.05.2006", width=200,
                                           height=25, corner_radius=20)
            self.data_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["date"] = self.data_entry

            self.age_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.age_frame.grid(row=4, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.age = CTk.CTkLabel(self.age_frame, text="Возраст:", font=CTk.CTkFont(size=15))
            self.age.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.age_entry = CTk.CTkEntry(self.age_frame, placeholder_text="19",
                                          width=200, height=25, corner_radius=20)
            self.age_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["age"] = self.age_entry

            self.status_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.status_frame.grid(row=5, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.status = CTk.CTkLabel(self.status_frame, text="Статус:", font=CTk.CTkFont(size=15))
            self.status.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.status_entry = CTk.CTkEntry(self.status_frame, placeholder_text="В семье",
                                             width=200, height=25, corner_radius=20)
            self.status_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.student_labels_dict["status"] = self.status_entry

        def search_btn_event(self):
            s = socket.socket()
            print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
            s.connect((client.SERVER_HOST, client.SERVER_PORT))
            print("[+] Connected.")
            request = f"230:{self.search_entry.get()}"
            s.send(request.encode())
            message = None
            while message is None:
                message = s.recv(1024).decode()
            print(data := message.lstrip('[').lstrip('(').rstrip(')').rstrip(']').split(','), 'end')
            self.student_labels_dict['name'].delete(0, CTk.END)
            self.student_labels_dict['name'].insert(0, f"{data[0][1:-1]}")
            for key, text in zip(list(self.student_labels_dict.keys())[1:], list(data[1:])):
                print(key, text)
                try:
                    self.student_labels_dict[key].delete(0, CTk.END)
                    self.student_labels_dict[key].insert(0, f"{text[2:-1]}") if len(text) > 3 else \
                        self.student_labels_dict[key].insert(0, f"{text[1:]}")
                except ValueError:
                    pass

        def create_btn_event(self):
            s = socket.socket()
            print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
            s.connect((client.SERVER_HOST, client.SERVER_PORT))
            print("[+] Connected.")
            data = [widget.get() for widget in [self.name_entry, self.phone_number_entry,
                                                self.social_media_entry, self.data_entry, self.age_entry,
                                                self.status_entry]]
            for val in data:
                if val is None:
                    return
            request = "315:{}, {}, {}, {}, {}, {}".format(*data)
            s.send(request.encode())

        def update_btn_event(self):
            s = socket.socket()
            print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
            s.connect((client.SERVER_HOST, client.SERVER_PORT))
            print("[+] Connected.")
            data = [widget.get() for widget in [self.name_entry, self.phone_number_entry,
                                                self.social_media_entry, self.data_entry, self.age_entry,
                                                self.status_entry]]
            for val in data:
                if val is None:
                    return
            request = "310:{}, {}, {}, {}, {}, {}".format(*data)
            s.send(request.encode())

    class VolunteerEdit:
        def __init__(self, main_frame):
            self.volunteer_labels_dict = dict()

            # Обзор. Добавление фреймов
            self.top_frame = CTk.CTkFrame(master=main_frame, width=640, height=115,
                                          fg_color="transparent")
            self.top_frame.grid(row=0, column=0, padx=(3, 3), pady=(3, 0), sticky="nsew")

            # Тело
            self.mid_frame = CTk.CTkFrame(master=main_frame, width=640, height=550,
                                          fg_color="transparent")
            self.mid_frame.grid(row=1, column=0, padx=(3, 3), pady=(3, 0), sticky="nsew")

            # Кнопки
            self.bottom_frame = CTk.CTkFrame(master=main_frame, width=640, height=70,
                                             fg_color="transparent")
            self.bottom_frame.grid(row=2, column=0, padx=(3, 3), pady=(3, 3), sticky="nsew")

            self.create_btn_frame = CTk.CTkFrame(master=self.bottom_frame, width=100, height=34,
                                                 fg_color="transparent", corner_radius=20)
            self.create_btn_frame.grid(row=0, column=0, padx=(435, 0), pady=(10, 3), sticky="nsew")
            self.create_btn = CTk.CTkButton(self.create_btn_frame, width=100, height=34,
                                            text="Создать", command=self.create_btn_event, corner_radius=20,
                                            font=CTk.CTkFont(size=14))
            self.create_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")

            self.update_btn_frame = CTk.CTkFrame(master=self.bottom_frame, width=100, height=34,
                                                 fg_color="transparent", corner_radius=20)
            self.update_btn_frame.grid(row=0, column=0, padx=(540, 0), pady=(10, 3), sticky="nsew")
            self.update_btn = CTk.CTkButton(self.update_btn_frame, width=100, height=34,
                                            text="Обновить", command=self.update_btn_event, corner_radius=20,
                                            font=CTk.CTkFont(size=14))
            self.update_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")

            # Посиковая строка
            self.search_entry_frame = CTk.CTkFrame(master=self.top_frame, width=200, height=34, fg_color="transparent")
            self.search_entry_frame.grid(row=0, column=0, padx=(360, 3), pady=(10, 10), sticky="nsew")
            self.search_entry = CTk.CTkEntry(self.search_entry_frame, placeholder_text="Поиск", width=200,
                                             height=34, corner_radius=20)
            self.search_entry.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

            self.search_btn_frame = CTk.CTkFrame(master=self.top_frame, width=70, height=34, fg_color="transparent")
            self.search_btn_frame.grid(row=0, column=1, padx=(7, 7), pady=(10, 10), sticky="nsew")
            self.search_btn = CTk.CTkButton(self.search_btn_frame, width=70, height=24,
                                            text="Найти", command=self.search_btn_event, corner_radius=20)
            self.search_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")

            # Поля с инфой
            self.name_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.name_frame.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.name = CTk.CTkLabel(self.name_frame, text="ФИО:", font=CTk.CTkFont(size=15))
            self.name.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.name_entry = CTk.CTkEntry(self.name_frame, placeholder_text="Иванов Иван Иванович", width=200,
                                           height=25, corner_radius=20)
            self.name_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["name"] = self.name_entry

            self.date_age_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.date_age_frame.grid(row=1, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.date_age = CTk.CTkLabel(self.date_age_frame, text="Дата рождения:", font=CTk.CTkFont(size=15))
            self.date_age.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.data_entry = CTk.CTkEntry(self.date_age_frame, placeholder_text="23.05.2006", width=200,
                                           height=25, corner_radius=20)
            self.data_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["date"] = self.data_entry

            self.phone_number_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.phone_number_frame.grid(row=2, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.phone_number = CTk.CTkLabel(self.phone_number_frame, text="Телефон:", font=CTk.CTkFont(size=15))
            self.phone_number.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.phone_number_entry = CTk.CTkEntry(self.phone_number_frame, placeholder_text="+7(966)100-10-73",
                                                   width=200, height=25, corner_radius=20)
            self.phone_number_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["phone"] = self.phone_number_entry

            self.email_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.email_frame.grid(row=3, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.email = CTk.CTkLabel(self.email_frame, text="Почта:", font=CTk.CTkFont(size=15))
            self.email.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.email_entry = CTk.CTkEntry(self.email_frame, placeholder_text="test@mail.ru",
                                            width=200, height=25, corner_radius=20)
            self.email_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["email"] = self.email_entry

            self.region_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.region_frame.grid(row=4, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.region = CTk.CTkLabel(self.region_frame, text="Регион:", font=CTk.CTkFont(size=15))
            self.region.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.region_entry = CTk.CTkEntry(self.region_frame, placeholder_text="Москва",
                                             width=200, height=25, corner_radius=20)
            self.region_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["region"] = self.region_entry

            self.tutor_name_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.tutor_name_frame.grid(row=5, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.tutor_name = CTk.CTkLabel(self.tutor_name_frame, text="ФИО куратора:", font=CTk.CTkFont(size=15))
            self.tutor_name.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.tutor_name_entry = CTk.CTkEntry(self.tutor_name_frame, placeholder_text="Иванов Иван Олегович",
                                                 width=200, height=25, corner_radius=20)
            self.tutor_name_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["tutor_name"] = self.tutor_name_entry

            self.social_media_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
            self.social_media_frame.grid(row=6, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            self.social_media = CTk.CTkLabel(self.social_media_frame, text="Соцсети:", font=CTk.CTkFont(size=15))
            self.social_media.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
            self.social_media_entry = CTk.CTkEntry(self.social_media_frame, placeholder_text="@Serega",
                                                   width=200, height=25, corner_radius=20)
            self.social_media_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
            self.volunteer_labels_dict["social"] = self.social_media_entry

            self.choose_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=300, fg_color="transparent")
            self.choose_frame.grid(row=7, column=0, padx=(5, 0), pady=(15, 15), sticky="nsew")

            self.dynamic_grid = list()

            def clean_dynamic_grid():
                for widget in self.dynamic_grid:
                    widget.grid_remove()

            def feel_with_1():
                clean_dynamic_grid()

                self.comment_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
                self.comment_frame.grid(row=8, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.comment = CTk.CTkLabel(self.comment_frame, text="Комментарий:", font=CTk.CTkFont(size=15))
                self.comment.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.comment_entry = CTk.CTkEntry(self.comment_frame, placeholder_text="Все хорошо",
                                                  width=200, height=25, corner_radius=20)
                self.comment_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["comment"] = self.region_entry
                self.dynamic_grid.append(self.comment_frame)
                self.dynamic_grid.append(self.comment)
                self.dynamic_grid.append(self.comment_entry)

                self.subscribe_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
                self.subscribe_frame.grid(row=9, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.check_var = CTk.IntVar(value=0)
                self.checkbox = CTk.CTkCheckBox(self.subscribe_frame, text="Подписка на рассылку",
                                                variable=self.check_var, onvalue=1, offvalue=0,
                                                font=CTk.CTkFont(size=15))
                self.checkbox.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.dynamic_grid.append(self.subscribe_frame)
                self.dynamic_grid.append(self.checkbox)

                self.request_date_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
                self.request_date_frame.grid(row=10, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.request_date = CTk.CTkLabel(self.request_date_frame, text="Дата подачи заявки:",
                                                 font=CTk.CTkFont(size=15))
                self.request_date.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.request_date_entry = CTk.CTkEntry(self.request_date_frame, placeholder_text="00.00.0000",
                                                       width=200, height=25, corner_radius=20)
                self.request_date_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["request_date"] = self.comment_entry
                self.dynamic_grid.append(self.request_date_frame)
                self.dynamic_grid.append(self.request_date)
                self.dynamic_grid.append(self.request_date_entry)

            def feel_with_2():
                clean_dynamic_grid()

                self.comment_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
                self.comment_frame.grid(row=8, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.comment = CTk.CTkLabel(self.comment_frame, text="Комментарий:", font=CTk.CTkFont(size=15))
                self.comment.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.comment_entry = CTk.CTkEntry(self.comment_frame, placeholder_text="Все отлично",
                                                  width=200, height=25, corner_radius=20)
                self.comment_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["comment"] = self.region_entry
                self.dynamic_grid.append(self.comment_frame)
                self.dynamic_grid.append(self.comment)
                self.dynamic_grid.append(self.comment_entry)

                self.subscribe_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
                self.subscribe_frame.grid(row=9, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.check_var = CTk.IntVar(value=0)
                self.checkbox = CTk.CTkCheckBox(self.subscribe_frame, text="Подписка на рассылку",
                                                variable=self.check_var, onvalue=1, offvalue=0,
                                                font=CTk.CTkFont(size=15))
                self.checkbox.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.dynamic_grid.append(self.subscribe_frame)
                self.dynamic_grid.append(self.checkbox)

                self.request_date_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                       fg_color="transparent")
                self.request_date_frame.grid(row=10, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.request_date = CTk.CTkLabel(self.request_date_frame, text="Дата подачи заявки:",
                                                 font=CTk.CTkFont(size=15))
                self.request_date.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.request_date_entry = CTk.CTkEntry(self.request_date_frame, placeholder_text="00.00.0000",
                                                       width=200, height=25, corner_radius=20)
                self.request_date_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["request_date"] = self.comment_entry
                self.dynamic_grid.append(self.request_date_frame)
                self.dynamic_grid.append(self.request_date)
                self.dynamic_grid.append(self.request_date_entry)

                self.deny_reason_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                      fg_color="transparent")
                self.deny_reason_frame.grid(row=11, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.deny_reason = CTk.CTkLabel(self.deny_reason_frame, text="Причина отказа:",
                                                font=CTk.CTkFont(size=15))
                self.deny_reason.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.deny_reason_entry = CTk.CTkEntry(self.deny_reason_frame, placeholder_text="Рад всех видеть",
                                                      width=200, height=25, corner_radius=20)
                self.deny_reason_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["deny_reason"] = self.comment_entry
                self.dynamic_grid.append(self.deny_reason_frame)
                self.dynamic_grid.append(self.deny_reason)
                self.dynamic_grid.append(self.deny_reason_entry)

            def feel_with_3():
                clean_dynamic_grid()

                self.comment_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
                self.comment_frame.grid(row=8, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.comment = CTk.CTkLabel(self.comment_frame, text="Комментарий:", font=CTk.CTkFont(size=15))
                self.comment.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.comment_entry = CTk.CTkEntry(self.comment_frame, placeholder_text="Все супер",
                                                  width=200, height=25, corner_radius=20)
                self.comment_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["comment"] = self.comment_entry
                self.dynamic_grid.append(self.comment_frame)
                self.dynamic_grid.append(self.comment)
                self.dynamic_grid.append(self.comment_entry)

                self.subscribe_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
                self.subscribe_frame.grid(row=9, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.check_var = CTk.IntVar(value=0)
                self.checkbox = CTk.CTkCheckBox(self.subscribe_frame, text="Подписка на рассылку",
                                                variable=self.check_var, onvalue=1, offvalue=0,
                                                font=CTk.CTkFont(size=15))
                self.checkbox.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.dynamic_grid.append(self.subscribe_frame)
                self.dynamic_grid.append(self.checkbox)

                self.request_date_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                       fg_color="transparent")
                self.request_date_frame.grid(row=10, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.request_date = CTk.CTkLabel(self.request_date_frame, text="Дата подачи заявки:",
                                                 font=CTk.CTkFont(size=15))
                self.request_date.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.request_date_entry = CTk.CTkEntry(self.request_date_frame, placeholder_text="00.00.0000",
                                                       width=200, height=25, corner_radius=20)
                self.request_date_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["request_date"] = self.request_date_entry
                self.dynamic_grid.append(self.request_date_frame)
                self.dynamic_grid.append(self.request_date)
                self.dynamic_grid.append(self.request_date_entry)

                self.training_date_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                        fg_color="transparent")
                self.training_date_frame.grid(row=11, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.training_date = CTk.CTkLabel(self.training_date_frame, text="Дата прохождения тренинга:",
                                                  font=CTk.CTkFont(size=15))
                self.training_date.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.training_date_entry = CTk.CTkEntry(self.training_date_frame, placeholder_text="00.00.0000",
                                                        width=200, height=25, corner_radius=20)
                self.training_date_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["training_date"] = self.training_date_entry
                self.dynamic_grid.append(self.training_date_frame)
                self.dynamic_grid.append(self.training_date)
                self.dynamic_grid.append(self.training_date_entry)

                self.status_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                 fg_color="transparent")
                self.status_frame.grid(row=12, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.status = CTk.CTkLabel(self.status_frame, text="Статус:",
                                           font=CTk.CTkFont(size=15))
                self.status.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.status_entry = CTk.CTkEntry(self.status_frame, placeholder_text="Не женат",
                                                 width=200, height=25, corner_radius=20)
                self.status_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["status"] = self.status_entry
                self.dynamic_grid.append(self.status_frame)
                self.dynamic_grid.append(self.status)
                self.dynamic_grid.append(self.status_entry)

                self.age_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                              fg_color="transparent")
                self.age_frame.grid(row=13, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.age = CTk.CTkLabel(self.age_frame, text="Возраст:",
                                        font=CTk.CTkFont(size=15))
                self.age.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.age_entry = CTk.CTkEntry(self.age_frame, placeholder_text="99",
                                              width=200, height=25, corner_radius=20)
                self.age_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["age"] = self.age_entry
                self.dynamic_grid.append(self.age_frame)
                self.dynamic_grid.append(self.age)
                self.dynamic_grid.append(self.age_entry)

                self.deny_reason_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                      fg_color="transparent")
                self.deny_reason_frame.grid(row=14, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.deny_reason = CTk.CTkLabel(self.deny_reason_frame, text="Причина отказа:",
                                                font=CTk.CTkFont(size=15))
                self.deny_reason.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.deny_reason_entry = CTk.CTkEntry(self.deny_reason_frame, placeholder_text="Рад всем",
                                                      width=200, height=25, corner_radius=20)
                self.deny_reason_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["deny_reason"] = self.deny_reason_entry
                self.dynamic_grid.append(self.deny_reason_frame)
                self.dynamic_grid.append(self.deny_reason)
                self.dynamic_grid.append(self.deny_reason_entry)

            def feel_with_4():
                self.training_date_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                        fg_color="transparent")
                self.training_date_frame.grid(row=8, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.training_date = CTk.CTkLabel(self.training_date_frame, text="Дата прохождения тренинга:",
                                                  font=CTk.CTkFont(size=15))
                self.training_date.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.training_date_entry = CTk.CTkEntry(self.training_date_frame, placeholder_text="00.00.0000",
                                                        width=200, height=25, corner_radius=20)
                self.training_date_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["training_date"] = self.training_date_entry
                self.dynamic_grid.append(self.training_date_frame)
                self.dynamic_grid.append(self.training_date)
                self.dynamic_grid.append(self.training_date_entry)

                self.status_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                 fg_color="transparent")
                self.status_frame.grid(row=9, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.status = CTk.CTkLabel(self.status_frame, text="Статус:",
                                           font=CTk.CTkFont(size=15))
                self.status.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.status_entry = CTk.CTkEntry(self.status_frame, placeholder_text="Не женат",
                                                 width=200, height=25, corner_radius=20)
                self.status_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["status"] = self.status_entry
                self.dynamic_grid.append(self.status_frame)
                self.dynamic_grid.append(self.status)
                self.dynamic_grid.append(self.status_entry)

                self.contact_date_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                       fg_color="transparent")
                self.contact_date_frame.grid(row=10, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.contact_date = CTk.CTkLabel(self.contact_date_frame, text="Дата последнего контакта:",
                                                 font=CTk.CTkFont(size=15))
                self.contact_date.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.contact_date_entry = CTk.CTkEntry(self.contact_date_frame, placeholder_text="00.00.0000",
                                                       width=200, height=25, corner_radius=20)
                self.contact_date_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["contact_date"] = self.contact_date_entry
                self.dynamic_grid.append(self.contact_date_frame)
                self.dynamic_grid.append(self.contact_date)
                self.dynamic_grid.append(self.contact_date_entry)

                self.sources_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50,
                                                  fg_color="transparent")
                self.sources_frame.grid(row=11, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.sources = CTk.CTkLabel(self.sources_frame, text="Источник:",
                                            font=CTk.CTkFont(size=15))
                self.sources.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.optionmenu_var = CTk.StringVar(value="Соцсети")
                self.sources_optionmenu = CTk.CTkOptionMenu(self.sources_frame, values=["Интернет-Сми", "Соцсети",
                                                                                        "Портал", "Знакомые/коллеги",
                                                                                        "Блогеры", "«Давай дружить»",
                                                                                        "от наставника",
                                                                                        "от сотрудника",
                                                                                        "Сбербанк", "от работодателя",
                                                                                        "ДОДО", "Другой Фонд",
                                                                                        "ЦССВ/ШПР/опека", "СМИ",
                                                                                        "радио", "ТВ",
                                                                                        "наружная реклама",
                                                                                        "другое"],
                                                            variable=self.optionmenu_var)
                self.sources_optionmenu.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["status"] = self.sources_optionmenu
                self.dynamic_grid.append(self.sources_frame)
                self.dynamic_grid.append(self.sources)
                self.dynamic_grid.append(self.sources_optionmenu)

                self.comment_frame = CTk.CTkFrame(master=self.mid_frame, width=640, height=50, fg_color="transparent")
                self.comment_frame.grid(row=12, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
                self.comment = CTk.CTkLabel(self.comment_frame, text="Комментарий:", font=CTk.CTkFont(size=15))
                self.comment.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))
                self.comment_entry = CTk.CTkEntry(self.comment_frame, placeholder_text="Люблю всех",
                                                  width=200, height=25, corner_radius=20)
                self.comment_entry.grid(row=0, column=1, padx=(5, 0), pady=(0, 0))
                self.volunteer_labels_dict["comment"] = self.comment_entry
                self.dynamic_grid.append(self.comment_frame)
                self.dynamic_grid.append(self.comment)
                self.dynamic_grid.append(self.comment_entry)

            def radiobutton_event():
                print("radiobutton toggled, current value:", self.radio_var.get())
                way_to_feel[int(self.radio_var.get())]()

            way_to_feel = {
                1: feel_with_1,
                2: feel_with_2,
                3: feel_with_3,
                4: feel_with_4,
            }

            self.radio_var = CTk.IntVar(value=0)
            radiobutton_1 = CTk.CTkRadioButton(self.choose_frame, text="Кандидат в наставники",
                                               command=radiobutton_event, variable=self.radio_var, value=1,
                                               border_width_unchecked=2, font=CTk.CTkFont(size=15))
            radiobutton_2 = CTk.CTkRadioButton(self.choose_frame, text="Отказники",
                                               command=radiobutton_event, variable=self.radio_var, value=2,
                                               border_width_unchecked=2, font=CTk.CTkFont(size=15))
            radiobutton_3 = CTk.CTkRadioButton(self.choose_frame, text="Прошел тренинг",
                                               command=radiobutton_event, variable=self.radio_var, value=3,
                                               border_width_unchecked=2, font=CTk.CTkFont(size=15))
            radiobutton_4 = CTk.CTkRadioButton(self.choose_frame, text="Волонтер",
                                               command=radiobutton_event, variable=self.radio_var, value=4,
                                               border_width_unchecked=2, font=CTk.CTkFont(size=15))
            radiobutton_1.grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            radiobutton_2.grid(row=1, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            radiobutton_3.grid(row=2, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")
            radiobutton_4.grid(row=3, column=0, padx=(5, 0), pady=(5, 0), sticky="nsew")

        def search_btn_event(self):
            s = socket.socket()
            print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
            s.connect((client.SERVER_HOST, client.SERVER_PORT))
            print("[+] Connected.")
            if self.radio_var.get() == 0:
                request = f"210:{self.search_entry.get()}"
                s.send(request.encode())
                message = None
                while message is None:
                    message = s.recv(1024).decode()
                print(data := message.lstrip('[').lstrip('(').rstrip(')').rstrip(']').split(','), 'end')
                self.volunteer_labels_dict['name'].delete(0, CTk.END)
                self.volunteer_labels_dict['name'].insert(0, f"{data[0][1:-1]}")
                data.append('-')
                for key, text in zip(list(self.volunteer_labels_dict.keys())[1:], data[1:]):
                    print(key, text)
                    try:
                        self.volunteer_labels_dict[key].delete(0, CTk.END)
                        self.volunteer_labels_dict[key].insert(0, f"{text[2:-1]}")
                    except ValueError:
                        pass
                self.volunteer_labels_dict['social'].delete(0, CTk.END)
                self.volunteer_labels_dict['social'].insert(0, '-')
            elif self.radio_var.get() == 1:
                request = f"220:{self.search_entry.get()}"
                s.send(request.encode())
                message = None
                while message is None:
                    message = s.recv(1024).decode()
                print(data := message.lstrip('[').lstrip('(').rstrip(')').rstrip(']').split(','), 'end')
            elif self.radio_var.get() == 2:
                request = f"230:{self.search_entry.get()}"
            elif self.radio_var.get() == 3:
                request = f"240:{self.search_entry.get()}"
            elif self.radio_var.get() == 4:
                request = f"250:{self.search_entry.get()}"
            else:
                return

        def create_btn_event(self):
            s = socket.socket()
            print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
            s.connect((client.SERVER_HOST, client.SERVER_PORT))
            print("[+] Connected.")
            print(self.radio_var, '!')
            data = [widget.get() for widget in [self.name_entry, self.data_entry, self.phone_number_entry,
                                                self.email_entry, self.region_entry, self.tutor_name_entry]]
            for val in data:
                if val is None:
                    return
            request = "300:{}, {}, {}, {}, {}, {}".format(*data)
            s.send(request.encode())
            if self.radio_var.get() == 1:
                s = socket.socket()
                print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
                s.connect((client.SERVER_HOST, client.SERVER_PORT))
                print("[+] Connected.")
                data = [widget.get() for widget in [self.name_entry, self.data_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry,
                                                    self.social_media_entry, self.dynamic_grid[2], self.dynamic_grid[4],
                                                    self.dynamic_grid[7]]]
                for val in data:
                    if val is None:
                        return
                request = "320:{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())
            elif self.radio_var.get() == 2:
                s = socket.socket()
                print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
                s.connect((client.SERVER_HOST, client.SERVER_PORT))
                print("[+] Connected.")
                data = [widget.get() for widget in [self.name_entry, self.data_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry,
                                                    self.social_media_entry, self.dynamic_grid[2], self.dynamic_grid[4],
                                                    self.dynamic_grid[7], self.dynamic_grid[10]]]
                for val in data:
                    if val is None:
                        return
                request = "330:{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())
            elif self.radio_var.get() == 3:
                s = socket.socket()
                print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
                s.connect((client.SERVER_HOST, client.SERVER_PORT))
                print("[+] Connected.")
                data = [widget.get() for widget in [self.name_entry, self.data_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry,
                                                    self.social_media_entry, self.dynamic_grid[2], self.dynamic_grid[4],
                                                    self.dynamic_grid[7], self.dynamic_grid[10], self.dynamic_grid[13],
                                                    self.dynamic_grid[16], self.dynamic_grid[19]]]
                for val in data:
                    if val is None:
                        return
                request = "340:{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())
            elif self.radio_var.get() == 4:
                s = socket.socket()
                print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
                s.connect((client.SERVER_HOST, client.SERVER_PORT))
                print("[+] Connected.")
                data = [widget.get() for widget in [self.name_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry,
                                                    self.social_media_entry, self.dynamic_grid[2], self.dynamic_grid[5],
                                                    self.dynamic_grid[8], self.dynamic_grid[11], self.dynamic_grid[14]]]
                for val in data:
                    if val is None:
                        return
                request = "350:{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())
                print('done')
            else:
                pass

        def update_btn_event(self):
            s = socket.socket()
            print(f"[*] Connecting to {client.SERVER_HOST}:{client.SERVER_PORT}...")
            s.connect((client.SERVER_HOST, client.SERVER_PORT))
            print("[+] Connected.")
            print(self.radio_var, '!')
            if self.radio_var.get() == 0:
                data = [widget.get() for widget in [self.name_entry, self.data_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry]]
                for val in data:
                    if val is None:
                        return
                request = "305:{}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())
            elif self.radio_var.get() == 1:
                data = [widget.get() for widget in [self.name_entry, self.data_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry,
                                                    self.social_media_entry, self.dynamic_grid[2], self.dynamic_grid[4],
                                                    self.dynamic_grid[7]]]
                for val in data:
                    if val is None:
                        return
                request = "325:{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())
            elif self.radio_var.get() == 2:
                data = [widget.get() for widget in [self.name_entry, self.data_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry,
                                                    self.social_media_entry, self.dynamic_grid[2], self.dynamic_grid[4],
                                                    self.dynamic_grid[7], self.dynamic_grid[10]]]
                for val in data:
                    if val is None:
                        return
                request = "335:{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())
            elif self.radio_var.get() == 3:
                data = [widget.get() for widget in [self.name_entry, self.data_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry,
                                                    self.social_media_entry, self.dynamic_grid[2], self.dynamic_grid[4],
                                                    self.dynamic_grid[7], self.dynamic_grid[10], self.dynamic_grid[13],
                                                    self.dynamic_grid[16], self.dynamic_grid[19]]]
                for val in data:
                    if val is None:
                        return
                request = "345:{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())
            elif self.radio_var.get() == 4:
                data = [widget.get() for widget in [self.name_entry, self.phone_number_entry,
                                                    self.email_entry, self.region_entry, self.tutor_name_entry,
                                                    self.social_media_entry, self.dynamic_grid[2], self.dynamic_grid[5],
                                                    self.dynamic_grid[8], self.dynamic_grid[11], self.dynamic_grid[14]]]
                for val in data:
                    if val is None:
                        return
                request = "355:{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*data)
                s.send(request.encode())

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Вкладки
        self.add("Подопечный обзор")
        self.add("Волонтер обзор")
        self.add("Подопечный изменить")
        self.add("Волонтер изменить")
        self.add("Куратор изменить")

        self.StudentReview(self.tab("Подопечный обзор"))
        self.VolunteerReview(self.tab("Волонтер обзор"))
        self.StudentEdit(self.tab("Подопечный изменить"))
        self.VolunteerEdit(self.tab("Волонтер изменить"))
