# 📊 AWS Daily Cost Report Automation

This repository contains the complete source code for the blog series  
**[Daily Automated AWS Cost Reports by Email](https://devopsbug.com)** on [devopsbug.com](https://devopsbug.com).

The project demonstrates how to:

- Develop and test AWS Lambda functions locally using **SAM CLI**
- Query the AWS **Cost Explorer API** to retrieve daily cost data by service
- Send cost reports via **SNS Email**
- Automate daily execution using **Amazon EventBridge**

## 🔧 What’s Inside

This project uses the **AWS Serverless Application Model (SAM)** framework and is organized as follows:

```bash
├── sam-cost-report/ # Source code for the AWS Lambda function
│ ├── app.py # Lambda handler that queries AWS Cost Explorer
│ └── requirements.txt # Python dependencies
├── template.yaml # SAM template defining resources (Lambda, SNS, EventBridge)
└── README.md # You are here
```

## 📚 Related Blog Series

This repository accompanies the following blog series on [devopsbug.com](https://devopsbug.com):

1. **[Part 1](https://devopsbug.com/posts/testing-aws-lambda-locally/)** – Developing and Testing Lambda Functions Locally with SAM CLI  
2. **[Part 2](https://devopsbug.com/posts/create-daily-aws-cost-reports/)** – Building a Lambda that Queries AWS Cost Explorer  
3. **[Part 3](https://devopsbug.com/posts/create-daily-aws-cost-reports_sns/)** – Sending AWS Cost Reports via Email with SNS  
4. **[Part 4](https://devopsbug.com/posts/create-daily-aws-cost-reports_event_bridge/)** – Automating Lambda Execution Using EventBridge

## 🚀 Quick Start

To deploy the application using SAM CLI:

```bash
# 1. Clone the repository
git clone https://github.com/DevOpsBug/AWS_DailyCostReport.git
cd AWS_DailyCostReport

# 2. Build the SAM application
sam build

# 3. Deploy (you’ll be prompted for parameters)
sam deploy --guided
```

Make sure your AWS credentials are properly configured (~/.aws/credentials) and you have sufficient permissions to deploy Lambda, SNS, and EventBridge resources.

## 📬 Output
Once deployed, you will receive daily emails at 8 PM (UTC) containing a breakdown of your AWS service costs for the current day.

## 🧾 License
MIT – Feel free to use and adapt!