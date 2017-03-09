FROM gaiaadm/pumba:latest

WORKDIR /src
ADD . /src

LABEL tugbot-test=true
LABEL tugbot-results-dir=/src/test-results
LABEL tugbot-event-docker=start
LABEL tugbot-event-filter-type=container
LABEL tugbot-event-docker-filter-action=start
LABEL tugbot-event-docker-filter-container=examplevotingapp_app

CMD [ "/bin/sh", "-c", "sleep 10; pumba kill examplevotingapp_app" ]
