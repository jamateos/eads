FROM elgalu/selenium:latest

WORKDIR /src
ADD . /src

LABEL tugbot-test=true
LABEL tugbot-results-dir=/src/test-results
LABEL tugbot-event-docker=start
LABEL tugbot-event-docker-filter-image=re2:(.*)examplevotingapp_vote(.*)

COPY selenium/prepare-container.sh /src/prepare-container.sh
COPY selenium/example.py /src/example.py

CMD [ "bash", "-c", "sudo /bin/bash /src/prepare-container.sh; xvfb-run python /src/example.py;" ]
