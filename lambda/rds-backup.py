import boto3
import datetime

# https://gist.github.com/mzupan/41d01bfb3b4c292fdac0

def lambda_handler(event, context):
    print("Connecting to RDS")
    client = boto3.client('rds')
    
    print("RDS snapshot backups stated at %s...\n" % datetime.datetime.now())
    client.create_db_snapshot(
        DBInstanceIdentifier='web-platform-slave', 
        DBSnapshotIdentifier='web-platform-%s' % datetime.datetime.now().strftime("%y-%m-%d-%H"),
        Tags=[
            {
                'Key': 'backupRetention',
                'Value': '1825'
            },
        ]
    )
    