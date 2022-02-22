from aws_cdk import (
    # Duration,
    Stack, aws_kinesis as _kinesis,
    Duration
    # aws_sqs as sqs,)
)

from constructs import Construct


class Kinesis(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stream = _kinesis.Stream(self, "MyCfnStream",
                                 stream_name="Ec2-Stream-Firehose",
                                 retention_period=Duration.hours(24),  #
                                 shard_count=2,
                                 stream_mode=_kinesis.StreamMode.PROVISIONED
                                 )
