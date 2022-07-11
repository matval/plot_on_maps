#!/usr/bin/env python3
import os
import sys
import matplotlib.pyplot as plt
import math
from salem import GoogleVisibleMap, Map
from utils import zeus_dlatlon2dxy, euler_from_quaternion, import_general_log, latlon2xy, waypoints, goals
from config import Config

libraries = [os.path.abspath('libraries/import_data'), 
             os.path.abspath('libraries/ros_utils'), \
             os.path.abspath('libraries/ros_utils/dist_packages'), \
             os.path.abspath('libraries/utils_hiro'), \
             os.path.abspath('functions')]

for lib in libraries:
    if lib not in sys.path:
        sys.path.append(lib)

configs = Config()

ekf_x_all = []
ekf_y_all = []
ekf_yaw_all = []
gps_lat_all = []
gps_lon_all = []
hor_acc_all = []
goals_x_all = []
goals_y_all = []
goals_lat_all = []
goals_lon_all = []
waypoint_x_all = []
waypoint_y_all = []
waypoint_z_all = []
gps_x_all = []
gps_y_all = []
imu_yaw_all = []

for name_folder in configs.folders:

    folder = os.listdir(name_folder)
    print('FOLDERS: ', folder)
    ekf_x_total = []
    ekf_y_total = []
    ekf_yaw_total = []
    gps_lat_total = []
    gps_lon_total = []
    hor_acc_total = []
    goals_x_total = []
    goals_y_total = []
    goals_lat_total = []
    goals_lon_total = []
    waypoint_x_total = []
    waypoint_y_total = []
    waypoint_z_total = []
    gps_x_total = []
    gps_y_total = []
    imu_yaw_total = []
    
    for k in range(0,len(configs.folders)):
        csv_location_general = os.path.join(name_folder,folder[k])
        print(csv_location_general)
        ekf_out_general = import_general_log(os.path.join(csv_location_general, 'terrasentia-ekf.csv'),0)
        ekf_x1 = ekf_out_general['pose.pose.position.x']
        ekf_y1= ekf_out_general['pose.pose.position.y']
        ekf_yaw1 = []
        for i, x in enumerate(ekf_out_general['pose.pose.orientation.x']):
            y1 = ekf_out_general['pose.pose.orientation.x'][i]
            z1 = ekf_out_general['pose.pose.orientation.z'][i]
            w1 = ekf_out_general['pose.pose.orientation.w'][i]
            roll1, pitch1, yaw1 = euler_from_quaternion(x,y1,z1,w1)
            ekf_yaw1.append(yaw1*180/math.pi)
        ekf_x_total.append(ekf_x1)
        ekf_y_total.append(ekf_y1)
        ekf_yaw_total.append(ekf_yaw1)
        gps_out_general = import_general_log(os.path.join(csv_location_general, 'terrasentia-full_gps.csv'),0) 
        #gps_ts = np.array(gps_out['Time'])
        #gps_ts -= t0
        gps_lat1 = gps_out_general['latitude']
        gps_lon1 = gps_out_general['longitude']
        hor_acc1 = gps_out_general['horizontal_accuracy']
        gps_lat_total.append(gps_lat1)
        gps_lon_total.append(gps_lon1)
        hor_acc_total.append(hor_acc1)
        goals_lat1, goals_lon1, zero_lat1, zero_lon1, zero_x1, zero_y1 = goals(os.path.join(csv_location_general, 'terrasentia-goals.csv'))
        goals_x1 = [0]*len(goals_lat1)
        goals_y1 = [0]*len(goals_lon1)
        for i in range(0, len(goals_lat1)):
            goals_x1[i], goals_y1[i] = zeus_dlatlon2dxy(zero_lat1, zero_lon1, goals_lat1[i], goals_lon1[i])
            goals_x1[i] += zero_x1
            goals_y1[i] += zero_y1
        goals_x_total.append(goals_x1)
        goals_y_total.append(goals_y1)
        goals_lat_total.append(goals_lat1)
        goals_lon_total.append(goals_lon1)
        waypoint_x1, waypoint_y1, waypoint_z1 = waypoints(os.path.join(csv_location_general, 'terrasentia-waypoints.csv'))
        gps_x1, gps_y1 = latlon2xy(gps_lat1, gps_lon1, zero_lat1, zero_lon1)
        waypoint_x_total.append(waypoint_x1)
        waypoint_y_total.append(waypoint_y1)
        waypoint_z_total.append(waypoint_z1)
        gps_x_total.append(gps_x1)
        gps_y_total.append(gps_y1)
        imu_out1 = import_general_log(os.path.join(csv_location_general, 'terrasentia-imu.csv'),0)
        #imu_ts = np.array(imu_out['Time'])
        #imu_ts == t0
        imu_yaw1 = []
        for i, x in enumerate(imu_out1['orientation.x']):
            y1 = imu_out1['orientation.x'][i]
            z1 = imu_out1['orientation.z'][i]
            w1 = imu_out1['orientation.w'][i]
            roll1, pitch1, yaw1 = euler_from_quaternion(x,y1,z1,w1)
            imu_yaw1.append(yaw1*180/math.pi)
        imu_yaw_total.append(imu_yaw1)
    ekf_x_all.append(ekf_x_total)
    ekf_y_all.append(ekf_y_total)
    ekf_yaw_all.append(ekf_yaw_total)
    gps_lat_all.append(gps_lat_total)
    gps_lon_all.append(gps_lon_total)
    hor_acc_all.append(hor_acc_total)
    goals_x_all.append(goals_x_total)
    goals_y_all.append(goals_y_total)
    goals_lat_all.append(goals_lat_total)
    goals_lon_all.append(goals_lon_total)
    waypoint_x_all.append(waypoint_x_total)
    waypoint_y_all.append(waypoint_y_total)
    waypoint_z_all.append(waypoint_z_total)
    gps_x_all.append(gps_x_total)
    gps_y_all.append(gps_y_total)
    imu_yaw_all.append(imu_yaw_total)

