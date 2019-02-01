#-----------------------------------------------------------------
# Working with psycopg2
#-----------------------------------------------------------------

import psycopg2
import sys
import datetime

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')    

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    for row in rows:
        print(row)

#------------------------------------------------------------
# show_menu
#------------------------------------------------------------

def show_menu(my_username):
    menu = '''

--------------------------------------------------
1. List users 
2. Show user 
3. New user 
---
4. Show friends 
5. Add friend 
---
6. Show messages
7. Post message


1:charge_friend, 2:view_friends_transactions, 3:view_personal_transactions,
4:view_personal_avg_spending, 5:view_uncompleted_requests, 6:view_num_late_payments,
7:add_comment, 8:add_friend, 9:transfer_money, 10: list_friends



1. Charge Friend  charge_friend(2)
2. View  A Friend's transactions  view_friends_transactions(3) -- REQUIRES USER INPUTTED NAME
3. View Personal Transactions (4)
4. View Personal Average Spending (6)
5. View Uncompleted Requests (5)
6. View Net profit of transactions with a friend -- REQUIRES USER INPUTTED DATE
7. Add Comment on transaction(8) -- Multi stage (show list of transactions and )
8. Add friend to Venmo(9) -- show list of fb friends who have venmo, ask to enter first and last name.
9. Transfer Money from Venmo to Bank Account
10. Pay External App 
11.List friends



Choose (1-7, 0 to quit): '''

    try:
        choice = int(input( menu ))
    except ValueError:
        print("\n\n* Invalid choice. Choose again.")
        show_menu()
    else:
        if choice == 0:
            print('Done.')
            cur.close()
            conn.close()
        elif choice in range(1,1+11):
            print()
            actions[choice]()
            show_menu()
        else:
            print("\n\n* Invalid choice (%s). Choose again." % choice)
            show_menu()
    finally:
        if cur != None:
            cur.close() 
        if conn != None:
            conn.close() 


#-----------------------------------------------------------
# charge_friend
#-----------------------------------------------------------
def charge_friend_menu():
    heading("Which Friend Would You Like to charge?")
    list_friends_menu()

    friend_uname = input("Enter Username:")
    charge_amount = input("Enter Charge Amount:")
    private = input("Is transaction private? TRUE or FALSE:")
    charge_friend(friend_uname,charge_amount, private)


def charge_friend(friend_uname,charge_amount,private):
    tmpl = '''
        INSERT INTO Transaction(amount,from_username,to_username,trans_type,
                                is_private,trans_date,venmo_acc_username)
        VALUES (%s,%s,%s,%s::integer,%s,GETDATE(),%s) #if s doesnt work for int try d

        INSERT INTO Venmo_Accepted(trans_id, from_id, paid)
        VALUES((SELECT MAX(trans_id) FROM Transaction), %s, FALSE)
    '''
    cmd = cur.mogrify(tmpl, ('%'+charge_amount+'%','%'+my_username+'%','%'+friend_uname+'%',1,'%'+private+'%',
                             '%'+my_username+'%','%'+my_username+'%'))
    print_cmd(cmd)
    cur.execute(cmd)

            

#------------------------------------------------------------
# list_friends
#------------------------------------------------------------

def list_friends_menu():
    heading('Your Friends:')
    user_n = input("What is your name")
    list_friends(user_n)

def list_friends(user_n):
    print(my_username)
    tmpl = '''
        SELECT vf.friend_username
          FROM Venmo_Friend as vf
          JOIN Venmo_Acc as va ON va.username = vf.username
         WHERE (va.username LIKE %s);
         -- ILIKE is a case insensitive LIKE
    '''
    cmd = cur.mogrify(tmpl, ('%'+user_n+'%'))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()

#------------------------------------------------------------
# view_friends_transactions
#------------------------------------------------------------

def view_friends_transactions_menu():
    heading("Which Friend Would You Like to See?")
    heading("You will not be able to see amount")
    list_friends()
    friend_uname = input("Enter Username:")
    view_friends_transactions(friend_uname)

def view_friends_transactions(friend_uname):
    tmpl = '''
        SELECT vf.friend_username, t.from_username, t.to_username, t.trans_type, t.trans_date
          FROM Venmo_Friend as vf
          JOIN Venmo_Acc as va ON va.username = vf.friend_username
          JOIN Transaction as t ON t.venmo_acc_username = va.username
         WHERE (va.username ILIKE %s) AND t.is_private = FALSE
         -- ILIKE is a case insensitive LIKE
    '''
    cmd = cur.mogrify(tmpl, ('%'+friend_uname+'%'))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
#------------------------------------------------------------
# view_personal_transactions
#------------------------------------------------------------

def view_personal_transactions_menu():
    heading("Here are your Personal Transaction")
    view_personal_transactions();

