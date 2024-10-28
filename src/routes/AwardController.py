from flask import Blueprint, make_response, Response, jsonify, request
from src.models.dto.AwardDto import AwardSchema
from src.services.AwardService import AwardService

simple_page = Blueprint('simple_page', __name__)

@simple_page.route('', methods=["POST"])
def Post() -> Response:
    award_schema = AwardSchema()
    award_data = request.json
    validated_data = award_schema.load(award_data)
    award_service = AwardService()
    new_award = award_service.create(validated_data)
    return new_award


@simple_page.route('<int:id>', methods=["DELETE"])
def Delete(id: int) -> Response:
    award_service = AwardService()
    result = award_service.delete(id)
    return result.__str__()

@simple_page.route('<int:id>', methods=["PUT"])
def Put(id: int) -> Response:
    award_schema = AwardSchema()
    award_data = request.json
    validated_data = award_schema.load(award_data)
    award_service = AwardService()
    result = award_service.update(id, validated_data)
    return result.__str__()


@simple_page.route('', methods=["GET"])
def Get() -> Response:
    award_service = AwardService()
    awards = award_service.get_all()
    return awards
