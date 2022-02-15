from aws_cdk import (
    # Duration,
    Stack, aws_kinesisfirehose as firehos
    # aws_sqs as sqs,)
)
import aws_cdk as cdk
from constructs import Construct

class Firehose(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
