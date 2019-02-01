
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') #view_personal_avg_spending


import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()

tmpl = """
        SELECT (AVG(t.amount::numeric))::money
          FROM Venmo_Acc as va
          JOIN Transaction as t ON va.username = t.from_username
         WHERE (va.username = '@Rhiane-Brooks') AND t.trans_type = -1


    """
heading("Prints @Rhiane-Brooks average spending on Venmo")
cur.execute(tmpl)
rows = cur.fetchall()
for row in rows:
    print(row)

# Below code is from our collective half functioning py file if you were curious

# #------------------------------------------------------------
# # view_personal_avg_spending
# #------------------------------------------------------------

# def view_personal_avg_spending_menu():
#     heading("Here are your Personal Averages Per Day on Venmo")
#     view_personal_avg_spending();

# def view_personal_avg_spending():
#     tmpl = '''
#         SELECT t.trans_date, AVERAGE(t.amount)
#           FROM Venmo_Acc as va
#           JOIN Transaction as t ON va.username = t.venmo_acc_userusername
#          GROUP BY t.trans_date 
#          WHERE (va.username ILIKE %s) AND t.trans_type = -1
#          -- ILIKE is a case insensitive LIKE
#     '''
#     cmd = cur.mogrify(tmpl, ('%'+my_username+'%'))
#     print_cmd(cmd)
#     cur.execute(cmd)
#     rows = cur.fetchall()
#     print_rows(rows)
#     print()