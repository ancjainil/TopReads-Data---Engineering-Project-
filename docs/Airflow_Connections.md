## Setting up Airflow Connections for this project
### Setting up ssh connection to submit jobs to EMR cluster
Goto Admin -> Connections -> Create.
Suggested Conn Id: `emr_ssh_default`
![Airflow EMR SSH Connection](images/Airflow_EMR_ssh.PNG)

### Setting up Airflow Redshift Connection
Goto Admin -> Connections -> Create.
Suggested Conn Id: `redshift_default`
![Airflow Redshift Connection](images/Airflow_Redshift.PNG)
