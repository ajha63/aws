import boto3
import datetime

def lambda_handler(event, context):

    print("Connecting to RDS")
    client = boto3.client('rds')

    for rds in client.describe_db_instances()['DBInstances']:
        dbinstancearn = rds['DBInstanceArn']
        dbinstanceid = rds['DBInstanceIdentifier']
        tagsdic = {}

        for tags in client.list_tags_for_resource(ResourceName=dbinstancearn)['TagList']:
            tagsdic[tags['Key']] = tags['Value']

        if (('backup' in tagsdic) and (tagsdic['backup'] == 'True')):
            # Get retention day tag
            if 'retentiondays' in tagsdic:
                retentionDays = tagsdic['retentiondays']
            else: 
                retentionDays = 365
            # Get deletesnap tag
            if 'deletesnapshot' in tagsdic:
                if tagsdic['deletesnapshot']:
                    deleteSnap = 'True'
                else:
                    deleteSnap = 'False'
            else:
                deleteSnap = 'False'

            rightnow = datetime.datetime.now().strftime("%Y-%m%d%H%M")
            snapname = "{0:s}-{1:s}".format(dbinstanceid, rightnow)
            
            print("RDS snapshot backups to: {0:s} started at: {1:s}".format(dbinstanceid, rightnow))
            client.create_db_snapshot(
                DBInstanceIdentifier=dbinstanceid,
                DBSnapshotIdentifier=snapname,
                Tags = [
                    {
                        'Key': 'retentiondays',
                        'Value': retentionDays
                    },
                    {
                        'Key': 'deletesnapshot',
                        'Value': str(deleteSnap)
                    },
                ]
            )
        else:
            print("No RDS snapshot to: {0:s}".format(dbinstanceid))
