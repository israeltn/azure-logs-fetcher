import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.loganalytics import LogAnalyticsDataClient
from azure.mgmt.security import SecurityCenter
from datetime import datetime, timedelta

# Initialize Azure credentials using DefaultAzureCredential (environment variables, managed identities, etc.)
credential = DefaultAzureCredential()

# Set up subscription and workspace details
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
log_analytics_workspace_id = os.getenv("AZURE_LOG_ANALYTICS_WORKSPACE_ID")

# Initialize clients
monitor_client = MonitorManagementClient(credential, subscription_id)
log_analytics_client = LogAnalyticsDataClient(credential)
security_center = SecurityCenter(credential, subscription_id)

# Define the time range for fetching logs (past 24 hours)
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=1)

# Function to get resource logs from Azure Monitor
def get_azure_monitor_logs(resource_group, resource_name):
    query = f"AzureDiagnostics | where TimeGenerated >= datetime({start_time.isoformat()})"
    result = monitor_client.metrics.list(resource_group_name=resource_group, resource_name=resource_name)
    for item in result.value:
        print(f"Metric Name: {item.name.localized_value}, Value: {item.timeseries}")

# Function to query Microsoft Sentinel logs
def get_sentinel_logs():
    query = "SecurityEvent | where TimeGenerated >= ago(24h) | take 10"
    query_results = log_analytics_client.query(log_analytics_workspace_id, query)
    for row in query_results.tables[0].rows:
        print(row)

# Function to query Microsoft Defender for Cloud Alerts
def get_defender_for_cloud_alerts():
    alerts = security_center.alerts.list(subscription_id)
    for alert in alerts:
        print(f"Alert: {alert.name}, Status: {alert.properties.status}")

# Function to query Microsoft Entra ID Protection logs (using Log Analytics)
def get_entra_id_protection_logs():
    query = "SigninLogs | where TimeGenerated >= ago(24h) and RiskLevelAggregated != 'none'"
    query_results = log_analytics_client.query(log_analytics_workspace_id, query)
    for row in query_results.tables[0].rows:
        print(row)

# Example usage
resource_group = "your-resource-group"
resource_name = "your-resource-name"

# Get logs from different services
get_azure_monitor_logs(resource_group, resource_name)
get_sentinel_logs()
get_defender_for_cloud_alerts()
get_entra_id_protection_logs()