def view_personal_transactions():
    tmpl = '''
        SELECT t.from_username, t.to_username, t.amount, t.trans_type, t.trans_date
          FROM Venmo_Acc as va
          JOIN Transaction as t ON va.username = t.venmo_acc_userusername
         WHERE (va.username ILIKE %s)
         -- ILIKE is a case insensitive LIKE
    '''
    cmd = cur.mogrify(tmpl, ('%'+my_username+'%'))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()

#------------------------------------------------------------
# view_personal_avg_spending
#------------------------------------------------------------

def view_personal_avg_spending_menu():
    heading("Here are your Personal Averages Per Day on Venmo")
    view_personal_avg_spending();

def view_personal_avg_spending():
    tmpl = '''
        SELECT t.trans_date, AVERAGE(t.amount)
          FROM Venmo_Acc as va
          JOIN Transaction as t ON va.username = t.venmo_acc_userusername
         GROUP BY t.trans_date 
         WHERE (va.username ILIKE %s) AND t.trans_type = -1
         -- ILIKE is a case insensitive LIKE
    '''
    cmd = cur.mogrify(tmpl, ('%'+my_username+'%'))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
#------------------------------------------------------------
# view_uncompleted_requests
#------------------------------------------------------------

def view_uncompleted_requests_menu():
    heading("Here are your Uncompleted Requests")
    view_personal_transactions();

def view_uncompleted_requests():
    tmpl = '''
        SELECT t.from_username, t.to_username, t.amount, t.trans_type, t.trans_date
          FROM Transaction as t
          JOIN Venmo_Accepted as vaa ON vaa.trans_id = t.trans_id
         WHERE ((t.from_username ILIKE %s) OR (t.to_username ILIKE %s)) AND vaa.paid = FALSE
         -- ILIKE is a case insensitive LIKE
    '''
    cmd = cur.mogrify(tmpl, ('%'+my_username+'%', '%'+my_username+'%'))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()

#------------------------------------------------------------
# view_net_profit_menu
#------------------------------------------------------------

def view_net_profit_menu():
    heading("Here is your net Profit")
    view_net_profit();

def view_net_profit():
    tmpl = '''
        CREATE VIEW loss as
        SELECT SUM(t.amount) as sum
          FROM Transaction as t
         WHERE (t.to_username LIKE %s AND t.trans_type = 1 ) OR 
                (t.from_username LIKE %s AND t.trans_type = -1)

        CREATE VIEW gain as
        SELECT SUM(t.amount) as sum
          FROM Transaction as t
         WHERE (t.from_username LIKE %s AND t.trans_type = 1 ) OR 
                (t.to_username LIKE %s AND t.trans_type = -1 )

        CREATE VIEW net as 
        SELECT l.sum as loss, g.sum as gain, (g.sum - l.sum) as net
          FROM loss as l 
          JOIN gain as g ON g.from_username = l.from_username

    '''
    cmd = cur.mogrify(tmpl, ('%'+my_username+'%','%'+my_username+'%',
                            '%'+my_username+'%','%'+my_username+'%'))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()



#-----------------------------------------------------------------
# list All Friends transactions:
#-----------------------------------------------------------------
def view_all_friends_transactions_menu():
    heading("Here are all your friends and your transactions")
    view_all_friends_transactions();

def view_all_friends_transactions():
    tmpl = '''
        SELECT t.trans_id, t.from_username, t.to_username, t.trans_type, t.trans_date
          FROM Venmo_Acc as va
          JOIN Transaction as t ON t.from_user_name = va.username
          JOIN Transaction as t ON t.to_user_name = va.username
          JOIN Venmo_Friend as vf ON vf.friend_username = va.username
         WHERE (vf.username ILIKE %s)
         -- ILIKE is a case insensitive LIKE
    '''
    cmd = cur.mogrify(tmpl, ('%'+my_username+'%'))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()





#-----------------------------------------------------------
# add_comment
#-----------------------------------------------------------
def add_comment_menu():
    view_all_friends_transactions_menu()

    trans_id = input("Enter Post Id you want to comment on:")
    comment = input("What do you want to comment?")
    add_comment(trans_id,comment)


def add_comment(trans_id, comment):
    tmpl = '''
        INSERT INTO Interaction(to_id, from_id,tdate,transaction_trans_id)
        VALUES (
                (SELECT t.from_username
                  FROM Transaction as t
                 WHERE t.trans_id = ILIKE %s), %s,GETDATE(), %s)

        INSERT INTO Comment(interact_id, liked, message)
        VALUES ((SELECT MAX(interact_id) FROM Interaction),FALSE,%s) #if s doesnt work for int try d
    '''
    cmd = cur.mogrify(tmpl, ('%'+trans_id+'%', '%'+my_username+'%', '%'+trans_id+'%', '%'+comment+'%'))
    print_cmd(cmd)
    cur.execute(cmd)

