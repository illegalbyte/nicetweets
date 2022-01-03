import tweepy
import matplotlib.pyplot as plt
import numpy
import filteredstream_API
# from secrets import API_KEY, API_KEY_SECRET, BEARER_TOKEN

# matplot for displaying sentiment over time
hl, = plt.plot([], [])

filteredstream_API.main()

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
    plt.draw()


update_line(hl, )