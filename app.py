#!/usr/bin/env python3
# import os

from My_stack.ec2_Stack import EC2
from My_stack.s3_Stack import S3
from My_stack.kinesis_Stack import Kinesis
from My_stack.firehose_Stack import Firehose
from My_stack.loaderbucket import LoaderS3
import aws_cdk as cdk


env_dev = cdk.Environment(account="993560847451", region="us-east-1")

app = cdk.App()
s3 = S3(app, "S3Storage", env=env_dev)
kinesis = Kinesis(app, "KinesisStreams", env=env_dev)
kinesis.add_dependency(s3,"it si dependency for firehosebut can not incluse so here kinesis")
firehos = Firehose(app, "Firehose-transport", env=env_dev)
firehos.add_dependency(kinesis,"kinesis should be present to start firehos")
ec2 = EC2(app, "Source-of-Stream-Data", env=env_dev)
ec2.add_dependency(kinesis, "Kinesis should be present to start push_records()")
LoaderS3(app, "CodeLoader", env=env_dev)

app.synth()
