FROM ubuntu:latest

WORKDIR /src
ADD . /src

LABEL tugbot-test=true
LABEL tugbot-results-dir=/src/test-results
LABEL tugbot-event-docker=start
LABEL tugbot-event-docker-filter-image=re2:(.*)example-voting-app-vote

CMD [ "sh", "-c", "sleep 10" ]
