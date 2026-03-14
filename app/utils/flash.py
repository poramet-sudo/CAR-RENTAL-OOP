from fastapi import Request

def set_flash(request: Request, message: str, category: str = "primary"):
    if "_messages" not in request.session:
        request.session["_messages"] = []
    request.session["_messages"].append({"message": message, "category": category})

def get_flashed_messages(request: Request):
    if "_messages" in request.session:
        return request.session.pop("_messages")
    return []