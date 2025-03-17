import uuid
import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from utils.randomizer import get_random_city_name, get_random_country_code, generate_label_widgets, get_random_image, get_random_occupation, get_random_university_name
from sduf.api_client import send_event
from schemas.sduf_request.sduf_request import SdufRequest, SdufEvent

router = APIRouter()

@router.post("")
async def feed(params: SdufRequest, db: Session = Depends(get_db)):
    image = get_random_image()
    titile = f"{get_random_city_name()}, {random.randint(24, 32)}, {get_random_country_code()}"
    widget = {
        "id": str(uuid.uuid4()),
        "name": "Touchable",
        "data": {
            "actions": {
                "click": {
                    "type": "navigate_to",
                    "screen_name": "profile_details",
                    "extra": {
                        "image_url": image,
                        "title": titile,
                    }
                }
            }
        },
        "nestedComponents": [
            {
                "data": {
                    "props": {
                    }
                },
                "id": str(uuid.uuid4()),
                "name": "MangusDivWidget",
                "nestedComponents": [
                    {
                        "data": {
                            "props": {
                                "m": 10
                            }
                        },
                        "id": "fdeebe1f-609b-40b1-83f3-f5ea94bfc4b0",
                        "memo": "",
                        "name": "MangusDivWidget",
                        "nestedComponents": [
                            {
                                "data": {
                                    "props": {
                                        "bgImg": {
                                            "uri": image,
                                        },
                                        "h": 350,
                                        "resizeMode": "cover",
                                        "rounded": "xl"
                                    }
                                },
                                "id": "iba5b577-eb63-48bd-82e9-441d1ae42647",
                                "memo": "",
                                "name": "MangusDivWidget",
                                "nestedComponents": []
                            },
                            {
                                "data": {
                                    "props": {
                                        "fontSize": "2xl",
                                        "m": "lg",
                                        "ml": "none"
                                    },
                                    "text": titile
                                },
                                "id": "9b75877f-58f2-4208-884c-e31e612bcb5f",
                                "memo": "",
                                "name": "MangusTextWidget"
                            },
                            {
                                "id": "cdbf8783-91a3-4043-94ae-af13f74d44dd",
                                "memo": "",
                                "name": "TwoColumn",
                                "type": "layout",
                                "data": {
                                    "columns": 4
                                },
                                "nestedComponents": generate_label_widgets(),
                            },
                            {
                                "id": "ce3e0740-6588-4852-8314-e92d8ac33bb2",
                                "memo": "",
                                "name": "TextWidget",
                                "data": {
                                    "text": get_random_occupation()
                                },
                            },
                            {
                                "id": "ce3e0740-6588-4852-8314-e92d8ac33bb3",
                                "memo": "",
                                "name": "TextWidget",
                                "data": {
                                    "text": get_random_university_name()
                                },
                            },
                        ]
                    }
                ]
            }
        ]
    }

    api_widget = {
        "id": str(uuid.uuid4()),
        "name": "ApiWidget",
        "data": {
            "callbackUrl": "{{HOST}}/feed"
        }
    }

    return [widget, api_widget]


@router.post("/filter-popup")
async def filter_popup(params: SdufRequest, db: Session = Depends(get_db)):
    widget = {
        "id": "78b98613-30af-40c1-a815-e42ab7310f5f",
        "memo": "",
        "name": "MangusTextWidget",
        "display_name": "Text",
        "data": {
            "text": "MangusTextWidget",
            "props": {
                "fontSize": "lg",
                "fontWeight": "bold",
                "textTransform": "uppercase",
                "color": "red400",
                "letterSpacing": 2,
                "mt": "lg"
            }
        }
    }

    event = SdufEvent(
        event_id=str(uuid.uuid4()),
        user_id=params.user_id,
        project_id=params.project_id,
        screen_id=params.screen_id,
        action="open_popup",
        payload={"widget": widget}
    )
    send_event(event)
    return []
