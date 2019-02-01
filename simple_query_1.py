
#List_friends
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 

import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()
tmpl = '''
        SELECT vf.friend_username
          FROM Venmo_Friend as vf
          JOIN Venmo_Acc as va ON va.username = vf.username
         WHERE (va.username = '@Rhiane-Brooks');


    '''
heading("Prints every friend of @Rhiane-Brooks")
cur.execute(tmpl)
rows = cur.fetchall()
for row in rows:
    print(row)




