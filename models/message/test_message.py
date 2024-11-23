from models.message.message import Message

def test_new():
    message = Message(conversation_id="conversation_id", sender_id="sender_id", content="content", reply_to_id="reply_to_id")

    assert str(message.conversation_id) == "conversation_id"
    assert str(message.sender_id) == "sender_id"
    assert str(message.content) == "content"
    assert str(message.reply_to_id) == "reply_to_id"
