from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["application"] == "devops-demo"

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
