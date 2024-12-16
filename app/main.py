from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    without_mask = 0
    without_vaccine = 0
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, friend)
        except VaccineError:
            without_vaccine += 1
        except NotWearingMaskError:
            without_mask += 1
        else:
            count += 1
    if count == len(friends):
        return f"Friends can go to {cafe.name}"
    if without_vaccine > 0:
        return "All friends should be vaccinated"
    if without_vaccine == 0 and without_mask > 0:
        return f"Friends should buy {without_mask} masks"