print('Len_ekfffffffffffffffffffffffffffff: ', len(ekf_x_total))

plt.close('all')

gpslon = [-88.2272, -88.2271]
gpslat = [40.1028, 40.10286]

g = GoogleVisibleMap(gpslon,gpslat, size_x=640, size_y=640, scale=1, maptype='satellite')  # try out also: 'terrain'
plt.figure(figsize=[10,6])

# the google static image is a standard rgb image
ggl_img = g.get_vardata()
plt.imshow(ggl_img)


sm = Map(g.grid, factor=1, countries=False)
sm.set_rgb(ggl_img)
f, ax1 = plt.subplots(1, 1, figsize=(10, 6))
sm.visualize(ax = ax1)

colorlines = ['red', 'blue']#, 'red', 'blue']
label_lines = ['RGB only', 'RGB+Depth']#'BADGR']#, 'LiDAR', 'WayFAST (Ours)']
mar2 = ['solid', 'solid']


for i in range(0,len(configs.folders)):
    print('LENFOLDER:', len(gps_lon_all[i]))
    print('STEPI: ', i)
    gpslontotal = gps_lon_all[i]
    gpslattotal = gps_lat_all[i]
    for k in range(0,len(gpslontotal)):
        print('STEPK: ',k)
        print(len(gps_lon_total))
        gpslt = []
        gpslot = []
        for j in range(0, len(gpslontotal[k])):
            if j==0 and k==0:
                x_init, y_init = sm.grid.transform((gps_lon_total[k])[j]+0.00000, (gps_lat_total[k])[j]-0.00000)
                if i == 0:
                    ax1.scatter(x_init, y_init, s=30, c ="yellow", marker="o",label = 'Initial Points' )
                else:
                    ax1.scatter(x_init, y_init, s=30, c ="yellow", marker="o")
            elif j==0 and k!=0:
                x_init, y_init = sm.grid.transform((gps_lon_total[k])[j]+0.00000, (gps_lat_total[k])[j]-0.00000)
                ax1.scatter(x_init, y_init, s=30, c ="yellow", marker="o")
            gpslt.append((gpslattotal[k])[j]-0.00000)
            gpslot.append((gpslontotal[k])[j]+0.00000)
        #x, y = sm.grid.transform(gpslontotal[k], gpslattotal[k])
        x, y = sm.grid.transform(gpslot, gpslt)
        if k == 0:
            ax1.plot(x,y, linestyle = mar2[i],color = colorlines[i],label = label_lines[i])
            #ax1.scatter(x, y, s=1, c = colorlines[i], linewidths=0.5, label = label_lines[i])
        else:
            ax1.plot(x,y, linestyle = mar2[i],color = colorlines[i])
            #ax1.scatter(x, y, s=1, c = colorlines[i], linewidths=0.5)
        #x_init, y_init = sm.grid.transform((gpslontotal[k])[0], (gpslattotal[k])[0])
        #ax1.scatter(x_init, y_init, s=80, c ="yellow", marker="o" )
    
print((goals_lon_total[0])[0])
print((goals_lat_total[0])[0])

x_goal, y_goal = sm.grid.transform((goals_lon_total[0])[0]+0.00000, (goals_lat_total[0])[0]-0.00000)
ax1.plot(x_goal, y_goal, color = "cyan", marker = "*", label = 'Goal', markersize=15)
#ax1.scatter(x_goal, y_goal, s=60, c ="cyan", marker="*", label = 'Goal' )

lgnd = ax1.legend(loc="lower right",prop={'size': 15})

lgnd.legendHandles[0]._sizes = [60]
#lgnd.legendHandles[1]._sizes = [60]
#lgnd.legendHandles[2]._sizes = [60]
#lgnd.legendHandles[3]._sizes = [60]
#ax1.set_xticklabels(['', ''])
ax1.set_xlabel('Longitude', fontsize = 14)
ax1.set_ylabel('Latitude', fontsize = 14)

plt.show()