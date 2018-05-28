import mysql.connector
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


class Fun2:
    cnx = mysql.connector.connect(user='root', password='razor',
                                  host='127.0.0.1', database='calendar')

    def deleteevent(self):

        name = input("Nazwa:\n")
        cursor = Fun2.cnx.cursor()
        query = "delete from event where name = %s"
        cursor.execute(query, (name,))
        Fun2.cnx.commit()
        cursor.close()

    def sortedevents(self):
        cursor = Fun2.cnx.cursor()
        query = ("SELECT * FROM calendar.event where start < now() "
                 "+ interval 30 day and start > now() order by start")
        cursor.execute(query)

        for (x) in cursor:
            t = x[3]
            print("Nazwa: " + x[1] + ", Opis: "
                  + x[2] + ", Data: " + t.strftime('%m/%d/%Y'))
        cursor.close()
        input()
