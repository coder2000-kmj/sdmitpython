sdm={"cse":186,"isc":178,"eee":164,"ece":145}
def admission(entry=1,cc=0,ic=0,eec=0,ec=0):
    if entry>20:
        print("cse count:",cc,"isc count:",ic,"eee count:",eec,"ece count:",ec)
        return
    else:
        dept=input("Tell us desired department: ")
        cutt=int(input("Tell us cutt off: "))
        if dept in list(sdm.keys()):
            if sdm[dept]<=(cutt) or sdm[dept]<=(cutt+5):
                print("Seat allocated @",dept)
                if dept=="cse":cc+=1;
                elif dept == "isc": ic += 1;
                elif dept == "eee": eec += 1;
                elif dept == "ece": ec += 1;
            else:print("Seat can't allocated")
        else:print(dept," not available")
        entry+=1;admission(entry,cc,ic,eec,ec);

admission()