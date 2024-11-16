# def test_profile(client):
#     response = client.post("/profile", json={
#         "payload": {},
#         "user_id": "user:travel:123",
#         "screen_id": 12,
#         "action": "zaction",
#         "project_id": "project"
#     })

#     assert response.status_code == 200
#     assert "message" in response.json()

# def test_profile_edit(client):
#     response = client.post("/profile/edit", json={
#         "payload": {},
#         "user_id": "user:travel:123",
#         "screen_id": 12,
#         "action": "action",
#         "project_id": "project"
#     })
#     assert response.status_code == 200
#     assert "message" in response.json()
