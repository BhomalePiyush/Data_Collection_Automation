from aws_cdk import (
    # Duration,
    Stack, aws_kinesisfirehose as _firehose
    # aws_sqs as sqs,)
)
from s3_Stack import S3
from kinesis_Stack import Kinesis
from constructs import Construct


class Firehose(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        _firehose.CfnDeliveryStreamProps(
                    s3_destination_configuration=_firehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn=S3.Bucket_arn,
                        role_arn="roleArn",
                        # the properties below are optional
                        buffering_hints=_firehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=60,
                            size_in_mBs=1
                        )
                    ),
                    kinesis_stream_source_configuration=
                    _firehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty(
                                            kinesis_stream_arn=Kinesis.Stream_arn,
                                            role_arn="roleArn")
        )

