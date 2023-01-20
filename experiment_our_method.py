
from utils.plot_map import plot_map

exp1 = ['fpn_experiments_w_recovery/collection-060922_215559/ros/ts_all_mission_2022_09_06_21h40m47s.bag']
exp2 = ['fpn_experiments_w_recovery/collection-060922_223507/ros/ts_all_mission_2022_09_06_22h26m38s.bag',
        'fpn_experiments_w_recovery/collection-060922_223548/ros/ts_all_mission_2022_09_06_22h35m49s.bag',
        'fpn_experiments_w_recovery/collection-060922_223641/ros/ts_all_mission_2022_09_06_22h36m41s.bag']
exp3 = ['fpn_experiments_w_recovery/collection-060922_225819/ros/ts_all_mission_2022_09_06_22h55m15s.bag',
        'fpn_experiments_w_recovery/collection-060922_231204/ros/ts_all_mission_2022_09_06_23h02m06s.bag']
exp4 = ['fpn_experiments_w_recovery/collection-090922_175356_m1_part1/ros/ts_all_mission_2022_09_09_17h42m17s.bag',
        'fpn_experiments_w_recovery/collection-090922_175838_m1_part2/ros/ts_all_mission_2022_09_09_17h57m04s.bag']
exp5 = ['fpn_experiments_w_recovery/collection-090922_181954_m2/ros/ts_all_mission_2022_09_09_18h03m36s.bag']
exp6 = ['fpn_experiments_w_recovery/collection-090922_202442_m3/ros/ts_all_mission_2022_09_09_20h18m54s.bag',
        'fpn_experiments_w_recovery/collection-090922_202442_m3/ros/ts_all_mission_2022_09_09_20h27m53s.bag']

experiments = [exp1, exp2, exp3, exp4, exp5, exp6]

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

        # Define parameters for plotting
        self.map_lon = [-88.2105, -88.2095]
        self.map_lat = [40.0719, 40.0721]
        self.transparency = 0.4
        self.scalebar_height = 0.35
        self.legend_columns = 5
        self.plot_recovery = True
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