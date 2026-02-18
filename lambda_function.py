import json
import pandas as pd
import numpy as np

def lambda_handler(event, context):
    print("Testing Pandas and NumPy on Python 3.14...")
    
    try:
        # Create a simple DataFrame to test the layer
        data = {
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': ['Python', '3.14', 'Rocks']
        }
        df = pd.DataFrame(data)
        
        # Perform a small calculation with NumPy
        mean_val = np.mean(df['A'])
        
        message = f"Successfully used Pandas {pd.__version__} and NumPy {np.__version__}"
        print(message)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': message,
                'mean_of_column_A': float(mean_val),
                'dataframe_summary': df.to_dict()
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
