from models.read_receipt.read_receipt import ReadReceipt


def test_new():
    read_receipt = ReadReceipt(conversation_id="conversation_id",
                                     user_id="user_id", last_read_message_id="last_read_message_id")

    assert str(read_receipt.conversation_id) == "conversation_id"
    assert str(read_receipt.user_id) == "user_id"
    assert str(read_receipt.last_read_message_id) == "last_read_message_id"
