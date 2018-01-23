# README.md

## rds-backup.py
RDS backup (rds_backup.py) is a __Python 3.6__ AWS lambda function to take rds snapshot and set tags with retention and deletion info.

## Setup RDS backup AWS lambda function.

#### Add new tags on RDS instances
It is necessary to add at least one new tag to each RDS to backup, the only required tag is "backup", the tags "retentionsdays" and "deletesnapshot" are not necessary.
```
backups: True
deletesnapshot: False
retentiondays: 123
```
The __backup__ and, __deletesnapshot__ tags can take the values "__True__" or "__False__", as indicated here (__literally__)
The __retentiondays__ tag must have an integer value greater than one. The objective of this tag is to indicate the number of days the snapshot should be retained.

#### Create a rds-backup role
You must create a role with sufficient privileges on RDS to ensure the lambda function execution. 
Be cautious and do not assign permissions that are not necessary.

#### Create lambda function