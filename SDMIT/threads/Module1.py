#multithread using _thread module
import _thread
course={"python":7.5,"javaSE":9.1,"javaEE":9,"spring":12.5,"ccpp":3.5}


def update(key="", value=0):
    course[key] = value;
    print(course[key])
def find(ctc=0):
    for has in course.keys():
        if course[has] <= ctc:
            print(has)
def all():
    for k in course.items():
        print(k)

try:
    _thread.start_new_thread(update,('javaEE',8.0))
    _thread.start_new_thread(find,(7.5,))
    _thread.start_new_thread(update,('javaSE',7.2))
    _thread.start_new_thread(find,(5,))
except Exception as e:
    print(e)

all();