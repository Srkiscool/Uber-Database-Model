-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2018-12-08 07:01:19.33

-- tables
-- Table: Bank_Acc
CREATE TABLE Bank_Acc (
    acc_num varchar  NOT NULL,
    name varchar  NOT NULL,
    balance money  NOT NULL,
    transfer_date timestamp  NOT NULL,
    venmo_acc_username varchar  NOT NULL,
    CONSTRAINT Bank_Acc_pk PRIMARY KEY (acc_num)
);

-- Table: Card
CREATE TABLE Card (
    card_num varchar  NOT NULL,
    sec_code int  NOT NULL,
    cardholder varchar  NOT NULL,
    exp_date date  NOT NULL,
    provider varchar  NOT NULL,
    venmo_acc_username varchar  NOT NULL,
    CONSTRAINT Card_pk PRIMARY KEY (card_num)
);

-- Table: Comment
CREATE TABLE Comment (
    interact_id int  NOT NULL,
    liked boolean  NOT NULL,
    message varchar  NOT NULL,
    CONSTRAINT Comment_pk PRIMARY KEY (interact_id)
);

-- Table: External_App
CREATE TABLE External_App (
    trans_id int  NOT NULL,
    CONSTRAINT External_App_pk PRIMARY KEY (trans_id)
);

-- Table: Facebook
CREATE TABLE Facebook (
    f_username varchar  NOT NULL,
    venmo_acc_username varchar  NOT NULL,
    CONSTRAINT Facebook_pk PRIMARY KEY (f_username)
);

-- Table: Fb_Friend
CREATE TABLE Fb_Friend (
    friend_username varchar  NOT NULL,
    has_venmo boolean  NOT NULL,
    CONSTRAINT Fb_Friend_pk PRIMARY KEY (friend_username)
);

-- Table: Fb_Friends_With
CREATE TABLE Fb_Friends_With (
    f_username varchar  NOT NULL,
    friend_username varchar  NOT NULL,
    CONSTRAINT Fb_Friends_With_pk PRIMARY KEY (f_username,friend_username)
);

-- Table: Interaction
CREATE TABLE Interaction (
    interact_id serial  NOT NULL,
    to_id varchar  NOT NULL,
    from_id varchar  NOT NULL,
    tdate timestamp  NOT NULL,
    transaction_trans_id int  NOT NULL,
    CONSTRAINT Interaction_pk PRIMARY KEY (interact_id)
);

-- Table: Likes
CREATE TABLE Likes (
    interact_id int  NOT NULL,
    CONSTRAINT Likes_pk PRIMARY KEY (interact_id)
);

-- Table: Transaction
CREATE TABLE Transaction (
    trans_id serial  NOT NULL,
    amount money  NOT NULL,
    from_username varchar  NOT NULL,
    to_username varchar  NOT NULL,
    trans_type int  NOT NULL,
    is_private boolean  NOT NULL,
    trans_date timestamp  NOT NULL,
    CONSTRAINT Transaction_pk PRIMARY KEY (trans_id)
);

-- Table: Venmo_Acc
CREATE TABLE Venmo_Acc (
    username varchar  NOT NULL,
    email varchar  NOT NULL,
    fname varchar  NOT NULL,
    lname varchar  NOT NULL,
    balance money  NOT NULL,
    CONSTRAINT Venmo_Acc_pk PRIMARY KEY (username)
);

-- Table: Venmo_Accepted
CREATE TABLE Venmo_Accepted (
    trans_id int  NOT NULL,
    from_id varchar  NOT NULL,
    paid boolean  NOT NULL,
    CONSTRAINT Venmo_Accepted_pk PRIMARY KEY (trans_id)
);

-- Table: Venmo_Friend
CREATE TABLE Venmo_Friend (
    username varchar  NOT NULL,
    friend_username varchar  NOT NULL,
    CONSTRAINT Venmo_Friend_pk PRIMARY KEY (username,friend_username)
);

-- foreign keys
-- Reference: Card_Venmo_Acc (table: Card)
ALTER TABLE Card ADD CONSTRAINT Card_Venmo_Acc
    FOREIGN KEY (venmo_acc_username)
    REFERENCES Venmo_Acc (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comment_Interaction (table: Comment)
ALTER TABLE Comment ADD CONSTRAINT Comment_Interaction
    FOREIGN KEY (interact_id)
    REFERENCES Interaction (interact_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: External_App_Transaction (table: External_App)
ALTER TABLE External_App ADD CONSTRAINT External_App_Transaction
    FOREIGN KEY (trans_id)
    REFERENCES Transaction (trans_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Facebook_Fb_Friends_With (table: Fb_Friends_With)
ALTER TABLE Fb_Friends_With ADD CONSTRAINT Facebook_Fb_Friends_With
    FOREIGN KEY (f_username)
    REFERENCES Facebook (f_username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Facebook_Venmo_Acc (table: Facebook)
ALTER TABLE Facebook ADD CONSTRAINT Facebook_Venmo_Acc
    FOREIGN KEY (venmo_acc_username)
    REFERENCES Venmo_Acc (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Fb_Friends_With_Facebook_Friend (table: Fb_Friends_With)
ALTER TABLE Fb_Friends_With ADD CONSTRAINT Fb_Friends_With_Facebook_Friend
    FOREIGN KEY (friend_username)
    REFERENCES Fb_Friend (friend_username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Interaction_Transaction (table: Interaction)
ALTER TABLE Interaction ADD CONSTRAINT Interaction_Transaction
    FOREIGN KEY (transaction_trans_id)
    REFERENCES Transaction (trans_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Likes_Interaction (table: Likes)
ALTER TABLE Likes ADD CONSTRAINT Likes_Interaction
    FOREIGN KEY (interact_id)
    REFERENCES Interaction (interact_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Transaction_Venmo_Acc (table: Transaction)
ALTER TABLE Transaction ADD CONSTRAINT Transaction_Venmo_Acc
    FOREIGN KEY (from_username)
    REFERENCES Venmo_Acc (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Transaction_Venmo_Accepted (table: Venmo_Accepted)
ALTER TABLE Venmo_Accepted ADD CONSTRAINT Transaction_Venmo_Accepted
    FOREIGN KEY (trans_id)
    REFERENCES Transaction (trans_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Venmo_Friend_Venmo_Acc (table: Venmo_Friend)
ALTER TABLE Venmo_Friend ADD CONSTRAINT Venmo_Friend_Venmo_Acc
    FOREIGN KEY (username)
    REFERENCES Venmo_Acc (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: bank_account_Venmo_Acc (table: Bank_Acc)
ALTER TABLE Bank_Acc ADD CONSTRAINT bank_account_Venmo_Acc
    FOREIGN KEY (venmo_acc_username)
    REFERENCES Venmo_Acc (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

