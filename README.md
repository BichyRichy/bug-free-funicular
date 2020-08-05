MaDDash and Measurement Archive container
-----
### Getting the Image
The Docker image is hosted at https://hub.docker.com/repository/docker/rygao7/maddash. Start the container using
    $ docker run -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /tmp/$(mktemp -d):/run -p 8080:80  --detach --name mad mad

Port 8080 on the host machine is mapped to port 80 in the container.
The Maddash webpage is located at the /maddash-webui URL. To view on the host machine, go to http://localhost:8080/maddash-webui/
The esmond measurement archive is located at the  /esmond/perfsonar/archive URL. 

### Creating the Mesh
