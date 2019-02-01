
#transfer money
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 

import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()
tmpl = """
        CREATE VIEW venmo_balance AS
        SELECT balance
          FROM Venmo_Acc
         WHERE (username = '@Rhiane-Brooks');

        UPDATE Bank_Acc
           SET balance = balance + (SELECT balance FROM venmo_balance)
         WHERE (venmo_acc_username = '@Rhiane-Brooks');

         UPDATE Venmo_Acc
            SET balance = 0
          WHERE (username = '@Rhiane-Brooks');
    """
cur.execute(tmpl)


heading("Transfers money over to '@Rhiane-Brooks' bank account balance")



# Below code is from our collective half functioning py file if you were curious

# #-----------------------------------------------------------------
# # transfer money
# #-----------------------------------------------------------------

# def transfer_money_menu():
#     heading("transferring your Venmo balance to bank account")


# def transfer_money():
#     tmpl = '''
#         CREATE VIEW venmo_balance AS
#         SELECT balance
#           FROM Venmo_Acc
#          WHERE (username ILIKE %s);

#         UPDATE Bank_Acc
#            SET balance = balance + venmo_balance
#          WHERE (venmo_acc_username ILIKE %s);

#          UPDATE Venmo_Acc
#             SET balance = 0
#           WHERE (username ILIKE %s);

#     '''
#     cmd = cur.mogrify(tmpl, ('%'+my_username+'%', '%'+my_username+'%', '%'+my_username+'%'))
#     print_cmd(cmd)
#     cur.execute(cmd)