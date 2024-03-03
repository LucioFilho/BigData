**DOCKER BASICS**

**Build**

***Build an image from the Dockerfile in the current directory and tag the image***
docker build -t myimage:1.0 .

***List all images that are locally stored with the Docker Engine***
docker image ls

***Delete an image from the local image store***
docker image rm alpine:3.4

**Share**

***Pull an image from a registry*** 
docker pull myimage:1.0

***Retag a local image with a new image name and tag***
docker tag myimage:1.0 myrepo/myimage:2.0

***Push an image to a registry***
docker push myrepo/myimage:2.0

**Run**

***Run a container from the Alpine version 3.9 image, name the running container “web” and expose port 5000 externally, mapped to port 80 inside the container.***
docker container run --name web -p 5000:80 alpine:3.9

***Stop a running container through SIGTERM***
docker container stop web

***Stop a running container through SIGKILL***
docker container kill web

***List the networks***
docker network ls

***List the running containers (add --all to include stopped containers)***
docker container ls

***Delete all running and stopped containers***
docker container rm -f $(docker ps -aq)

***Print the last 100 lines of a container’s logs***
docker container logs --tail 100 web

**Docker Management**

***All commands below are called as options to the base docker command.*** 
***Run docker <command> --help for more information on a particular command.***

app*        ***Docker Application***
assemble*   ***Framework-aware builds (Docker Enterprise)***
builder     ***Manage builds***
cluster     ***Manage Docker clusters (Docker Enterprise)***
config      ***Manage Docker configs***
context     ***Manage contexts***
engine      ***Manage the docker Engine***
image       ***Manage images***
network     ***Manage networks***
node        ***Manage Swarm nodes***
plugin      ***Manage plugins***
registry*   ***Manage Docker registries***
secret      ***Manage Docker secrets***
service     ***Manage services***
stack       ***Manage Docker stacks***
swarm       ***Manage swarm***
system      ***Manage Docker***
template*   ***Quickly scaffold services (Docker Enterprise)***
trust       ***Manage trust on Docker images***
volume      ***Manage volumes***


**COMMANDS**
***https://docker-curriculum.com/***

docker pull

docker images ***list of images that are available locally***

docker run 'container_name'
docker run 'container_name' echo 'hello'

docker ps ***shows you all containers that are currently running***

docker ps -a ***list of all containers that we ran***

docker rm ***clean up containers***

exit to ***exit***

# deletes all containers that have a status of exited
docker rm $(docker ps -a -q -f status=exited)

docker container prune ***WARNING! This will remove all stopped containers.***


**STATIC SITES**

docker run --rm -it prakhar1989/static-site

docker run -d -P --name static-site prakhar1989/static-site
***-d will detach our terminal, -P will publish all exposed ports to random ports and finally --name corresponds to a name we want to give***

docker port static-site ***open http://localhost:32769 in your browser.***
* 80/tcp -> 0.0.0.0:32769
* 443/tcp -> 0.0.0.0:32768

docker run -p 8888:80 prakhar1989/static-site
***You can also specify a custom port to which the client will forward connections to the container.***

docker stop static-site ***To stop a detached containe***