#-----------------------------------------------------------------
# show_all_venmo_users
#-----------------------------------------------------------------

def show_all_venmo_users_menu():
    heading("All Users:")
    show_all_venmo_users()

def show_all_venmo_users():
    tmpl = '''
        SELECT vc.username
        FROM Venmo_Acc as vc
         -- ILIKE is a case insensitive LIKE
    '''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
#-----------------------------------------------------------------
# add_friend
#-----------------------------------------------------------------
def add_friend_menu():
    print("add_friend")

    show_all_venmo_users_main()

    uid_1 = input("Enter Friend username you would like to add to your Friends list")
    add_friend(uid_1)

def add_friend(uid_1):
    tmpl = '''
        INSERT INTO Venmo_Friend(username, friend_username)
        VALUES (%s,%s);

        INSERT INTO Venmo_friends (username, friend_username)
        VALUES (%s,%s);       
    '''
    cmd = cur.mogrify(tmpl, ('%'+uid_1+'%', '%'+my_username+'%','%'+trans_id+'%', '%'+my_username+'%'))
    print_cmd(cmd)
    cur.execute(cmd)

#-----------------------------------------------------------------
# transfer money
#-----------------------------------------------------------------

def transfer_money_menu():
    heading("transferring your Venmo balance to bank account")


def transfer_money():
    tmpl = '''
        CREATE VIEW venmo_balance AS
        SELECT balance
          FROM Venmo_Acc
         WHERE (username ILIKE %s);

        UPDATE Bank_Acc
           SET balance = balance + venmo_balance
         WHERE (venmo_acc_username ILIKE %s);

         UPDATE Venmo_Acc
            SET balance = 0
          WHERE (username ILIKE %s);

    '''
    cmd = cur.mogrify(tmpl, ('%'+my_username+'%', '%'+my_username+'%', '%'+my_username+'%'))
    print_cmd(cmd)
    cur.execute(cmd)


# #-----------------------------------------------------------------
# # show_external_companies
# #-----------------------------------------------------------------

# def show_external_companies_menu()
#     heading("All Companies:")
#     show_external_companies()

# def show_external_companies():
#     tmpl = '''
#         SELECT ea.company_id
#         FROM External_App as ea
#          -- ILIKE is a case insensitive LIKE
#     '''
#     cmd = cur.mogrify(tmpl)
#     print_cmd(cmd)
#     cur.execute(cmd)
#     rows = cur.fetchall()
#     print_rows(rows)
#     print()

# #-----------------------------------------------------------
# # pay_external_app
# #-----------------------------------------------------------
# def pay_external_app_menu():
#     heading("Here are a list of companies who you can pay:")
#     show_external_companies_menu()

#     company_name = input("Enter Comapny Name:")
#     amount = input("How much do you want to pay them?:")
#     private = input("Is transaction private? TRUE or FALSE:")
#     pay_external_app(company_name,amount, private)


# def pay_external_app(company_name,amount,private):
#     tmpl = '''
#         INSERT INTO Transaction(amount,from_username,to_username,trans_type,
#                                 is_private,trans_date)
#         VALUES (%s,%s,%s,%s::integer,%s,GETDATE(),%s) #if s doesnt work for int try d

#         INSERT INTO Venmo_Accepted(trans_id, from_id, paid)
#         VALUES((SELECT MAX(trans_id) FROM Transaction), %s, TRUE)

#         UPDATE Venmo_Acc as va
#            SET va.balance = va.balance + %s::integer

#     '''
#     cmd = cur.mogrify(tmpl, ('%'+amount+'%','%'+my_username+'%','%'+company_name+'%',-1,'%'+private+'%',
#                              '%'+my_username+'%', amount))
#     print_cmd(cmd)
#     cur.execute(cmd)


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# We leverage the fact that in Python functions are first class
# objects and build a dictionary of functions numerically indexed 

actions = { 1:charge_friend_menu, 2:view_friends_transactions_menu, 3:view_personal_transactions_menu,
            4:view_personal_avg_spending_menu, 5:view_uncompleted_requests_menu, 6:view_net_profit_menu,
            7:add_comment_menu, 8:add_friend_menu, 9:transfer_money_menu, 10:list_friends_menu}


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'socnet', 'isdb'
        # you may have to adjust the user 
        # python a4-socnet-sraja.py a4_socnet postgres
        if len(sys.argv) >= 2:
            db = sys.argv[1]
        if len(sys.argv) >= 3:
            user = sys.argv[2]
        # by assigning to conn and cur here they become
        # global variables.  Hence they are not passed
        # into the various SQL interface functions
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()

        global my_username
        my_username = input("Enter Your Venmo Username")
        show_menu(my_username)
    
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))


