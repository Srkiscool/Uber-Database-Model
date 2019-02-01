
#view_uncompleted_requests_menu
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
          FROM Transaction as t
          JOIN Venmo_Accepted as vaa ON vaa.trans_id = t.trans_id
         WHERE ((t.from_username = '@Rhiane-Brooks') OR (t.to_username = '@Rhiane-Brooks')) AND vaa.paid = FALSE

    """
heading("Prints @Rhiane-Brooks' Uncompleted Venmo Requests")
cur.execute(tmpl)
rows = cur.fetchall()
for row in rows:
    print(row)



# Below code is from our collective half functioning py file if you were curious


# def view_uncompleted_requests_menu():
#     heading("Here are your Uncompleted Requests")
#     view_personal_transactions();

# def view_uncompleted_requests():
#     tmpl = '''
#         SELECT t.from_username, t.to_username, t.amount, t.trans_type, t.trans_date
#           FROM Transaction as t
#           JOIN Venmo_Accepted as vaa ON vaa.trans_id = t.trans_id
#          WHERE ((t.from_username ILIKE %s) OR (t.to_username ILIKE %s)) AND vaa.paid = FALSE
#          -- ILIKE is a case insensitive LIKE
#     '''
#     cmd = cur.mogrify(tmpl, ('%'+my_username+'%', '%'+my_username+'%'))
#     print_cmd(cmd)
#     cur.execute(cmd)
#     rows = cur.fetchall()
#     print_rows(rows)
#     print()