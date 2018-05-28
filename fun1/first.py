import mysql.connector
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class Fun1:
    cnx = mysql.connector.connect(user='root', password='razor',
                                  host='127.0.0.1', database='calendar')

    def showevents(self):

        cursor = Functions1.cnx.cursor()

        query = ("SELECT * FROM calendar.event")
        cursor.execute(query)
        for (x) in cursor:
            t = x[3]
            print("Nazwa: " + x[1] + ", Opis: " + x[2] + ", Data: "
                  + t.strftime('%m/%d/%Y'))
        cursor.close()
        input()

    def addevent(self):

        name = input("Nazwa:\n")
        desc = input("Opis:\n")
        year = input("Rok:\n")
        month = input("Miesiac:\n")
        day = input("Dzien:\n")
        type = input("Typ powtarzania(0 - brak, d - dzien, "
                     "m - miesiac, y - rok):\n")
        freq = input("Czestotliwosc powtarzania:\n")

        add_event = ("INSERT INTO event (id, name, "
                     "description, start, type, frequency) "
                     "VALUES (%s, %s, %s, %s, %s, %s)")

        if type == "0":
            cr = Functions1.cnx.cursor()
            cursor = Functions1.cnx.cursor()
            query = ("select max(id) as id from event")
            cr.execute(query)
            for (x) in cursor:
                id = x[0] + 1
            cr.close()

            data = (str(id), name, desc,
                    date(int(year), int(month),
                         int(day)), type, freq)
            cursor.execute(add_event, data)

        elif type == "d":
            fr = 0
            for x in range(0, 30):
                cr = Functions1.cnx.cursor()
                cursor = Functions1.cnx.cursor()

                query = ("select max(id) as id from event")
                cr.execute(query)
                for (y) in cursor:
                    id = y[0] + 1
                cr.close()

                data = (str(id), name, desc,
                        date(int(year), int(month),
                             int(day)) + timedelta(days=fr), type, freq)
                cursor.execute(add_event, data)
                fr = fr + int(freq)

        elif type == "m":
            fr = 0
            for x in range(0, 12):
                cr = Functions1.cnx.cursor()
                cursor = Functions1.cnx.cursor()

                query = ("select max(id) as id from event")
                cr.execute(query)
                for (y) in cursor:
                    id = y[0] + 1
                cr.close()

                data = (str(id), name, desc,
                        date(int(year), int(month),
                             int(day)) + relativedelta(months=fr), type, freq)
                cursor.execute(add_event, data)
                fr = fr + int(freq)
        elif type == "y":
            fr = 0
            for x in range(0, 2):
                cr = Functions1.cnx.cursor()
                cursor = Functions1.cnx.cursor()

                query = ("select max(id) as id from event")
                cr.execute(query)
                for (y) in cursor:
                    id = y[0] + 1
                cr.close()

                data = (str(id), name, desc,
                        date(int(year), int(month),
                             int(day)) + relativedelta(months=fr * 12),
                        type, freq)
                cursor.execute(add_event, data)
                fr = fr + int(freq)

        Functions1.cnx.commit()
        cursor.close()
        input()

