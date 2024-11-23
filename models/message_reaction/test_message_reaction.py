from models.message_reaction.message_reaction import MessageReaction

def test_new():
    conversation = MessageReaction(user_id="user_id", message_id="message_id", emoji=":)")

    assert str(conversation.user_id) == "user_id"
    assert str(conversation.message_id) == "message_id"
    assert str(conversation.emoji) == ":)"
