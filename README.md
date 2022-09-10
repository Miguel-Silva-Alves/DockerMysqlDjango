# DockerMysqlDjango

![APM](https://img.shields.io/apm/l/vim-mode?color=green&label=license&logo=mit&logoColor=mit&style=for-the-badge&logo=appveyor)
![Badge](https://img.shields.io/static/v1?label=python&message=tools&color=red&flat&logo=PYTHON&style=for-the-badge&logo=appveyor)
![Badge](https://img.shields.io/static/v1?label=django&message=framework&color=yellowgreen&flat&logo=PYTHON&style=for-the-badge&logo=appveyor)

# How to use

## Requirements

- [Docker](https://www.docker.com/)
- [Docker-compose](https://docs.docker.com/compose/install/)

## Install
``` 
cd DockerMysqlDjango/
docker-compose up -d --build mysql
docker-compose up --build django
```

## After change on Django
``` 
docker-compose up --build django
```

## Open mysql bash
``` 
docker-compose up -d mysql
docker exec -ti <container_id_mysql> bash
mysql -uroot -p
Enter password: (RootPassword)
show databases;
use Company;
show tables;
show columns from employees;
select * from employees;
```

## Quote

> [1] FALOURD, Guillaume. **Um pouco de Docker na prática**.(2022) https://www.zup.com.br/blog/docker-na-pratica?utm_source=google-chat&utm_medium=interno&utm_campaign=gc-geral%E2%80%A6