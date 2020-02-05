#hybrid
from inher2 import dlithe
from inher1 import candidate,org

class campus(dlithe,org):
    people=['Mohamed','sabari']


c1=campus();c1.name=c1.people[0];c1+'java';c1.addMore();
print(c1)
c2=campus();c2.name=c2.people[1];c2+'c';c2.addMore();print(c2)
