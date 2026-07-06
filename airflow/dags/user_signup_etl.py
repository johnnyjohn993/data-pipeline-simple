from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
# Placeholder imports representing your internal package structure
# from src.transformations.clean_users import run_cleansing
# from src.utils.s3_uploader import upload_to_s3

default_args = {
    'owner': 'data_engineering',
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_from_mysql():
    print("Extracting new signups from MySQL OLTP...")
    return [{"id": 1, "username": "  john_doe ", "email": "JOHN@example.com", "created_at": "2026-07-01"}]

def transform_data(ti):
    raw_data = ti.xcom_pull(task_ids='extract_task')
    print(f"Transforming and cleansing {len(raw_data)} records...")
    # Clean logic simulated
    cleaned = [{k: v.strip().lower() if isinstance(v, str) else v for k, v in row.items()} for row in raw_data]
    return cleaned

def load_to_s3(ti):
    cleaned_data = ti.xcom_pull(task_ids='transform_task')
    print(f"Uploading OLAP-ready data to S3 Data Lake: {cleaned_data}")

with DAG('user_signup_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    extract_task = PythonOperator(task_id='extract_task', python_callable=extract_from_mysql)
    transform_task = PythonOperator(task_id='transform_task', python_callable=transform_data)
    load_task = PythonOperator(task_id='load_task', python_callable=load_to_s3)

    extract_task >> transform_task >> load_task
