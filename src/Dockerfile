FROM python:3.8-slim

RUN useradd --create-home --shell /bin/bash app_user

USER app_user
WORKDIR /home/app_user


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt 
# Change ownership of the files and directories to be copied
COPY --chown=app_user:app_user . .
# RUN chown -R app_user /home/app_user/Results
# RUN APP_UID=$(id -u):$(id -g)

CMD ["bash"] 



# /home/user/2022/Develop/prior22v1/src/Dockerfile
