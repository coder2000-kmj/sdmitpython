class ViswanathError(RuntimeError):
    def __init__(self,msg="ViswanathError occurs due to invalid data"):
        self.msg=msg