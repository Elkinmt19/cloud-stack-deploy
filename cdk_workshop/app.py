#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack
from cdk_workshop.cdk_glue_job_stacks import CdkGlueJopStack

app = cdk.App()
# CdkWorkshopStack(app, "cdk-workshop")
CdkGlueJopStack(app, "cdk-glue-job-test")

app.synth()
