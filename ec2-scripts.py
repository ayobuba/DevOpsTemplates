import click
import pprint

from boto3_type_annotations.ec2 import ServiceResource
from boto3_type_annotations.ec2 import Client
import boto3
from botocore.exceptions import ClientError

ec2_resource: ServiceResource = boto3.resource('ec2')
ec2_client: Client = boto3.client('ec2')


@click.group()
def cli():
    """Script manages ec2 instances"""
    pass


@cli.command('create-instance')
@click.argument('ami')
def create_ec2(ami):
    try:
        instance = ec2_resource.create_instances(
            InstanceType='t2.micro',
            KeyName='EffectiveDevOps',
            SecurityGroupIds=['sg-02b4eef405594c38f'],
            ImageId=ami,
            MaxCount=1,
            MinCount=1
            # ImageId='ami-00eb20669e0990cb4'
        )
        print(instance[0].id)
    except ClientError as e:
        print(e)


@cli.command('describe-instance')
@click.argument('ami')
def describe_ec2_instance(ami):
    try:
        instance = ec2_client.describe_instances(
            InstanceIds=[ami]
        )

        pprint.pprint(instance)
    except ClientError as e:
        print(e)

@cli.command('delete-instance')
@click.argument('ami')
def delete_instance(ami):
    try:
        instance = ec2_client.terminate_instances(InstanceIds=[ami], DryRun=False)
        pprint.pprint(instance)
    except ClientError as e:
        print(e)

@cli.command('get-vpc-id')
@click.argument()


if __name__ == '__main__':
    cli()

# describe_ec2_instance('i-0d26268b135614f2a')
