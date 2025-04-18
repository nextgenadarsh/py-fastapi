Sqlite
---

# Database Setup

- You can execute commands to sqllite in the console.
- Run `sqlite3` to enter sqlite command mode
- Run `.open <file_name>` to create persistent database.
- Run `create table ...` query to create schema.
- Run `.schema` to see the list of schemas created
- Run `select ...` query to see the records
- You can Run `.mode <mode_name>` to see the structure of the output. Modes are:
    - column
    - markdown
    - box
    - table


# Database Scripts

```sql
CREATE TABLE "users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"email"	TEXT UNIQUE,
	"user_name"	TEXT UNIQUE,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"hashed_password"	TEXT,
	"is_active"	INTEGER,
	"roles"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "todos" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT UNIQUE,
	"description"	TEXT,
	"priority"	INTEGER,
	"complete"	INTEGER,
	"owner_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("owner_id") REFERENCES users("id") 
);
```
