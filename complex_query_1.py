
#view_friends_transactions
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 

import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()
tmpl = """
		CREATE VIEW friendsOf as
		SELECT vf.friend_username
		  FROM Venmo_Friend as vf
		 WHERE vf.username = '@Rhiane-Brooks';


		SELECT t.from_username, t.to_username, t.trans_type, t.trans_date
		  FROM Transaction as t
		 WHERE t.from_username IN (SELECT * FROM friendsOf) OR t.to_username IN (SELECT * FROM friendsOf) AND t.is_private = FALSE;



    """
print("Prints @Rhiane-Brooks friends' public transactions")
cur.execute(tmpl)
rows = cur.fetchall()
for row in rows:
    print(row)



