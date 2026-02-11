from app import app
import json

def test_add():
    client = app.test_client()
    response = client.post(
        "/add",
        data=json.dumps({"a": 2, "b": 3}),
        content_type="application/json"
    )
    assert response.json["result"] == 5
