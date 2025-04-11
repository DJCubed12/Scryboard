from flask import current_app, request


@current_app.post("/rfid")
def post_rfid():
    data = request.json
    print("New RFID post:", data)

    if data["rfid"]:
        return {"success": True, "rfid": data["rfid"]}
    else:
        return {
            "success": False,
            "message": "No 'rfid' field included in request.",
        }, 400
