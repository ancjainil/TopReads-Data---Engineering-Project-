## warehouse_config.cfg file in warehouse folder contains  

    [AWS]  
    KEY=<AWS-KEY>
    SECRET=<AWS-SECRET-KEY>
      
    [CLUSTER]  
    HOST='<Redshift Cluster Endpoint>'  
    DB_NAME='<db-name>'  
    DB_USER='<db-user-name>'  
    DB_PASSWORD='<db-password>'  
    DB_PORT=<db-port, default 5439>  
      
    [IAM_ROLE]  
    ARN=<Redshift ARN role>
      
      
    [STAGING]  
    SCHEMA=<Warehouse-staging-schema>  
      
    [WAREHOUSE]  
    SCHEMA=<Warehouse-schema>  
      
      
    [BUCKET]  
    LANDING_ZONE=<landing-zone-bucket>  
    WORKING_ZONE=<working-zone-bucket>
    PROCESSED_ZONE=<processed-zone-bucket>

The driver in `topreads_warehouse_driver.py` first loads staging tables and then issues UPSERTs into the warehouse schema using queries from `topreads_staging_queries.py` and `topreads_warehouse_queries.py`. Ensure the IAM role has `COPY` permissions on the processed bucket and that the target schemas already exist before running the driver.
