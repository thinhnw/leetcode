class RecentCounter(object):

    def __init__(self):
        self.out_of_range = 0
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        while self.out_of_range < len(self.pings):
            if t - 3000 > self.pings[self.out_of_range]:
                self.out_of_range += 1
            else:
                break
        return len(self.pings) - self.out_of_range
