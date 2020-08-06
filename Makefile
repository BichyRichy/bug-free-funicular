build: buildEsmond buildMaddash

buildEsmond: esmondImage/Dockerfile
	cd esmondImage
	docker build --tag mad:esmond esmondImage

buildMaddash: MaddashImage/Dockerfile MaddashImage/maddash.yaml
	cd MaddashImage
	docker build --tag mad:perf MaddashImage

run: runEsmond runMaddash

runEsmond:
	docker rm esmond
	docker run -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /tmp/$(mktemp -d):/run -p 8090:80  --detach --name esmond mad:esmond
	docker exec -it esmond bash

runMaddash:
	docker rm perf
	docker run -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /tmp/$(mktemp -d):/run -p 8080:80  --detach --name perf mad:perf
	docker exec -it perf bash