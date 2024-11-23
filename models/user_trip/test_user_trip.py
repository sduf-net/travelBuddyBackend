from datetime import date
from models.user_trip.user_trip import UserTrip


def test_create_user_trip():
    user = UserTrip(
        user_id="user_id",
        start_date=date.today(),
        end_date=date.today(),
        country="country",
        province="province",
        city="city")

    assert str(user.user_id) == "user_id"
    assert str(user.start_date) == str(date.today())
    assert str(user.end_date) == str(date.today())
    assert str(user.country) == "country"
    assert str(user.province) == "province"
    assert str(user.city) == "city"
