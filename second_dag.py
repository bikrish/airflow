import logging
import os

import pendulum

from airflow import DAG
from airflow.configuration import conf
from airflow.decorators import task
from airflow.example_dags.libs.helper import print_stuff

try:
    from kubernetes.client import models as k8s
except ImportError:
    log.warning(
        "The example_kubernetes_executor example DAG requires the kubernetes provider."
        " Please install it with: pip install apache-airflow[cncf.kubernetes]"
    )
    k8s = None

if k8s:
    with DAG(
        dag_id='example_kubernetes_executor',
        schedule_interval=None,
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        tags=['example3'],
    ) as dag:

        echo_task = BashOperator(task_id="echo",
                                bash_command='echo "this is hello message"')

        recv_task = BashOperator(task_id="recv",
                                bash_command='echo "task recieved"')

echo_task >> recv_task