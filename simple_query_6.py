
#Display Balance 
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 

import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()

tmpl = """
	SELECT username, fname, lname, balance
	  FROM Venmo_Acc
	 WHERE username = '@Rhiane-Brooks'



    """
heading("Prints '@Rhiane-Brooks' Venmo balance")
cur.execute(tmpl)
rows = cur.fetchall()
for row in rows:
    print(row)




# Below code is from our collective half functioning py file if you were curious


# #-----------------------------------------------------------------
# # list All Friends transactions:
# #-----------------------------------------------------------------
# def view_all_friends_transactions_menu():
#     heading("Here are all your friends and your transactions")
#     view_all_friends_transactions();

# def view_all_friends_transactions():
#     tmpl = '''
#         SELECT t.trans_id, t.from_username, t.to_username, t.trans_type, t.trans_date
#           FROM Venmo_Acc as va
#           JOIN Transaction as t ON t.from_user_name = va.username
#           JOIN Transaction as t ON t.to_user_name = va.username
#           JOIN Venmo_Friend as vf ON vf.friend_username = va.username
#          WHERE (vf.username ILIKE %s)
#          -- ILIKE is a case insensitive LIKE
#     '''
#     cmd = cur.mogrify(tmpl, ('%'+my_username+'%'))
#     print_cmd(cmd)
#     cur.execute(cmd)
#     rows = cur.fetchall()
#     print_rows(rows)
#     print()

        # CREATE TABLE t as
        # SELECT t.trans_id, t.from_username, t.to_username, t.trans_type, t.trans_date
        #   FROM Venmo_Acc as va
        #   JOIN Transaction as t ON t.to_username = va.username
        #   JOIN Venmo_Friend as vf ON vf.friend_username = va.username
        #  WHERE (vf.username = '@Rhiane-Brooks');


        # CREATE TABLE f as
        # SELECT t.trans_id, t.from_username, t.to_username, t.trans_type, t.trans_date
        #   FROM Venmo_Acc as va
        #   JOIN Transaction as t ON t.from_username = va.username
        #   JOIN Venmo_Friend as vf ON vf.friend_username = va.username
        #  WHERE (vf.username = '@Rhiane-Brooks');

        # SELECT f.trans_id, f.from_username, f.to_username, f.trans_type, f.trans_date
        #   FROM t
        #   FULL OUTER JOIN f ON f.trans_id = t.trans_id 

