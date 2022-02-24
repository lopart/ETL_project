from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
#from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'adhoc':False,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'trigger_rule': u'all_success'
}

dag = DAG(
    'ETL_pipeline',
    default_args=default_args,
    description='ETL pipeline for project',
    schedule_interval="@daily",
)

t1 = BashOperator(
   task_id='odd_api',
   bash_command='python3 ~/dags/scripts/odd_api.py',
   dag=dag,
)

t2 = BashOperator(
   task_id='kafka_input',
   bash_command='python3 ~/dags/scripts/kafka_producer.py',
   dag=dag,
)

t3 = BashOperator(
   task_id='structured_stream_output',
   bash_command='python3 ~/dags/scripts/kafka_to_spark.py',
   dag=dag,
)

t4 = BashOperator(
   task_id='aws_s3_dataflow',
   bash_command='python3 ~/dags/scripts/s3_sink.py',
   dag=dag,
)




t1.doc_md = """\
#### Task Documentation
You can document your task using the attributes `doc_md` (markdown),
`doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
rendered in the UI's Task Instance Details page.
![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
"""

dag.doc_md = __doc__
t1 >> t2 >> t3 >> t4
