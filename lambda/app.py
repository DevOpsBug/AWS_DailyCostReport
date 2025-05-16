import boto3
import os
import json
from datetime import datetime

def lambda_handler(event, context):
    ce_client = boto3.client('ce')
    sns_client = boto3.client('sns')
    topic_arn = os.environ['SNS_TOPIC_ARN']
    print("Topic ARN: " + topic_arn)
    
    # Get first day of current month and today's date
    end_date = datetime.now().date()        #current date
    start_date = end_date.replace(day=1)    #first day of the month
    
    response = ce_client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date.strftime('%Y-%m-%d'),
            'End': end_date.strftime('%Y-%m-%d')
        },
        Granularity='MONTHLY',  # Changed to MONTHLY for month-to-date view
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )
    
    # Process and format the response
    cost_data = []
    total_cost = 0.00
    for result in response['ResultsByTime']:
        for group in result['Groups']:
            service_name = group['Keys'][0]
            amount = float(group['Metrics']['UnblendedCost']['Amount'])
            unit = group['Metrics']['UnblendedCost']['Unit']
            total_cost += amount        #aggregate total cost
            if amount > 0.00:           #filter out zero-cost services
                cost_data.append({
                    'Service': service_name,
                    'Cost': f"{amount:.2f}",
                    'Currency': unit
                })
    
    # Sort services by cost (highest to lowest)
    cost_data.sort(key=lambda x: float(x['Cost']), reverse=True)
    
    message = {
            'startDate': start_date.strftime('%Y-%m-%d'),
            'endDate': end_date.strftime('%Y-%m-%d'),
            'totalCost': f"{total_cost:.2f}",
            'costs': cost_data,
            'currency': unit    # Currency unit
        }
    
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=json.dumps(message),
        Subject='AWS Daily Cost Report'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Cost report sent successfully!',
            'sns_response': response,
            
        })
    }
