# 
FROM python:3.8

# 
WORKDIR /code

# 
COPY ./ /code/

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
CMD [ "python", "./main.py"]
