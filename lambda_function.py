import json
import pandas as pd
import numpy as np

def lambda_handler(event, context):
    try:
        # Create simple dataframe
        data = pd.DataFrame({
            "numbers": [10, 20, 30, 40]
        })

        # Use numpy to calculate mean
        mean_value = np.mean(data["numbers"])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Dependencies loaded successfully   ✅",
                "pandas_version": pd.__version__,
                "numpy_version": np.__version__,
                "calculated_mean": float(mean_value)
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
