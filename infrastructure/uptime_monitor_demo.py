from aws_cdk import (
    # Duration,
    Duration,
    Stack,
    aws_events as events,
    aws_events_targets as targets,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as pylambda,
    aws_iam as iam
)
from constructs import Construct

class UptimeMonitorDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        schedule = events.Rule(
            self, "uptime-rule",
            rule_name="uptime-monitor",
            description="Every couple minutes, check if the website is online.",
            enabled=True,
            schedule=events.Schedule.rate(Duration.minutes(5))
        )

        uptime_function = pylambda.PythonFunction(
            self, "uptime-function",
            function_name="uptime-function",
            entry="src",
            index="website_pulse.py",
            handler="lambda_handler",
            architecture=lambda_.Architecture.ARM_64,
            runtime=lambda_.Runtime.PYTHON_3_9,
            memory_size=256,
            initial_policy=[
                iam.PolicyStatement(
                    actions=[
                        "ses:SendEmail"
                    ],
                    effect=iam.Effect.ALLOW,
                    resources=["*"]
                )
            ]
        )

        schedule.add_target(targets.LambdaFunction(uptime_function))
