# MySQL Database Management

As a platform, MySQL is designed to reside on a single server and be accessed from several remote locations.
In our development cycle, we now have a single main server which all developers should be using.
Therefore, within this directory is the backup script to repopulate a MySQL database at any given point in time.

The file "echelon_db_backup.sql" can be used to two ends:
1. Restore the main database (or any SQL Server) to a given point in time if information were lost or corrupted.
2. Allow for local dev SQL servers to import data from this file at any time for testing purposes.