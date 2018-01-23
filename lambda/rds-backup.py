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

        if ('backup' in tagsdic and tagsdic['backup'] == 'si'):
            starttime = datetime.datetime.now().strftime("%y-%m-%d-%H:%M")
            print("RDS snapshot backups to: {0:s} started at: {1:s}".format(dbinstanceid, starttime))
            today = datetime.datetime.now().strftime("%Y%m%d%H%M")
            snapname = "{0:s}-{1:s}".format(dbinstanceid, today)
            client.create_db_snapshot(
                DBInstanceIdentifier=dbinstanceid,
                DBSnapshotIdentifier=snapname
            )
        else:
            print("No RDS snapshot to: {0:s}".format(dbinstanceid))
