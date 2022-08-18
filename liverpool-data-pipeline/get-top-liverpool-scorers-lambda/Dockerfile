FROM public.ecr.aws/lambda/python:3.8

COPY get_top_liverpool_scorers.py ${LAMBDA_TASK_ROOT}

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD [ "get_top_liverpool_scorers.handler" ] 