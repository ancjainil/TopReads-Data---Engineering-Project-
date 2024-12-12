from airflow.plugins_manager import AirflowPlugin

import operators
import helpers

# Defining the plugin class
class TopReadsPlugin(AirflowPlugin):
    name = "topreads_plugin"
    operators = [
        operators.DataQualityOperator,
        helpers.LoadAnalyticsOperator
    ]
