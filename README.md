# luigisample

Default Port: 8082
-  luigid --port 8082
- http://localhost:8082/

## Docs
- https://lovethepenguin.com/python-create-an-etl-with-luigi-pandas-and-sqlalchemy-d3cdc9292bc7

##  Run

```
$ sudo pip3 install pandas
$ sudo pip3 install sqlalchemy
$ sudo pip3 install luigi
```


```
sqlite3 db1
create table names (id varchar(10) primary key, first_name text, last_name text);
insert into names values('2','john','doe');
insert into names values('3','jenny','doe');

```