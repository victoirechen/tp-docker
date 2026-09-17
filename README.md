# tp-docker
les dossier pour le TP docker

ex3:
PS C:\Users\victo\Desktop\tp_docker> docker --version                                                                    
Docker version 29.8.0, build 88096ef

PS C:\Users\victo\Desktop\tp_docker> docker images   
i Info →   U  In Use
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA

PS C:\Users\victo\Desktop\tp_docker> docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:5e23090353324d887c48ad5e5c56d294eab81588df9605b07d1afe895f9cc8f8
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
PS C:\Users\victo\Desktop\tp_docker> docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
   (amd64)
3. The Docker daemon created a new container from that image which runs the
   executable that produces the output you are currently reading.
4. The Docker daemon streamed that output to the Docker client, which sent it
   to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
$ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
https://hub.docker.com/

For more examples and ideas, visit:
https://docs.docker.com/get-started/

PS C:\Users\victo\Desktop\tp_docker> docker ps              
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

PS C:\Users\victo\Desktop\tp_docker> docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
f9524da34b13   hello-world   "/hello"   8 minutes ago   Exited (0) 5 minutes ago             eager_raman

PS C:\Users\victo\Desktop\tp_docker> docker rm f9524da34b13  
f9524da34b13

PS C:\Users\victo\Desktop\tp_docker> docker ps -a          
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

PS C:\Users\victo\Desktop\tp_docker> docker rmi hello-world
Untagged: hello-world:latest
Deleted: sha256:5e23090353324d887c48ad5e5c56d294eab81588df9605b07d1afe895f9cc8f8