-- DROP DATABASE IF EXISTS venmo;
-- CREATE DATABASE venmo;

\c venmo
-- \i initialize.sql


\echo Venmo Account Information

	SELECT *
	  FROM Venmo_Acc;

\echo Transactions

	SELECT *
	  FROM Transaction;

\echo External Applications Linked to Venmo

	SELECT *
	  FROM External_App;

\echo 'Paid Status of Transaction'

	SELECT *
	  FROM Venmo_Accepted;

\echo 'Social Interactions for Each Transaction'

	SELECT *
	  FROM Interaction;

\echo Social Interactions - Comments

	SELECT *
	  FROM Comment;

\echo Social Interactions - Likes

	SELECT *
	  FROM Likes;

\echo Venmo Friendships

	SELECT *
	  FROM Venmo_Friend;

\echo Bank Account Information

	SELECT *
	  FROM Bank_Acc;

\echo Card Information

	SELECT *
	  FROM Card;

\echo Facebook Usernames

	SELECT *
	  FROM Facebook;

\echo Facebook Friendships

	SELECT *
	  FROM Fb_Friends_With;

\echo 'Facebook Friends with Venmo'

	SELECT *
	  FROM Fb_Friend;

\echo 







