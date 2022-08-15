# Define the name of the file with the code
LAMBDA_CODE_NAME="is_top_scorers_pl_available"
LAMBDA_FUNCTION_NAME="IsTopScorersPremierLeagueAvailable"

# Publish the needed layers
# Deleting useless binary files
mkdir deps \
&& cd deps \
&& unzip -qq ../../layers/layers.zip \

# Creating the final zip file with the code and the dependencies
cp ../${LAMBDA_CODE_NAME}.py . \
&& mv task/* . \
&& rm -r task \
&& rm requirements.txt \
&& cp ../../.env . \
&& zip -r9q ${LAMBDA_CODE_NAME}.zip . \
&& mv ${LAMBDA_CODE_NAME}.zip ../${LAMBDA_CODE_NAME}.zip \
&& cd .. \
&& rm -rf deps

# Delete lambda function if it exists 
deleted_function_output=$(awslocal lambda delete-function \
    --function-name ${LAMBDA_FUNCTION_NAME})

# Create the lambda function
awslocal lambda create-function \
    --function-name ${LAMBDA_FUNCTION_NAME} \
    --runtime python3.8 \
    --handler ${LAMBDA_CODE_NAME}.lambda_handler \
    --role arn:aws:iam::012345678901:role/DummyRole \
    --zip-file fileb://${LAMBDA_CODE_NAME}.zip \
    --layers requests