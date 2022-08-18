# Define the name of the file with the code
LAMBDA_FUNCTION_NAME="IsTopScorersPremierLeagueAvailable"

# Invoke the lambda function of order to test it
aws lambda invoke \
    --function-name ${LAMBDA_FUNCTION_NAME} \
    --invocation-type RequestResponse \
    --log-type Tail \
    --payload '{ "data": "test" }' \
    output.json