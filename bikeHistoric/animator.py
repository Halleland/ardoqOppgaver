import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from dataLoader import *

class Animator():
    '''Animates one month of station activity from historic data in the oslo region'''
    def __init__(self, filename, url):
    

        # Setup matplot
        self.fig, self.ax = plt.subplots()
        self.ani = FuncAnimation(self.fig, self.update, interval=5, init_func = self.setup_plot, blit = True)

        #Data
        self.filename = filename
        self.dataManager = DataManager(filename, url)

        # Animation
        self.lerpPercent = 0

    def setup_plot(self):
        "Inital drawing"
        x,y = self.dataManager.getCoordinates()
        s = self.nextData()
        self.scat = self.ax.scatter(x,y, s=s)

        xmin, xmax, ymin, ymax= self.dataManager.minAndMaxCoordinates()
        self.ax.axis([xmin, xmax, ymin, ymax])

        return self.scat,
    
    def update(self, i):
        s = self.nextData()
        self.scat.set_sizes(s)
        # TODO: Title/Information
        self.fig.canvas.set_window_title(self.filename+" "+str(self.dataManager.getDay()))
        return self.scat,
    
    def nextData(self):
        if self.lerpPercent == 0:
            self.dataManager.nextDay()
        sizes = self.lerpStationNumberBetweenDays(self.dataManager.prevDay, self.dataManager.currentDay, self.lerpPercent)
        self.lerpPercent += 1
        self.lerpPercent %= 100
        return np.array([3*value for value in sizes.values()])


    def lerp(self, prev,cur, percent):
        return prev + (cur - prev) * percent/100

    def lerpStationNumberBetweenDays(self, prevDay, currentDay, percent):
        lerpedDay = {}
        if prevDay is not None:
            for key, value in prevDay.items():
                lerpedDay[key] = self.lerp(value, currentDay[key], percent)
            
            return lerpedDay
        else:
            return currentDay
