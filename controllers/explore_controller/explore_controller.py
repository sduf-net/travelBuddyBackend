from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.sduf_request.sduf_request import SdufRequest
from database import get_db
import uuid
import random
from utils.randomizer import get_random_woman_name, get_random_country_code, generate_label_widgets, get_random_image, get_random_occupation, get_random_university_name

router = APIRouter()

@router.post("")
async def profile(params: SdufRequest, db: Session = Depends(get_db)):
    print(params)
    widget = {
        "id": str(uuid.uuid4()),
        "name": "Touchable",
        "data": {
            "actions": {
                "click": {
                    "type": "navigate_to",
                    "screen_name": "profile_details"
                }
            }
        },
        "nestedComponents": [
            {
                "data": {
                    "props": {
                        "m": 10,
                        "shadow":"md",
                        "bg": "#EEEEEE",
                        "rounded": "xl"
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
                                            "uri": get_random_image(),
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
                                    "text": f"{get_random_woman_name()}, {random.randint(24, 32)}, {get_random_country_code()}"
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
            "callbackUrl": "{{HOST}}/explore"
        }
    }

    return [widget, api_widget]
