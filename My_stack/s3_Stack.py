from aws_cdk import (
    # Duration,
    Stack, aws_s3 as _s3
    # aws_sqs as sqs,
)
import aws_cdk as cdk
from constructs import Construct


class S3(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        Bucket=_s3.Bucket(self,
                           "myfirstbucket",
                           bucket_name='s3newpiyusbhomale1999',
                           versioned=True,
                           block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
                           removal_policy=cdk.RemovalPolicy.DESTROY)  # Destroy S3 when cloud is destroyed if empty
        Bucket_arn=Bucket.bucket_arn()
