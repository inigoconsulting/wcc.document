from plone.jsonapi.routes import add_plone_route

# CRUD
from plone.jsonapi.routes.api import get_items
from plone.jsonapi.routes.api import create_items
from plone.jsonapi.routes.api import update_items
from plone.jsonapi.routes.api import delete_items

from plone.jsonapi.routes.api import url_for

# GET
@add_plone_route("/wccdocuments", "wccdocuments", methods=["GET"])
@add_plone_route("/wccdocuments/<string:uid>", "wccdocuments", methods=["GET"])
def get(context, request, uid=None):
    """ get wccdocuments
    """
    items = get_items("wcc.document.document", request, uid=uid, endpoint="wccdocuments")
    return {                       
        "url": url_for("wccdocuments"),   
        "count": len(items),       
        "items": items,
    }

# CREATE
@add_plone_route("/wccdocuments/create", "wccdocuments_create", methods=["POST"])
@add_plone_route("/wccdocuments/create/<string:uid>", "wccdocuments_create", methods=["POST"])
def create(context, request, uid=None):
    """ create wccdocuments
    """
    items = create_items("wcc.document.document", request, uid=uid, endpoint="wccdocuments")
    return {
        "url": url_for("wccdocuments_create"),
        "count": len(items),
        "items": items,
    }


# UPDATE
@add_plone_route("/wccdocuments/update", "wccdocuments_update", methods=["POST"])
@add_plone_route("/wccdocuments/update/<string:uid>", "wccdocuments_update", methods=["POST"])
def update(context, request, uid=None):
    """ update wccdocuments
    """
    items = update_items("wcc.document.document", request, uid=uid, endpoint="wccdocuments")
    return {
        "url": url_for("wccdocuments_update"),
        "count": len(items),
        "items": items,
    }


# DELETE
@add_plone_route("/wccdocuments/delete", "wccdocuments_delete", methods=["POST"])
@add_plone_route("/wccdocuments/delete/<string:uid>", "wccdocuments_delete", methods=["POST"])
def delete(context, request, uid=None):
    """ delete wccdocuments
    """
    items = delete_items("wcc.document.document", request, uid=uid, endpoint="wccdocuments")
    return {
        "url": url_for("wccdocuments_delete"),
        "count": len(items),
        "items": items,
    }

