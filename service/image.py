from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import colorsys
from colorspacious import deltaE

# import json

# 色值表
palette1 = [
    {"key": "red", "value": (255, 0, 0)},
    {"key": "yellow", "value": (255, 255, 0)},
    {"key": "blue", "value": (0, 0, 255)},
    {"key": "green", "value": (0, 128, 0)},
    {"key": "orange", "value": (255, 165, 0)},
    {"key": "cyan", "value": (0, 255, 255)},
    {"key": "magenta", "value": (255, 0, 255)},
    {"key": "purple", "value": (128, 0, 128)},
    {"key": "brown", "value": (165, 42, 42)},
]

palette2 = [
    {"key": "black", "value": (0, 0, 0)},
    {"key": "white", "value": (255, 255, 255)},
    {"key": "gray", "value": (128, 128, 128)},
]


def getFitSize(img: Image, max_size: int = 1024):
    width, height = img.size
    if width > height:
        if width > max_size:
            height = int(height * max_size / width)
            width = max_size
    else:
        if height > max_size:
            width = int(width * max_size / height)
            height = max_size
    return (width, height)


# def getDiffer(c1, c2):
#     return sum((c1[i] - c2[i]) ** 2 for i in range(3))

def getDiffer(c1, c2):
    return deltaE(np.array(c1)[:3], np.array(c2)[:3], input_space="sRGB255")


def getApproximateColor(color):
    # color = color.strip('#')
    color = [int(color[i : i + 2], 16) for i in range(0, len(color), 2)]
    color += [255]  # 添加alpha通道
    color = tuple(color)

    min_distance = 100000
    closest_color = None
    rgb = color[:3]
    hsv = colorsys.rgb_to_hsv(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
    if hsv[1] * 100 < 10:
        # 灰度色
        for pcolor in palette2:
            distance = getDiffer(pcolor["value"], color)
            if distance < min_distance:
                min_distance = distance
                closest_color = pcolor["key"]
    else:
        # 彩色
        for pcolor in palette1:
            distance = getDiffer(pcolor["value"], color)
            if distance < min_distance:
                min_distance = distance
                closest_color = pcolor["key"]
    return closest_color


def RGBhistogram(clt: KMeans):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist


def recognizeImageColor(img: Image, colorCount: int = 5):
    size = getFitSize(img)
    img = img.resize((size[0], size[1]), resample=Image.BILINEAR)

    pixels = np.array(img.convert("RGBA"))
    pixels = pixels.reshape((-1, 4))
    filter = np.array([0])
    pixels = pixels[np.isin(pixels[:, 3], filter, invert=True)]
    pixels = np.delete(pixels, np.s_[3:], 1)

    kmeans = KMeans(n_clusters=colorCount, random_state=0, n_init="auto").fit(pixels)
    cluster_centers = np.uint8(kmeans.cluster_centers_)
    # print(cluster_centers)
    hist = RGBhistogram(kmeans)
    # print(hist)
    result = []
    for i in range(len(cluster_centers)):
        color = "{:02X}{:02X}{:02X}".format(
            cluster_centers[i][0], cluster_centers[i][1], cluster_centers[i][2]
        )
        item = {
            "color": color,
            "percentage": round(hist[i], 6),
            "label": getApproximateColor(color),
        }
        result.append(item)
    result.sort(key=lambda x: x["percentage"], reverse=True)
    # print(json.dumps(result, indent=4))
    return {"colorTemplateList": result}
