from pyproj import Transformer
import matplotlib.pyplot as plt
import pickle
import time
from shapely.geometry import Point, Polygon

#nasze dane epsg:2180
#lon lat: epsg:4326
#OSM: EPSG:3857
#lepiej transformować EPSG 3857 na 2180 - mniej punktów

def transform_coordinates(x,y,source="epsg:2180",target ="epsg:4326" ):

    transformer = Transformer.from_crs(source, target)
    return transformer.transform(x, y)

def transformPoly(polygon,source="epsg:3857",target ="epsg:2180" ):

    transformer = Transformer.from_crs(source, target)
    poly = []
    for point in polygon:
        poly.append(transformer.transform(*point))

    return poly

#sprawdza czy punkt znajduje się w obrębie koła o srodu: centrum i promieniu: promien
def jestWkole(centrum, promien, punkt):

    if (promien**2) >= ((punkt[0]-centrum[0])**2)+((punkt[1]-centrum[1])**2):
        return True
    else:
        return False

#przeszukanie zbioru danych i wybór punktów leżących w obrębie zdefiniowanego koła
def punktyWkole(data,centrum,promien):

    # pobranie adresów promieniu R od punktu centralnego:
    adresy = []
    for i, line in enumerate(data):

        if i == 0:  # pominiecie nagłówka
            adresy.append(line)
            continue

        coord = line[8].split(' ')
        # print(i)
        if jestWkole(centrum, promien, [float(coord[0]), float(coord[1])]):
            adresy.append(line)
            print(i, ' zapisano')
    return adresy

#sprawdzenie czy punkt lezy w obrębie zdefinowanego polygonu:
#https://automating-gis-processes.github.io/CSC18/lessons/L4/point-in-polygon.html
def punktyWpolygonie(data, polygon):

    poly = Polygon(polygon)
    adresy = []
    for i, line in enumerate(data):

        if i == 0:  # pominiecie nagłówka
            adresy.append(line)
            continue

        coord = line[8].split(' ')
        p = Point(float(coord[0]), float(coord[1]))
        # print(i)
        if p.within(poly):
            adresy.append(line)
            #print(i, ' zapisano')
    return adresy

def writeCSV(adresy,path,header=True):

    for line in adresy:
        if header == False:
            continue

        csv_line = '\n'+str(line[0])+';'+str(line[1])+';'+str(line[2])+';'+str(line[3])+\
                   ';'+str(line[4])+';'+str(line[5])+';'+str(line[6])+';'+str(line[7])+';'+str(line[8])

        with open(path,'a') as file:
            file.write(csv_line)

#testowanie:
if __name__== '__main__':

    #otwarcie pliku z danymi adresowymi:
    start_time = time.time()
    data = pickle.load(open('dataPL.p', 'rb'))
    mid_time = time.time()

    #pobranie adresów w zdefiniowanym kole
    #jeśli na mapie obszar jest kołem
    #adresy = punktyWkole(data,transform_coordinates(2099926.837072454, 7281753.069288979,source="epsg:3857",target ="epsg:2180"),26662)

    #przykładowy polygon:
    coords = [
  [
    2035667.319337357,
    7339843.080204577
  ],
  [
    2031017.2571224084,
    7293765.190983722
  ],
  [
    2045812.9096245177,
    7237541.711475707
  ],
  [
    2073290.5499855778,
    7225282.456545387
  ],
  [
    2107531.917204745,
    7223591.524830861
  ],
  [
    2126977.631921803,
    7256564.693264133
  ],
  [
    2125286.7002072763,
    7292496.992197827
  ],
  [
    2096540.8610603209,
    7311519.973986253
  ],
  [
    2072022.3511996828,
    7333502.086275102
  ],
  [
    2035667.319337357,
    7339843.080204577
  ]
]

    #pobranie adresów w zdefiniowanym polygonie (z mapy). Trzeba przekazać współrzędne
    adresy = punktyWpolygonie(data,transformPoly(coords))

    #wyświetlenie info o czasie operacji
    print('1: ', mid_time-start_time,'s\t2:',time.time()-mid_time,'s')

    #zapis do pliku *csv : trzeba skasował, bo dopisuje linie:
    # writeCSV(adresy,'adresy.csv')


    # chmura punktów - przykładowa wizualizacja wybranych punktów adresowych:
    cloud = [line[8].split(' ') for line in adresy[1:]]
    cc = [(float(line[0]), float(line[1])) for line in cloud]
    x = [p for p, pp in cc]
    y = [pp for p, pp in cc]

    plt.figure()
    plt.scatter(y, x)


