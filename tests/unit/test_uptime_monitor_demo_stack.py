import aws_cdk as core
import aws_cdk.assertions as assertions

from uptime_monitor_demo.uptime_monitor_demo_stack import UptimeMonitorDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in uptime_monitor_demo/uptime_monitor_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = UptimeMonitorDemoStack(app, "uptime-monitor-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
