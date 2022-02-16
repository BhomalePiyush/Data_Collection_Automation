from aws_cdk import (
    # Duration,
    Stack, aws_ec2 as _ec2,
    aws_iam as _iam

    # aws_sqs as sqs,)
)
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
        bot=_ec2.Instance(self, "Instance1",
                          instance_type=_ec2.InstanceType(instance_type_identifier="t2.micro"),
                          instance_name="happymetogetfirstec2",
                          machine_image=_ec2.AmazonLinuxImage(
                            generation=_ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                            ),
                          block_devices=[_ec2.BlockDevice(
                              device_name="/dev/sdb",
                              volume=_ec2.BlockDeviceVolume.ebs(5)
                                                           )
                          ],
                          user_data=_ec2.UserData.custom(user_data),
                          key_name='ec2-access1',
                          vpc=vpc,
                          vpc_subnets=_ec2.SubnetSelection(
                             subnet_type=_ec2.SubnetType.PUBLIC
                             ),
                          )
        # add permissions to access services
        bot.role.add_managed_policy(
            _iam.ManagedPolicy.from_aws_managed_policy_name(
                "AccessPolicy1"
            )
        )


        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "Createec2Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )