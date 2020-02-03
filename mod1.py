#modules importing

import bubble
print(bubble.price)

bubble.price.reverse()
print(bubble.price)

def erase(origin=0,reach=0):
    if origin<reach:
        bubble.price.pop(origin)
        origin+=1;erase(origin,reach)
    else:
        return


erase(1,4)
print(bubble.price)
