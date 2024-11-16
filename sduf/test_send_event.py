# import pytest
# import responses
# from requests.exceptions import HTTPError
# from config import settings
# from sduf.api_client import send_event

# BASE_URL = settings.SDUF_BASE_URL

# # Test for a successful HTTP response
# @responses.activate
# def test_send_event_success():
#     # Mock the expected URL and response
#     responses.add(
#         responses.POST,
#         f"{BASE_URL}/push/event",
#         json={"status": "event received"},
#         status=200
#     )

#     # Call the function and check the result
#     result = send_event({})
#     assert result == {"status": "event received"}
#     assert len(responses.calls) == 1  # Ensure only one call was made
#     assert responses.calls[0].request.url == f"{BASE_URL}/push/event"

# # Test for an HTTP 500 Internal Server Error
# @responses.activate
# def test_send_event_internal_server_error():
#     # Mock the 500 response
#     responses.add(
#         responses.POST,
#         f"{BASE_URL}/push/event",
#         status=500
#     )

#     # Check that the function raises an HTTPError
#     with pytest.raises(HTTPError):
#         send_event({})
#     assert len(responses.calls) == 1
#     assert responses.calls[0].response.status_code == 500

# # Test for an HTTP 404 Not Found error
# @responses.activate
# def test_send_event_not_found():
#     # Mock the 404 response
#     responses.add(
#         responses.POST,
#         f"{BASE_URL}/push/event",
#         status=404
#     )

#     # Check that the function raises an HTTPError
#     with pytest.raises(HTTPError):
#         send_event({})
#     assert len(responses.calls) == 1
#     assert responses.calls[0].response.status_code == 404
