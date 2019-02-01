
#view_personal_transactions
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 

import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()

tmpl = """
        SELECT t.from_username, t.to_username, t.amount, t.trans_type, t.trans_date
          FROM Venmo_Acc as va
          JOIN Transaction as t ON va.username = t.from_username
         WHERE (va.username = '@Rhiane-Brooks')


    """

heading("Prints @Rhiane-Brooks personal transactions")
cur.execute(tmpl)
rows = cur.fetchall()
for row in rows:
    print(row)




# Below code is from our collective half functioning py file if you were curious

# #------------------------------------------------------------
# # view_personal_transactions
# #------------------------------------------------------------

# def view_personal_transactions_menu():
#     heading("Here are your Personal Transaction")
#     view_personal_transactions();

# def view_personal_transactions():
#     tmpl = '''
#         SELECT t.from_username, t.to_username, t.amount, t.trans_type, t.trans_date
#           FROM Venmo_Acc as va
#           JOIN Transaction as t ON va.username = t.venmo_acc_userusername
#          WHERE (va.username ILIKE %s)
#          -- ILIKE is a case insensitive LIKE
#     '''
#     cmd = cur.mogrify(tmpl, ('%'+my_username+'%'))
#     print_cmd(cmd)
#     cur.execute(cmd)
#     rows = cur.fetchall()
#     print_rows(rows)
#     print()
