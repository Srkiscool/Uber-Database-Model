
#add_comment
def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 

import psycopg2 as pg2
con = pg2.connect(database = 'venmo', user = 'isdb')
con.autocommit = True
cur = con.cursor()

tmpl = """
        INSERT INTO Interaction(to_id, from_id,tdate,transaction_trans_id)
        VALUES ('@Rhiane-Brooks','@m_cruzy',current_timestamp,4);

        INSERT INTO Comment(interact_id, liked, message)
        VALUES ((SELECT MAX(interact_id) FROM Interaction),FALSE,'What is up yo')

    """
cur.execute(tmpl)



heading("Adds the comment 'What is up yo' to @mcruzy's transactions from @Rhiane-Brooks")




# Below code is from our collective half functioning py file if you were curious

# #-----------------------------------------------------------
# # add_comment
# #-----------------------------------------------------------
# def add_comment_menu():
#     view_all_friends_transactions_menu()

#     trans_id = input("Enter Post Id you want to comment on:")
#     comment = input("What do you want to comment?")
#     add_comment(trans_id,comment)


# def add_comment(trans_id, comment):
#     tmpl = '''
#         INSERT INTO Interaction(to_id, from_id,tdate,transaction_trans_id)
#         VALUES (
#                 (SELECT t.from_username
#                   FROM Transaction as t
#                  WHERE t.trans_id = ILIKE %s), %s,GETDATE(), %s)

#         INSERT INTO Comment(interact_id, liked, message)
#         VALUES ((SELECT MAX(interact_id) FROM Interaction),FALSE,%s) #if s doesnt work for int try d
#     '''
#     cmd = cur.mogrify(tmpl, ('%'+trans_id+'%', '%'+my_username+'%', '%'+trans_id+'%', '%'+comment+'%'))
#     print_cmd(cmd)
#     cur.execute(cmd)