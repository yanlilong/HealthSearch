create table Query(Query_ID INTEGER NOT NULL,Age INTEGER, Sex CHARACTER(1) NOT NULL,Symptom VARCHAR(500) NOT NULL,
   Disease VARCHAR(200) NOT NULL,
   QueryLastTime TIME NOT NULL,
   QueryFrequency INTEGER NOT NULL,
   PRIMARY KEY(Query_ID )
);
create table ResultURL(ResultURL_ID INTEGER NOT NULL,
ShortenURL VARCHAR(20) NOT NULL,
ResultURL VARCHAR(65535) NOT NULL,
PublishedTime TIME NOT NULL,
Title VARCHAR(200) NOT NULL,
Frequency INTEGER NOT NULL,
Clicks INTEGER NOT NULL,
LastUpdateTime TIME NOT NULL,
Resource_ID INTEGER NOT NULL,
PRIMARY KEY(ResultURL_ID)
);
create table Query_ResultURL(Query_ID INTEGER NOT NULL,
ResultURL_ID INTEGER NOT NULL,
PRIMARY KEY(Query_ID,ResultURL_ID)
);
create table DataResource(Resource_ID INTEGER NOT NULL,
ResourceName VARCHAR(100) NOT NULL,
URL VARCHAR(65535),
Frequency INTEGER,
PRIMARY KEY(Resource_ID)
);
create table ResourceURL_DataResource(ResourceURL_ID INTEGER NOT NULL,
Resource_ID INTEGER NOT NULL,
PRIMARY KEY(ResourceURL_ID,Resource_ID)
);

