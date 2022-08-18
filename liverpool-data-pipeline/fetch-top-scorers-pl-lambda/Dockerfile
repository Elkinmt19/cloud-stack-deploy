FROM public.ecr.aws/lambda/python:3.8

COPY fetch_top_scorers_pl.py ${LAMBDA_TASK_ROOT}

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD [ "fetch_top_scorers_pl.handler" ] 