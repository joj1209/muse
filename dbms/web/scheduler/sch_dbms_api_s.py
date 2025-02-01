import time
import requests
import logging
from dbms.common.common_func import save_data
from dbms.models.api_models import ApiDataSum
from django.db import connection

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
def my_custom_sql(self,strd_d):
    logger.info('--51 [run_sch_dbms_api_s] Start !!')         
    with connection.cursor() as cursor:
        cursor.execute("select * from td_dbms_api_s where strd_dt=%s",[strd_d])
        # cursor.execute("select * from td_dbms_api_s where strd_dt='20241126'")
        # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        # row = cursor.fetchone()
        row = cursor.fetchall()
        
    print(row)    
    
    logger.info('--51 [run_sch_dbms_api_s] End !!')         
    return row