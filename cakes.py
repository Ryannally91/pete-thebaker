recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
def cakes(recipe, available):
    can_make=[]
    for k, v in recipe.items():
        if k not in available.keys():
            return 0
        else:
            for key, val in available.items():
                if k == key:
                    can_make.append(int(val / v))
    num_cakes= min(can_make)
    return num_cakes
cakes(recipe, available)


#Other solutions

def cakes1(recipe, available):
      return min([available[i]//recipe[i] if i in available else 0 for i in recipe])
#// means integer division 9//2 = 4

def cakes2(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe      