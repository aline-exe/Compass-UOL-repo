### docker
docker build .
docker image/volume/container/network ls
docker ps
docker stop <idcontainer>
docker images
docker pull <library>
docker tag <nome>:<tag>
docker rmi <imagem>
docker system prune
docker run --rm <container>
docker cp
docker stats
docker push <imagem> (dockerhub)

### volumes
docker run -v /data (ou) docker run -v nomevolume:/data
docker run /dir/data:/data (/dir/data sendo o volume) - bind mount
docker volume ls
docker volume create <nome>
docker volume inspect <nome>
docker volume rm <nome>

### flags
--help
-t (nomear img na criação)
-i (docker start)
-f (forçar)
--rm

### redes
docker network create <nome>
docker networm rm <nome>
docker network prune

### compose
docker-compose up (-d)
docker compose down

### swarm
docker swarm init
docker node ls
docker service (ls)
docker service rm <nomeserviço)
docker service create --name <nome> --replicas <replicas> -p


### resumo
ls: listar
rm: remover
prune: remover não utilizados
