DROP TABLE "Meta_Columns";
DROP TABLE "Users";

CREATE TABLE "Meta_Columns" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"category"	TEXT NOT NULL,
	"sub-cat"	TEXT,
	"name"	TEXT NOT NULL,
	"desc"	TEXT,
	"notes"	TEXT,
	"created_by"	TEXT NOT NULL DEFAULT 'consultant_app',
	"created_date"	TEXT NOT NULL DEFAULT 'datetime(''now'', ''localtime'')',
	"updated_by"	TEXT,
	"updated_date"	TEXT
)

CREATE TABLE "Users" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"role"	TEXT NOT NULL,
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"acct_type"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"phone_type"	TEXT,
	"phone_num"	TEXT,
	"notes"	TEXT,
	"created_by"	TEXT NOT NULL DEFAULT 'consultant_app',
	"created_date"	TEXT NOT NULL DEFAULT 'datetime("now", "localtime")',
	"updated_by"	TEXT,
	"updated_date"	TEXT,
	"last_login"	TEXT,
	"lockout"	NUMERIC NOT NULL DEFAULT 0
)

