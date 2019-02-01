
#show_all_venmo_users
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 

import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()

tmpl = """
        SELECT vc.username
        FROM Venmo_Acc as vc
    """
heading("Showing all venmo users")
cur.execute(tmpl)
rows = cur.fetchall()
for row in rows:
    print(row)




# Below code is from our collective half functioning py file if you were curious

# #-----------------------------------------------------------------
# # show_all_venmo_users
# #-----------------------------------------------------------------

# def show_all_venmo_users_menu():
#     heading("All Users:")
#     show_all_venmo_users()

# def show_all_venmo_users():
#     tmpl = '''
#         SELECT vc.username
#         FROM Venmo_Acc as vc
#          -- ILIKE is a case insensitive LIKE
#     '''
#     cmd = cur.mogrify(tmpl)
#     print_cmd(cmd)
#     cur.execute(cmd)
#     rows = cur.fetchall()
#     print_rows(rows)
#     print()