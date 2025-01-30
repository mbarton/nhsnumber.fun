import nhs_number

def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": nhs_number.generate()[0]
    }
