from aws_cdk import (
    # Duration,
    Stack, aws_kinesis as kinesis
    # aws_sqs as sqs,)
)
import aws_cdk as cdk
from constructs import Construct

class Kinesis(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        kinesis.CfnStream(self, "MyCfnStream",
                          name="Ec2-Stream-Firehose",
                          retention_period_hours=24,
                          shard_count=1,
                          stream_mode_details=kinesis.CfnStream.StreamModeDetailsProperty(
                              stream_mode="provisioned"
                          ))

