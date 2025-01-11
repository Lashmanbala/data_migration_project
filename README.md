# Data Migration Project

## Overview

In this project I've demonstrated the migration process of data from Mysql db to postgres db in a scalable way by using docker and airflow.

I have developed a custom python application for this migration process and containerized the application.

The python application container is being orchastrated by airflow. I've developed a DAG file to orchastrate.

Airflow is running with postgres db in docker container.

For demonstration purpose both mysql and postgres servers running in docker.

## Setup
To setup this project locally, follow these steps

1. **Clone This Repositories:**
  ```bash
  git clone https://github.com/Lashmanbala/data_migration_project
  ```

2. **Install Docker and Docker compose**
 
3. **Edit the docker compose file with your values of volumes and environment variables**
 
4. **Create a .env file like the sample.env file in dags directory**
  
5. **Run docker compose file**
   ```bash
    docker compose up
   ```
   Wait untill all the docker containers started and all the services are up
   
6. **Run the database scripts in the respective containers:**
   ```bash
    docker exec -it mysql_db bash -c "mysql --local-infile=1 -p${MYSQL_ROOT_PASSWORD} < /migration_project/database_files/mysql_cmds.sql"
   ```

   ```bash
    docker exec -it postgres_db bash -c " psql -U${POSTGRES_USER} -f /migration_project/database_files/postgres_cmds.sql"
   ```
   verify the databases

7. **Trigger the Dag in the Airflow web UI:**
    ```bash
    localhost:8080
    ```
