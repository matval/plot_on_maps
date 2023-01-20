
from utils.plot_map import plot_map

exp1 = ['fpn_experiments_wo_recovery/2022-08-30-wps/collection-300822_220556_m4_complete/ros/ts_all_mission_2022_08_30_21h52m23s.bag']
# exp2 = ['fpn_experiments_wo_recovery/2022-08-30-wps/collection-300822_230410_m7/ros/ts_all_mission_2022_08_30_23h01m29s.bag',
#         'fpn_experiments_wo_recovery/2022-08-30-wps/collection-300822_230450_m7_m8/ros/ts_all_mission_2022_08_30_23h04m50s.bag',
#         'fpn_experiments_wo_recovery/2022-08-30-wps/collection-300822_230450_m7_m8/ros/ts_all_mission_2022_08_30_23h12m10s.bag',
#         'fpn_experiments_wo_recovery/2022-08-30-wps/collection-300822_230450_m7_m8/ros/ts_all_mission_2022_08_30_23h12m25s.bag']
exp3 = ['fpn_experiments_wo_recovery/2022-08-30-wps/collection-300822_230450_m7_m8/ros/ts_all_mission_2022_08_30_23h18m08s.bag',
        'fpn_experiments_wo_recovery/2022-08-30-wps/collection-300822_230450_m7_m8/ros/ts_all_mission_2022_08_30_23h23m48s.bag',
        'fpn_experiments_wo_recovery/2022-08-30-wps/collection-300822_230450_m7_m8/ros/ts_all_mission_2022_08_30_23h27m13s.bag']
exp4 = ['fpn_experiments_wo_recovery/2022-09-01/collection-010922_212741/ros/ts_all_mission_2022_09_01_21h24m46s.bag',
        'fpn_experiments_wo_recovery/2022-09-01/collection-010922_214022/ros/ts_all_mission_2022_09_01_21h30m53s.bag']
exp5 = ['fpn_experiments_wo_recovery/2022-09-01/collection-010922_221612/ros/ts_all_mission_2022_09_01_22h10m37s.bag',
        'fpn_experiments_wo_recovery/2022-09-01/collection-010922_221718/ros/ts_all_mission_2022_09_01_22h17m19s.bag',
        'fpn_experiments_wo_recovery/2022-09-01/collection-010922_221746/ros/ts_all_mission_2022_09_01_22h17m46s.bag',
        'fpn_experiments_wo_recovery/2022-09-01/collection-010922_221833/ros/ts_all_mission_2022_09_01_22h18m33s.bag',
        'fpn_experiments_wo_recovery/2022-09-01/collection-010922_222147/ros/ts_all_mission_2022_09_01_22h19m02s.bag',
        'fpn_experiments_wo_recovery/2022-09-01/collection-010922_222242/ros/ts_all_mission_2022_09_01_22h22m42s.bag',
        'fpn_experiments_wo_recovery/2022-09-01/collection-010922_222308/ros/ts_all_mission_2022_09_01_22h23m08s.bag']
exp6 = ['fpn_experiments_wo_recovery/2022-09-01/collection-010922_223757/ros/ts_all_mission_2022_09_01_22h29m12s.bag',
        'fpn_experiments_wo_recovery/2022-09-01/collection-010922_224414/ros/ts_all_mission_2022_09_01_22h39m55s.bag']

experiments = [exp1, exp3, exp4, exp5, exp6]

class Config:
    def __init__(self):
        self.data_dir = r'/media/mateus/1336a09b-baca-4722-85f3-3f7f6884754d/fpn_2022'

        # Define parameters for data extraction
        self.start_after        = 0            # Start getting data after some seconds

        # Define topics for data extraction
        self.odom_topic         = "/terrasentia/ekf"
        self.mhe_topic          = "/terrasentia/mhe_output"
        self.gps_topic          = "/terrasentia/full_gps"
        self.collision_topic    = "/terrasentia/is_collision_mhe"
        self.goals_topic        = "/terrasentia/wp_follow_goals"

        # Define parameters for plotting
        self.map_lon = [-88.2105, -88.2095]
        self.map_lat = [40.0719, 40.0721]
        self.transparency = 0.4
        self.scalebar_height = 0.35
        self.legend_columns = 4
        self.plot_recovery = False
        self.multiple_runs = True

# Load config parameters
configs = Config()

# collections_list = []
# for root, dirs, files in os.walk(configs.data_dir):
#     bags_list = []
#     dirs.sort()
#     for file in files:
#         if file.startswith("ts_all_mission") and file.endswith(".bag"):
#             bags_list.append(os.path.join(root, file))

#     if len(bags_list) > 0:
#         collections_list.append(bags_list)

# del bags_list

# print('len(collections_list):', len(collections_list))

plot_map(configs, experiments)