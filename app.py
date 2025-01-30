import nhs_number

def handler(event, context):
    path = event["requestContext"]["http"]["path"]
    quantity = 1

    if path != "/":
        quantity = min(int(path[1:]), 1000)

    numbers = nhs_number.generate(quantity=quantity)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": "\n".join(numbers)
    }
