
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
		CREATE VIEW friends_of as
		SELECT vf.friend_username
		  FROM Venmo_Friend as vf
		 WHERE vf.username = '@Rhiane-Brooks';


		SELECT t.from_username, t.to_username, t.trans_type, t.trans_date
		  FROM Transaction as t
		 WHERE t.from_username IN (SELECT * FROM friends_of) OR t.to_username IN (SELECT * FROM friends_of) AND t.is_private = FALSE;



    """
heading("Prints @Rhiane-Brooks friends' public transactions")
cur.execute(tmpl)
rows = cur.fetchall()
for row in rows:
    print(row)




# Below code is from our collective half functioning py file if you were curious


# #------------------------------------------------------------
# # view_friends_transactions
# #------------------------------------------------------------

# def view_friends_transactions_menu():
#     heading("Which Friend Would You Like to See?")
#     heading("You will not be able to see amount")
#     list_friends()
#     friend_uname = input("Enter Username:")
#     view_friends_transactions(friend_uname)

# def view_friends_transactions(friend_uname):
#     tmpl = '''
#         SELECT vf.friend_username, t.from_username, t.to_username, t.trans_type, t.trans_date
#           FROM Venmo_Friend as vf
#           JOIN Venmo_Acc as va ON va.username = vf.friend_username
#           JOIN Transaction as t ON t.venmo_acc_username = va.username
#          WHERE (va.username ILIKE %s) AND t.is_private = FALSE
#          -- ILIKE is a case insensitive LIKE
#     '''
#     cmd = cur.mogrify(tmpl, ('%'+friend_uname+'%'))
#     print_cmd(cmd)
#     cur.execute(cmd)
#     rows = cur.fetchall()
#     print_rows(rows)
#     print()