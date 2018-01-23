# README.md

## rds-backup.py
RDS backup (rds_backup.py) is a __Python 3.6__ AWS lambda function to take rds snapshot and set tags with retention and deletion info.

## Setup RDS backup AWS lambda function.

#### Create a rds-backup role
You must create a role with sufficient privileges on RDS to ensure the lambda function execution. 
Be cautious and do not assign permissions that are not necessary.

#### Add new tags on RDS instances
It is necessary to add at least one new tag to each RDS to backup, the only required tag is "backup", the tags "retentionsdays" and "deletesnapshot" are not necessary.
```
backups: True
deletesnapshot: False
retentiondays: 123
```
The __backup__ and, __deletesnapshot__ tags can take the values "__True__" or "__False__", as indicated here (__literally__)
The __retentiondays__ tag must have an integer value greater than one. The objective of this tag is to indicate the number of days the snapshot should be retained.

#### Create lambda function
1. Browse to AWS services Lambda and click on __Create fuction__ button.
2. Add function name
3. Select Python 3.6 on Runtime list.
4. Select __Choose an existing role__ on Role*.
5. On __Existing role*__ choose the previously created role
6. Click on __Create function__ botton to continue.
7. Remove the example code from the edition window and paste the python function code and click on __Save__ botton.
8. Move down to the page and in the __Basic Settings__ box add the __description__ and set the __Time out__ in 1 minute zero seconds and, click __Save__ botton again.
#### Add trigger to lambda function. 
1. Scroll down on __Add triggers__ choices and click on __CloudWatch Events__.
2. Scroll down to the bottom page and click on __Rule__ choices list and select __Create new rule__.
3. Add Rule name and, rule description.
4. Choose the __Schedule expression__ option button.
5. Enter a __Schedule expression*__. Enter a __Schedulle expression__ that fits with the execution needs. You can find a good examples on [Schedule Expressions Using Rate or Cron]
6. Click on __Adde__ botton.
7. Click 0n __Save__ botton

Now your lambda function works! it will be ready to take action or if you prefer, you can add a test and validate its operation.

[Schedule Expressions Using Rate or Cron]: <https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html>