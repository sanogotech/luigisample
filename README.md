# luigisample

Default Port: 8082
-  luigid --port 8082
- http://localhost:8082/

## Docs
- https://lovethepenguin.com/python-create-an-etl-with-luigi-pandas-and-sqlalchemy-d3cdc9292bc7

- https://www.datarevenue.com/en-blog/how-to-scale-your-machine-learning-pipeline

## Gist Docs
- https://gist.github.com/sanogotech/fcfeb2f39dd8ad582e83ce0e396eb015

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


```
sqlite3 db2
create table salaries (id varchar(10) primary key, salary integer);
insert into salaries values('1',10000);
insert into salaries values('2',13000);
insert into salaries values('3',23000);
```

```
$ luigid --port 8082
$ python etl.py
```