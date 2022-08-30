FROM public.ecr.aws/lambda/python:3.8

RUN pip install sklearn

COPY iris_model.sav .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]