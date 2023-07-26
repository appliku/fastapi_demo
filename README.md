# Demo FastAPI application

Deploy this project on Appliku.

Add a Postgres Database to your project through dashboard.

## Test application

### Send a message
Run this curl command to send a message:

```shell
curl --request POST \
  --url https://fastmsg.applikuapp.com/messages/ \
  --header 'Content-Type: application/json' \
  --data '{
	"name" : "john Snow",
	"email": "123@example.com",
	"message": "hello"
}'
```

### Check messages

Connect to the databas using credentials from Appliku dashboard.

```shell 
psql postgresql://<username>:<password>@<host>:<port>/<database>
```


```
psql (15.3)
Type "help" for help.

vvcouwzwiumuhrgr=# \dt
              List of relations
 Schema |   Name   | Type  |      Owner
--------+----------+-------+------------------
 public | messages | table | cfrwqblgcumroizg
(1 row)

vvcouwzwiumuhrgr=# select * from messages;
 id |   name    |      email      | message
----+-----------+-----------------+---------
  1 | john Snow | 123@example.com | hello
(1 rows)
```
