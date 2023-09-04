from .basket import Basket

# versi pemula

# def get_basket(request):
#     basket = Basket(request)
#     return {'basket': basket}

# versi pro


def basket(request):
    return {"basket": Basket(request)}
