DROP TABLE knowdedge_info;
CREATE TABLE knowdedge_info (id int NOT NULL, createtime timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, systemid int NOT NULL, issue text NOT NULL, causes text, solution text, ps text, status int NOT NULL, annex varchar(100), PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
