import json
import csv
from io import StringIO

def lambda_handler(event, context):
    # Example: Imagine this data came from an S3 CSV file or a request
    csv_data = """Name,Age,City
    Tom,25,New York
    Jack,30,Los Angeles
    Nick,35,Chicago
    """
    
    try:
        # Use the built-in csv module to read data
        f = StringIO(csv_data.strip())
        reader = csv.DictReader(f)
        
        data_list = []
        ages = []
        
        for row in reader:
            data_list.append(row)
            ages.append(int(row['Age']))
            
        # Calculate the mean without NumPy
        mean_age = sum(ages) / len(ages)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': "Success! No Pandas required.",
                'python_version': "3.14",
                'average_age': mean_age,
                'total_records': len(data_list),
                'data': data_list
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }