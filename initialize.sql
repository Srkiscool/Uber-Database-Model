-- Setup the database for Venmo.

--Run with command psql -d postgres -U isdb -f initialize.sql

\c postgres
DROP DATABASE IF EXISTS venmo;

CREATE database venmo;
\c venmo

\i create.SQL

\copy Venmo_Acc(username, email, fname, lname, balance) FROM 'Venmo_Acc.csv'	csv header

\copy Bank_Acc(acc_num, name, balance, transfer_date, venmo_acc_username) FROM 'Bank_Acc.csv'	csv header

\copy Card(card_num, sec_code, cardholder, exp_date, provider, venmo_acc_username) 	FROM 'Card.csv'		csv header

\copy Transaction(amount, from_username, to_username, trans_type, is_private, trans_date) FROM 'Transaction.csv'	csv header

\copy Venmo_Accepted(trans_id, from_id, paid) FROM 'Venmo_Accepted.csv'	csv header

\copy External_App(trans_id) FROM 'External_App.csv'	csv header

\copy Interaction(to_id, from_id, tdate, transaction_trans_id) FROM 'Interaction.csv'	csv header

\copy Comment(interact_id, liked, message) FROM 'Comment.csv'	csv header

\copy Likes(interact_id) FROM 'Likes.csv'	csv header

\copy Venmo_Friend(username, friend_username) FROM 'Venmo_Friend.csv'	csv header

\copy Facebook(f_username, venmo_acc_username) FROM 'Facebook.csv'	csv header

\copy Fb_Friend(friend_username, has_venmo) FROM 'Fb_Friend.csv'	csv header

\copy Fb_Friends_With(f_username, friend_username) FROM 'Fb_Friends_With.csv'	csv header












