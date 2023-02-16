from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QComboBox
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon, QPixmap
from random import choice
import requests

url1 = requests.get(
    "https://api.cryptorank.io/v1/currencies?api_key=2dbf562e70708772d3ef5912379549bfec68d781bcb3e23dc9238db912b9")
url = url1.json()
dc = {}
global bitcoin, Ethereum, BNB, Riple, EOS, Bitcoin_cash
bitcoin = 0
Ethereum = 0
BNB = 0
Riple = 0
EOS = 0
Bitcoin_cash = 0

bitcoin = round(url["data"][0]["values"]["USD"]["price"], 3)
Ethereum = round(url["data"][1]["values"]["USD"]["price"], 3)
BNB = round(url["data"][3]["values"]["USD"]["price"], 3)
Riple = round(url["data"][5]["values"]["USD"]["price"], 3)
EOS = round(url["data"][8]["values"]["USD"]["price"], 3)
Bitcoin_cash = round(url["data"][11]["values"]["USD"]["price"], 3)


class MyWindow(QMainWindow):

    def __init__(self, width=700, height=700, title="123") -> None:
        super().__init__()

        self.setWindowIcon(QIcon("binance.png"))
        self.setWindowTitle("Binance")
        self.setGeometry(1000, 600, width, height)
        self.setFixedSize(1000, 600)
        st = """ background-color: gray; color: black; font-size: 20px;border-style: outset;border-width: 2px;border-radius: 15px;padding: 4px;"""
        self.m_lbl = QLabel(
            "Зарегистрируйтесь     и     получите     100    $", self)
        self.m_lbl.setStyleSheet(st)
        self.m_lbl.setGeometry(250, 50, 470, 30)
        self.glav = QLabel(self)
        glav1 = QPixmap("odamcha.png").scaled(QtCore.QSize(50, 50))
        self.glav.setPixmap(glav1)
        self.glav.setGeometry(10, 10, 50, 50)
        self.glav = QIcon("odamcha.png")
        self.search = QLabel(self)
        search1 = QPixmap("search.png").scaled(QtCore.QSize(50, 50))
        self.search.setPixmap(search1)
        self.search.setGeometry(800, 10, 50, 50)
        self.search = QIcon("search.png")
        self.scaner = QLabel(self)
        scaner1 = QPixmap("scaner.png").scaled(QtCore.QSize(60, 60))
        self.scaner.setPixmap(scaner1)
        self.scaner.setGeometry(900, 10, 50, 50)
        self.scaner = QIcon("scaner.png")
        style1 = """ background-color: white;order-style: outset;border-width: 2px;border-radius: 15px;padding: 4px;"""
        self.m_btn = QPushButton("Зарегистрироваться", self)
        self.m_btn.setStyleSheet(style1)
        self.m_btn.setGeometry(250, 100, 150, 30)
        style2 = """ background-color: yellow;border-style: outset;border-width: 2px;border-radius: 15px;padding: 4px;"""
        self.m_btn1 = QPushButton("Логин", self)
        self.m_btn1.setStyleSheet(style2)
        self.m_btn1.setGeometry(570, 100, 150, 30)
        st = """color: gray; font-size: 17px"""
        self.m_lbl = QLabel("Ваш список", self)
        self.m_lbl.setStyleSheet(st)
        self.m_lbl.setGeometry(20, 140, 100, 25)
        st1 = """color: black; font-size: 17px"""
        self.m_lbl = QLabel("Монета", self)
        self.m_lbl.setStyleSheet(st1)
        self.m_lbl.setGeometry(150, 140, 100, 25)
        style1 = """ background-color: white;color: gray"""
        self.bitcoin = QPushButton(f"Bitcoin BTC\n$ {bitcoin}", self)
        self.bitcoin.setStyleSheet(style1)
        self.bitcoin.setGeometry(20, 200, 100, 50)
        self.Ethereum = QPushButton(f"Ethereum ETH\n$ {Ethereum}", self)
        self.Ethereum.setStyleSheet(style1)
        self.Ethereum.setGeometry(20, 270, 100, 50)
        self.Bitcoin_cash = QPushButton(f"Solana SOL\n$ {Bitcoin_cash}", self)
        self.Bitcoin_cash.setStyleSheet(style1)
        self.Bitcoin_cash.setGeometry(20, 340, 100, 50)
        st0 = """color: red; font-size: 17px"""
        self.bit = QLabel(f"$ {bitcoin}", self)
        self.bit.setStyleSheet(st0)
        self.bit.setGeometry(250, 200, 150, 30)
        self.eth = QLabel(f"$ {Ethereum}", self)
        self.eth.setStyleSheet(st0)
        self.eth.setGeometry(250, 270, 150, 30)
        self.btc = QLabel(f"$ {Bitcoin_cash}", self)
        self.btc.setStyleSheet(st0)
        self.btc.setGeometry(250, 340, 150, 30)
        self.BNB = QPushButton(f"BNB BNB\n$ {BNB}", self)
        self.BNB.setStyleSheet(style1)
        self.BNB.setGeometry(520, 200, 100, 50)
        self.Riple = QPushButton(f"Riple XRP\n$ {Riple}", self)
        self.Riple.setStyleSheet(style1)
        self.Riple.setGeometry(520, 270, 100, 50)
        self.EOS = QPushButton(f"Dogecoin DOGE\n$ {EOS}", self)
        self.EOS.setStyleSheet(style1)
        self.EOS.setGeometry(520, 340, 100, 50)
        st11 = """color: green; font-size: 17px"""
        self.bnb = QLabel(f"$ {BNB}", self)
        self.bnb.setStyleSheet(st11)
        self.bnb.setGeometry(750, 200, 150, 30)
        self.rp = QLabel(f"$ {Riple}", self)
        self.rp.setStyleSheet(st11)
        self.rp.setGeometry(750, 270, 150, 30)
        self.es = QLabel(f"$ {EOS}", self)
        self.es.setStyleSheet(st11)
        self.es.setGeometry(750, 340, 150, 30)
        icon1 = QIcon("arrow.png")
        st7 = """background-color:yellow;border-style: outset;border-width: 2px;border-radius: 15px;padding: 4px;"""
        self.k_upd = QPushButton(icon1, "Update", self)
        self.k_upd.setGeometry(450, 500, 75, 50)
        self.k_upd.setStyleSheet(st7)

        self.k_upd.clicked.connect(self.kurs1)

    def kurs1(self):
        dic = self.kurs()
        print(dic)
        bitcoin0=dic['1']
        Ethereum0 = dic['2']
        BNB0 = dic['3']
        Riple0 = dic['4']
        EOS0 = dic['5']
        Bitcoin_cash0 = dic['6']

        self.bit.setText(str(bitcoin0))
        self.eth.setText(str(Ethereum0))
        self.btc.setText(str(Bitcoin_cash0))
        self.bnb.setText(str(BNB0))
        self.rp.setText(str(Riple0))
        self.es.setText(str(EOS0))
        icon1 = QIcon("arrow.png")
        rang = ["white", "blue", "green"]
        rang1 = choice(rang)
        st7 = """background-color:rang1;border-style: outset;border-width: 2px;border-radius: 15px;padding: 4px;"""
        self.k_upd = QPushButton(icon1, "Update", self)
        self.k_upd.setGeometry(450, 500, 75, 50)
        self.k_upd.setStyleSheet(st7)

    def kurs(self):
        url1 = requests.get(
            "https://api.cryptorank.io/v1/currencies?api_key=2dbf562e70708772d3ef5912379549bfec68d781bcb3e23dc9238db912b9")
        url = url1.json()
        bitcoin1 = round(url["data"][0]["values"]["USD"]["price"], 3)
        Ethereum1 = round(url["data"][1]["values"]["USD"]["price"], 3)
        BNB1 = round(url["data"][3]["values"]["USD"]["price"], 3)
        Riple1 = round(url["data"][5]["values"]["USD"]["price"], 3)
        EOS1 = round(url["data"][8]["values"]["USD"]["price"], 3)
        Bitcoin_cash1 = round(url["data"][11]["values"]["USD"]["price"], 3)
        global dc
        dc = {
            '1': bitcoin1,
            '2': Ethereum1,
            '3': BNB1,
            '4': Riple1,
            '5': EOS1,
            '6': Bitcoin_cash1
        }
        return dc
