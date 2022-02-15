#!/usr/bin/env python3
# import os

import aws_cdk as cdk

from My_stack.s3_Stack import S3
from My_stack.kinesis_Stack import Kinesis
from My_stack.firehose_Stack import Firehose
from My_stack.ec2_Stack import EC2

env_dev = cdk.Environment(account="993560847451", region="us-east-1")
app = cdk.App()

S3(app, "S3Storage", env=env_dev)

Kinesis(app, "KinesisStreams", env=env_dev,)

EC2(app, "Source-of-Stream-Data", env=env_dev, )
Firehose(app, "Firehose-transport", env=env_dev, )
app.synth()
