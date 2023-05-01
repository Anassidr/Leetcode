# pop function removes the last item from the list and returns its value

class Solution:
    def isValid(self, s: str) -> bool:
        track = []
        sdict = {"{":"}", "(":")", "[":"]"}
        for x in s:
            if x in sdict:
                track.append(x)
            elif track == [] or sdict[track.pop()] != x:
                return False
        return track == []
