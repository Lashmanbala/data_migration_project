from airflow.models.dag import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount

default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':0
}

dag = DAG(
    dag_id='migration_docker',
    description='Orchastrating docker containers for migration project',
    default_args=default_args,
    schedule=None,
    start_date=datetime(2025,1,3),
    catchup=False,
    tags=['Migration']
    )

migrate_tables_1 = DockerOperator(
    task_id='Migrating_small_tables',
    image='migrator:latest',
    container_name='migrator1',
    network_mode='migration_network',
    docker_url='unix://var/run/docker.sock',
    auto_remove='success',
    env_file='.env', # it should be the relative path not the absolute path
    environment={
        'TABLE_LIST_STR':'departments, categories, categories, products'
    },
    mounts=[
        Mount(source='/home/ubuntu/migration_project', target='/app', type='bind')
            ],
    dag=dag
)

migrate_tables_2 = DockerOperator(
    task_id='Migrating_orders_table',
    image='migrator:latest',
    container_name='migrator2',
    network_mode='migration_network',
    docker_url='unix://var/run/docker.sock',
    auto_remove='success',
    env_file='.env', # it should be the relative path not the absolute path
    environment={
        'TABLE_LIST_STR':'orders'
    },
    mounts=[
        Mount(source='/home/ubuntu/migration_project', target='/app', type='bind')
            ],
    dag=dag
)

migrate_tables_3 = DockerOperator(
    task_id='Migrating_order_items_table',
    image='migrator:latest',
    container_name='migrator3',
    network_mode='migration_network',
    docker_url='unix://var/run/docker.sock',
    auto_remove='success',
    env_file='.env', # it should be the relative path not the absolute path
    environment={
        'TABLE_LIST_STR':'order_items'
    },
    mounts=[
        Mount(source='/home/ubuntu/migration_project', target='/app', type='bind')
            ],
    dag=dag
)

migrate_tables_1
migrate_tables_2
migrate_tables_3