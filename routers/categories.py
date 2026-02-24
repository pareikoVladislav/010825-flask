from flask import Blueprint, jsonify, request
from sqlalchemy import select
from pydantic import ValidationError

from core.db import db
from models import Category
from schemas.questions import CategoryBase, CategoryCreateRequest

categories_bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/categories"
)


@categories_bp.route("", methods=["GET"])
def get_all_categories():
    stmt = select(Category)
    categories = db.session.execute(stmt).scalars().all()

    response = [
        CategoryBase.model_validate(cat).model_dump()
        for cat in categories
    ]
    return jsonify(response), 200


@categories_bp.route("", methods=["POST"])
def create_category():
    raw_data = request.get_json(silent=True)

    if not raw_data:
        return jsonify({"error": "Request body is missing or not valid JSON"}), 400

    try:
        validated = CategoryCreateRequest.model_validate(raw_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    try:
        category = Category(**validated.model_dump())
        db.session.add(category)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create category", "detail": str(e)}), 500

    return jsonify(CategoryBase.model_validate(category).model_dump()), 201


@categories_bp.route("/<int:category_id>", methods=["PUT"])
def update_category(category_id: int):
    raw_data = request.get_json(silent=True)

    if not raw_data:
        return jsonify({"error": "Request body is missing or not valid JSON"}), 400

    try:
        validated = CategoryCreateRequest.model_validate(raw_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    stmt = select(Category).where(Category.id == category_id)
    category = db.session.execute(stmt).scalars().one_or_none()

    if not category:
        return jsonify({"error": f"Category with ID {category_id} not found"}), 404

    try:
        category.name = validated.name
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update category", "detail": str(e)}), 500

    return jsonify(CategoryBase.model_validate(category).model_dump()), 200


@categories_bp.route("/<int:category_id>", methods=["DELETE"])
def delete_category(category_id: int):
    stmt = select(Category).where(Category.id == category_id)
    category = db.session.execute(stmt).scalars().one_or_none()

    if not category:
        return jsonify({"error": f"Category with ID {category_id} not found"}), 404

    try:
        db.session.delete(category)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to delete category", "detail": str(e)}), 500

    return jsonify({"message": f"Category with ID {category_id} deleted successfully"}), 200