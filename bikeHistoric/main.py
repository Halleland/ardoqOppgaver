
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from animator import *

url = "https://data.urbansharing.com/oslobysykkel.no/trips/v1/2019/05.json"
filename = "mai2019.json"
url2 = "https://data.urbansharing.com/oslobysykkel.no/trips/v1/2020/05.json"
filename2 = "mai2020.json"
a = Animator(filename, url)
b = Animator(filename2, url2)
plt.show()