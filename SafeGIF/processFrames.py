from PIL import Image, ImageSequence
import cv2
import numpy
from PIL import Image, ImageSequence
# file to extract luminance and distance from deep red from an unprocessed gif
def process_frame(frame):
    dst = frame.convert("RGB")
    avg_color_per_row = numpy.average(dst, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0) 
    distance = (256-avg_color[0])**2 + avg_color[1]**2 + avg_color[2]**2
    #from http://en.wikipedia.org/wiki/Luminance_(relative)
    relLuminance = 0.2126*avg_color[0] + 0.7152*avg_color[1] + 0.0722*avg_color[2]
    return distance, relLuminance
   
