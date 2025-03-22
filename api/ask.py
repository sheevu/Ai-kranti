from agent import main

def handler(request):
    data = request.json()
    query = data.get("message")
    if not query:
        return {
            "statusCode": 400,
            "body": "No message provided"
        }

    reply = main.respond_to_query(query)
    return {
        "statusCode": 200,
        "body": reply
    }
