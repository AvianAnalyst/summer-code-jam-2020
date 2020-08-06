def test_urlconf(client):
    response = client.get('/chat/')
    assert response.status_code == 200
