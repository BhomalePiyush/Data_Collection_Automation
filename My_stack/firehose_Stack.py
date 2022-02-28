from aws_cdk import (
    # Duration,
    Stack, aws_kinesisfirehose as _firehose

    # aws_sqs as sqs,)
)

from constructs import Construct


class Firehose(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        _firehose.CfnDeliveryStream(self, "streamtos3bucket",
                                    delivery_stream_name="Streams-to-S3",
                                    delivery_stream_type="KinesisStreamAsSource",
                                    s3_destination_configuration=_firehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                                     bucket_arn='arn:aws:s3:::s3newpiyusbhomale1999',
                                     role_arn="arn:aws:iam::993560847451:role/Firehose-Role-To-access-Kinesis-s3",
                                     # the properties below are optional
                                     buffering_hints=_firehose.CfnDeliveryStream.BufferingHintsProperty(
                                                                                                interval_in_seconds=300,
                                                                                                size_in_m_bs=1
                                                                                                 )
                                     ),
                                    kinesis_stream_source_configuration=_firehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty(
                                            kinesis_stream_arn='arn:aws:kinesis:us-east-1:993560847451:stream/Ec2-Stream-Firehose',
                                            role_arn="arn:aws:iam::993560847451:role/Firehose-Role-To-access-Kinesis-s3"
                                     )
                                     )

