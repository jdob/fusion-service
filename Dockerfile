FROM python:3

EXPOSE 8000

ENV HOME=/code
RUN mkdir -p ${HOME} && \
    useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin \
            -c "Fusion Application User" default
WORKDIR ${HOME}


ADD fusion ${HOME}/fusion
ADD requirements.txt manage.py setup.py ${HOME}/

RUN pip install -r requirements.txt -e .

RUN chown -R 1001:0 ${HOME} && \
    find ${HOME} -type d -exec chmod g+ws {} \;

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
USER 1001
