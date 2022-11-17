import os
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_glue as glue,
)

DEFAULT_ARGUMENTS = {
    "--TempDir": f"s3://aws-glue-assets-{os.environ.get('ACCOUNT_ID')}-us-east-1/temporary/",
    "--job-language": "python",
    "--additional-python-modules":"string-color",
    "--extra-py-files":"s3://glue-etl-tests-permanence-predictions-pragma/glue-jobs-test/color_sentences_test/more_colors.py"
}


class CdkGlueJopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cfn_job = glue.CfnJob(
            self, "cdk_glue_job_test",
            command=glue.CfnJob.JobCommandProperty(
                name="pythonshell",
                python_version="3.9",
                script_location="s3://glue-etl-tests-permanence-predictions-pragma/glue-jobs-test/color_sentences_test/color_full.py"
            ),
            role=f"arn:aws:iam::{os.environ.get('ACCOUNT_ID')}:role/LF-GlueServiceRole",
            connections=glue.CfnJob.ConnectionsListProperty(
                connections=["permanence-prediction-pragma-connection"]
            ),
            default_arguments=DEFAULT_ARGUMENTS,
            description="This is a simple Glue job built on top of AWS CDK",
            execution_property=glue.CfnJob.ExecutionPropertyProperty(
                max_concurrent_runs=1
            ),
            max_retries=123,
            name="cdk_glue_job_test",
            tags={"project":"permanence_prediction_pragma"},
            timeout=2880,
        )
