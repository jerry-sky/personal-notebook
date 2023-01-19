---
lang: 'en-GB'
title: 'SQL Notes'
author: 'Jerry Sky'
description: 'Notes on SQL-related stuff.'
keywords: 'notes, SQL, query, database'
---



## Resources

- [`GROUP_CONCAT` and `DISTINCT`](https://stackoverflow.com/questions/3083499/mysql-distinct-on-a-group-concat)
- [Replacing `NULL` with a different value](https://database.guide/4-ways-to-replace-null-with-a-different-value-in-mysql/)
- [Pivoting in MySQL](http://mysql.rjweb.org/doc.php/pivot)
- [Performance tuning — Query Caching](https://logicalread.com/2015/09/28/mysql-with-query-caching-mc13/#.Xh9i-nWYXmF)
- [TypeORM — Databases with TypeScript](https://www.infoq.com/articles/typescript-mysql/)

---



## Show columns from a `SELECT` query

```sql
-- create a temporary table
CREATE TEMPORARY TABLE exportTable AS (your_query);
-- show the columns
SHOW COLUMNS FROM exportTable;
```

[Source](https://stackoverflow.com/a/38816005/4249875)

---



## `TRUNCATE` all tables in a database

```sql
SET FOREIGN_KEY_CHECKS = 0;

truncate table "yourTableName";

SET FOREIGN_KEY_CHECKS = 1;
```

[Source](https://stackoverflow.com/a/45597248/4249875)

---



## Big data

A data set of 9 million tuples is nothing for a relational database.
For maintaining sufficient performance as always use indexes
and all will be well.

[Source](https://connor-mcdonald.com/2021/11/13/when-does-a-table-become-too-big)
