import os
import math
import pandas as pd

def zeus_dlatlon2dxy(lat1, lon1, lat2, lon2):
	R = 6367300

	rlat1 = lat1*math.pi/180
	rlat2 = lat2*math.pi/180
	rlon1 = lon1*math.pi/180
	rlon2 = lon2*math.pi/180
	dlat = rlat2 - rlat1
	dlon = rlon2 - rlon1

	dx = R*dlon*math.cos(0.5*(rlat1+rlat2))
	dy = R*dlat

	return dx, dy

def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians

def import_general_log (path, n_lines_header):
    #print('import_general_log', path)
    df = []
    if os.path.isfile(path):
#        try:
        fo = open(path)
        n_hashtag_headers = 0
        hashtag_is_present = True
        while hashtag_is_present:
            l = fo.readline()
            if l[0] is '#':
                n_hashtag_headers +=1
            else:
                hashtag_is_present = False 
            
        if n_hashtag_headers > 0:
            n_lines_header = n_hashtag_headers
        df = pd.read_csv(path,  sep=",", header=n_lines_header, error_bad_lines=False, na_values=' nan')
    else:
        print('>>>>> ' + os.path.basename(path) + ' does not exist')
#        except:
#            print('Check ' + path + ' file!')
    return df 

def latlon2xy(lat, lon, zero_lat, zero_lon):    

    gps_x = [0]*len(lat)
    gps_y = [0]*len(lat)  

    for j in range(0, len(lat)):
        gps_x[j], gps_y[j] = zeus_dlatlon2dxy(zero_lat, zero_lon, lat[j], lon[j])
    
    return np.array(gps_x), np.array(gps_y)

def waypoints(csv_name):
    """ Accesses x, y, z values from waypoints from the 'path' type messages in waypoints.csv file """
    x_list = []
    y_list = []
    z_list = []
    if os.path.isfile(csv_name):
        a = pd.read_csv(csv_name)
        for index, row in enumerate(a['poses']):
            if row != '[]':
                #print(index, row.split('\n'))
                break

        b = row.rstrip('[]').lstrip('[]')

        for datapoint in b.split(','):
            data = datapoint.split('pose:')[-1].split('\n')
            for i, val in enumerate(data):
                if 'position:' in val:
                    break
            x_val = float(data[i+1].split('x:')[-1].strip(' '))
            y_val = float(data[i+2].split('y:')[-1].strip(' ')) 
            z_val = float(data[i+3].split('z:')[-1].strip(' '))
            x_list.append(x_val)
            y_list.append(y_val)
    return (x_list, y_list, z_list)

def goals(csv_name):
    a = pd.read_csv(csv_name)
    if 'data' in list(a):
        b = a['data']
        if len(b) > 0:
            data = b[0]

            goals_lat = []
            goals_lon = []

            for datapoint in data.split(','):
                lat = float(datapoint.split('latitude: ')[-1].split('\n')[0])
                lon = float(datapoint.split('longitude: ')[-1].split('\n')[0])
                goals_lat.append(lat)
                goals_lon.append(lon)
                print(lat, lon)
            zero_lat = a['zero_lat'][0]
            zero_lon = a['zero_lon'][0]
            zero_x = a['zero_x'][0]
            zero_y = a['zero_y'][0]
        
    return goals_lat, goals_lon, zero_lat, zero_lon, zero_x, zero_y