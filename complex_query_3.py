
#add_friend
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 

import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()

tmpl = """
        INSERT INTO Venmo_Friend(username, friend_username)
        VALUES ('@Rhiane-Brooks', '@Prof-Queen'); 

        INSERT INTO Venmo_Friend(username, friend_username)
        VALUES ('@Prof-Queen', '@Rhiane-Brooks'); 
    """
cur.execute(tmpl)

heading("Creates a new friendship between  '@Prof_Queen' and '@Rhiane-Brooks'")



# Below code is from our collective half functioning py file if you were curious

# #-----------------------------------------------------------------
# # add_friend
# #-----------------------------------------------------------------
# def add_friend_menu():
#     print("add_friend")

#     show_all_venmo_users_main()

#     uid_1 = input("Enter Friend username you would like to add to your Friends list")
#     add_friend(uid_1)

# def add_friend(uid_1):
#     tmpl = '''
#         INSERT INTO Venmo_Friend(username, friend_username)
#         VALUES (%s,%s);

#         INSERT INTO FRIENDS (username, friendusername)
#         VALUES (%s,%s);       
#     '''
#     cmd = cur.mogrify(tmpl, ('%'+uid_1+'%', '%'+my_username+'%','%'+trans_id+'%', '%'+my_username+'%'))
#     print_cmd(cmd)
#     cur.execute(cmd)