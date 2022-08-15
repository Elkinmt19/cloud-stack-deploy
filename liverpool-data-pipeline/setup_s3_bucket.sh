# Define the name of the bucket that is gonna be created
BUCKET_NAME="elkinmle19-top-liverpool-scorers"

# Delete the bucket if it already exits
delete_bucket=$(awslocal s3api delete-bucket \
    --bucket ${BUCKET_NAME})

# Create the bucket
awslocal s3api create-bucket \
    --bucket ${BUCKET_NAME}