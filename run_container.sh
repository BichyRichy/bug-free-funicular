docker rm mad
docker run -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /tmp/$(mktemp -d):/run -p 8080:80  --detach --name mad mad
docker exec -it mad bash