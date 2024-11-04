pip freeze > requirements.txt
chmod +x ./entrypoint.sh

<!-- 

docker compose up: Starts up the containers defined in the docker-compose.yml file, creating and starting the containers if they don't exist yet.

-d (detached mode): Runs the containers in the background, allowing you to continue using the terminal after the containers start.

--build: Forces a rebuild of the images before starting the containers, even if they already exist. This is helpful if you’ve made changes to your Dockerfile or application code and want to apply them without manually rebuilding the images.

 -->
 
docker compose up -d --build
docker exec -it container_name /bin/sh

<!-- giving the host machine the right over the docker files -->
chown -R 1000:1000 /usr/src/app
<!-- check if all file rights has been change to the host machine-->
ls -l /usr/src/app

<!-- To view all images -->
docker images

<!-- this will remove dangling (unused) images, helping manage disk space. -->
docker image prune -f


tp.delay()
tp1.delay()
tp2.delay()
tp3.delay()

<!-- grouping task -->
from celery import group
from newapp.task import tp, tp1, tp2, tp3
tasks_group = group(tp.s(), tp1.s(), tp2.s(), tp3.s())
tasks_group.apply_async()