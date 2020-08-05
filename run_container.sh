docker rm perf
docker run -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /tmp/$(mktemp -d):/run -p 8080:80  --detach --name perf mad:perf
docker exec -it perf bash