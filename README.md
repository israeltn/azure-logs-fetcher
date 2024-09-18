# Azure Logs Fetcher

This Python script allows you to log in to Azure using Azure SDKs, and retrieve logs from various services such as Azure resources, Microsoft Sentinel, Microsoft Entra ID Protection (formerly Azure AD Identity Protection), and Microsoft Defender for Cloud.

## Features

- **Azure Resource Logs**: Fetch metrics and logs from any Azure resource using Azure Monitor.
- **Microsoft Sentinel Logs**: Query Security Events from Microsoft Sentinel via Log Analytics.
- **Microsoft Entra ID Protection Logs**: Retrieve risky sign-in logs from Microsoft Entra ID Protection (formerly Azure AD Identity Protection) using Log Analytics.
- **Microsoft Defender for Cloud Alerts**: Get alerts from Microsoft Defender for Cloud.

## Prerequisites

1. **Python 3.x**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Azure Subscription**: You must have an active Azure subscription.
3. **Azure CLI** (Optional): For testing and easier authentication, you can install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
4. **Required Azure SDKs**: Install the necessary SDKs using `pip`:

   ```bash
   pip install azure-identity azure-mgmt-monitor azure-loganalytics azure-mgmt-security
   ```


** Clone the repository (or download the project):**

   ```bash   
   git clone https://github.com/your-repo/azure-logs-fetcher.git
   cd azure-logs-fetcher
   Set up the virtual environment:
      ```
   ```bash  
   Copy code
   python -m venv venv
   Activate the virtual environment:
   ```
Windows:
```bash  

venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```
Install the dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```