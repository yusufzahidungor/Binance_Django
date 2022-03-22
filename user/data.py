# with open("sample4.json") as f:
#     data = json.load(f)

# for item in data:
#     cursor.execute("""INSERT INTO people (firstName,lastName,gender,age,numberr) VALUES(?,?,?,?,?)""",(item['firstName'],item['lastName'],item['gender'],item['age'],item['numberr']))
#     con.commit()

import websocket
import json, pprint
import time
import sqlite3

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"


def on_open(ws):
    print('opened connection')


def on_close(ws):
    print('closed connection')


def on_message(ws, message):
    #global closes, in_position

    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)
    time.sleep(10) #10 saniye

#pip install websocket-client  
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()