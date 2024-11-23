from models.conversation.conversation import Conversation


def test_new():
    conversation = Conversation(user_id="user1", opponent_user_id="user2")

    assert str(conversation.user_id) == "user1"
    assert str(conversation.opponent_user_id) == "user2"

def test_archive_conversation():
    conversation = Conversation(user_id="user1", opponent_user_id="user2")
    conversation = conversation.archive_conversation()

    assert bool(conversation.is_archived) is True
