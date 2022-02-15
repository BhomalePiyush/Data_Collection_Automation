from aws_cdk import (
    # Duration,
    Stack, aws_ec2 as _ec2

    # aws_sqs as sqs,)
)
import aws_cdk as cdk
from constructs import Construct

class EC2(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # initialize your vpc
        vpc = _ec2.Vpc.from_lookup(self,
                                   "importVPC",
                                   vpc_id="vpc-0efbae3722b5b51c9")
        #Read Bootstrap Script
        with open('bootstrap_script/install_http.sh', mode="r") as file:
            user_data=file.read()


        # ec2 instance creation
        _ec2.Instance(self, "Instance1",
                      vpc=vpc,
                      instance_type=_ec2.InstanceType(instance_type_identifier="t2.micro"),
                      instance_name="happymetogetfirstec2",
                      machine_image=_ec2.AmazonLinuxImage(),
                      user_data=_ec2.UserData.custom(user_data),
                      )


        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "Createec2Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )