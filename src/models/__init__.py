

def model_factory(model: str):

    if model.lower() == "user":
        from models.user import User
