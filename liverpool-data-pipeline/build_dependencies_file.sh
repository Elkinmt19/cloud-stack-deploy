# Define the container image name and container name
CONTAINER_NAME="lambda_layer"
CONTAINER_IMAGE_NAME="elkinmle19/lambda-functions-dev:requests-pandas-dotenv"
LAYER_FILE_NAME="layers.zip"

# Built the container locally
docker build -t ${CONTAINER_IMAGE_NAME} .

# Fetch the dependencies zip file
docker run --rm --name ${CONTAINER_NAME} -itd ${CONTAINER_IMAGE_NAME}
docker cp ${CONTAINER_NAME}:/var/task ./layers/
docker stop ${CONTAINER_NAME}

# Zip the folder
cd layers/ \
&& zip -r ${LAYER_FILE_NAME} task \
&& rm -r task


