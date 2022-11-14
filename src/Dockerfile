FROM python:3.8-slim

RUN useradd --create-home --shell /bin/bash app_user

RUN chown app_user:app_user -R /home/app_user/

WORKDIR /home/app_user


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt 


USER app_user

COPY . .
# RUN chown -R app_user /home/app_user/Results


CMD ["bash"] 

# /home/user/2022/Develop/prior22v1/src/Dockerfile