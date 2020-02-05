class ViswanathError(RuntimeError):
    def __init__(self,msg="ViswanathError occurs due to invalid data"):
        self.msg=msg
ctc=[4.5,9.2,5.6,12.5,3.7,1.9,12.3]

try:
    desired = float(input("Tell us data wish to search"))
    if desired in ctc:print(ctc.index(desired))
    else:raise ViswanathError;
except ViswanathError as verror:
    print(verror.msg)
    desired = float(input("Tell us data wish to search"))
    if desired in ctc:print(ctc.index(desired))