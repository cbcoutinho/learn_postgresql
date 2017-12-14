# Learn PostgreSQL using 'The Complete SQL Bootcamp'

This is a repository that contains work related to the sql course I'm
taking to learn postgresql.

These scripts all assume that 'dvdrentals' database has been restored
to a locally running postgresql server. The dvdrentals database is
accessible via the course link. To create the database locally from a
fresh dvdrental.tar file, first create a fresh database, then restore it
using the following command:

```bash
$ createdb dvdrentals
$ pg_restore --clean --dbname=dvdrentals dvdrental.tar
```

To restore the exercises database, use the following commands.
 NOTE: If the database is already created, it errors out on the
 (--create/-C) flag.

```bash
$ createdb exercises
$ pg_restore --clean --dbname=exercises --exit-on-error exercises.tar
```
