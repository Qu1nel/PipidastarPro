import datetime
import random
import socket
import sqlite3
from threading import Thread

SERVER_HOST = "77.232.131.231"
SERVER_PORT = 5002

client_sockets = dict()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")


def func_200(msg: str, cs=None):
    # print("Here is data")
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM padavan WHERE fio=?', (msg.split(':')[1],)).fetchall()
    response = f"{str(res)}"
    # print(response)
    cs.send(response.encode())
    exit()


def func_210(msg: str, cs=None):
    # print("Here is data")
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM persons WHERE fio=?', (msg.split(':')[1],)).fetchall()
    response = f"{str(res)}"
    # print(response)
    cs.send(response.encode())
    exit()


def func_220(msg: str, cs=None):
    # print("Here is data")
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM candidates_mentor WHERE fio=?', (msg.split(':')[1],)).fetchall()
    response = f"{str(res)}"
    # print(response)
    cs.send(response.encode())
    exit()


def func_230(msg: str, cs=None):
    # print("Here is data")
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM candidates_cancels WHERE fio=?', (msg.split(':')[1],)).fetchall()
    response = f"{str(res)}"
    # print(response)
    cs.send(response.encode())
    exit()


def func_240(msg: str, cs=None):
    # print("Here is data")
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM candidates_passed_training WHERE fio=?', (msg.split(':')[1],)).fetchall()
    response = f"{str(res)}"
    # print(response)
    cs.send(response.encode())
    exit()


def func_250(msg: str, cs=None):
    # print("Here is data")
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM volunteers WHERE fio=?', (msg.split(':')[1],)).fetchall()
    response = f"{str(res)}"
    # print(response)
    cs.send(response.encode())
    exit()


def func_300(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO persons (fio, birthday, number_phone, email, region, fio_curator) VALUES (?, ?, ?, ?, ?, ?)',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM persons')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_305(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    data.append(data[0])
    data.pop(0)
    print(data)
    cursor.execute('UPDATE persons SET birthday=?, number_phone=?, email=?, region=?, fio_curator=? WHERE fio=?',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM persons')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_310(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    data.append(data[0])
    data.pop(0)
    print(data)
    cursor.execute('UPDATE padavan SET number_phone=?, social_media=?, birthday=?, age=?, status=? WHERE fio=?',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM padavan')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_315(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO padavan (fio, number_phone, social_media, birthday, age, status) VALUES (?, ?, ?, ?, ?, ?)',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM padavan')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()



def func_320(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    data.append('ДОДО')
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append('Неизвестно')
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO candidates_mentor (fio, birthday, number_phone, email, region, fio_curator, social_media, comment, subscription, date_of_request, source, date_supply, date_send, date_written, date_interview, past_job) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM candidates_mentor')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_325(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    data.append('ДОДО')
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append('Неизвестно')
    data.append(data[0])
    data.pop(0)
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE candidates_mentor SET birthday=?, number_phone=?, email=?, region=?, fio_curator=?, social_media=?, comment=?, subscription=?, date_of_request=?, source=?, date_supply=?, date_send=?, date_written=?, date_interview=?, past_job=?) WHERE fio=?',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM candidates_mentor')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_330(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    data.append('ДОДО')
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append('Неизвестно')
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO candidates_cancels (fio, birthday, number_phone, email, region, fio_curator, social_media, comment, subscription, date_of_request, cancel_reason, source, date_supply, date_send, date_written, date_interview, past_job) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM candidates_cancels')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_335(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    data.append('ДОДО')
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append('Неизвестно')
    data.append(data[0])
    data.pop(0)
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE candidates_cancels SET birthday=?, number_phone=?, email=?, region=?, fio_curator=?, social_media=?, comment=?, subscription=?, date_of_request=?, cancel_reason=?, source=?, date_supply=?, date_send=?, date_written=?, date_interview=?, past_job=? WHERE fio=?',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM candidates_cancels')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_340(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    data.append('ДОДО')
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append('Неизвестно')
    data.append(random.randint(1, 100))
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO candidates_passed_training (fio, birthday, number_phone, email, region, fio_curator, social_media, comment, subscription, date_of_request, date_of_training_ending, status, age, cancel_reason, source, date_supply, date_send, date_written, date_interview, past_job, passwd) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM candidates_passed_training')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_345(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    data.append('ДОДО')
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append('Неизвестно')
    data.append(random.randint(1, 100))
    data.append(data[0])
    data.pop(0)
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE candidates_passed_training SET birthday=?, number_phone=?, email=?, region=?, fio_curator=?, social_media=?, comment=?, subscription=?, date_of_request=?, date_of_training_ending=?, status=?, age=?, cancel_reason=?, source=?, date_supply=?, date_send=?, date_written=?, date_interview=?, past_job=?, passwd=? WHERE fio=?',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM candidates_passed_training')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_350(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append('Неизвестно')
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO volunteers (fio, number_phone, email, region, fio_curator, social_media, date_of_request, status, date_of_last_contact, source, comment, date_supply, date_send, date_written, date_interview, past_job) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM volunteers')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


def func_355(msg: str, cs=None):
    data = list(map(str.strip, msg.split(':')[1].split(',')))
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    data.append('Неизвестно')
    data.append(data[0])
    data.pop(0)
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE volunteers SET number_phone=?, email=?, region=?, fio_curator=?, social_media=?, date_of_request=?, status=?, date_of_last_contact=?, source=?, comment=?, date_supply=?, date_send=?, date_written=?, date_interview=?, past_job=? WHERE fio=?',
                   tuple(data))
    connection.commit()
    cursor.execute('SELECT * FROM volunteers')
    events = cursor.fetchall()
    for event in events:
        print(event)
    exit()


code_dict = {
    "200": func_200,
    "210": func_210,
    "220": func_220,
    "230": func_230,
    "240": func_240,
    "250": func_250,
    "300": func_300,
    "305": func_305,
    "310": func_310,
    "315": func_315,
    "320": func_320,
    "325": func_325,
    "330": func_330,
    "335": func_335,
    "340": func_340,
    "345": func_345,
    "350": func_350,
    "355": func_355,
}


def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
            print(msg)
        except Exception as e:
            print(f"[!] Error: {e}")
            return
        else:
            try:
                code_dict[msg.split(':')[0]](msg, cs=cs)
            except KeyError:
                pass


while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()
