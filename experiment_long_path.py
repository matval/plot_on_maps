
from utils.plot_map import plot_map

exp1 = ['fpn_experiment_long_path/collection-080922_212651/ros/ts_all_mission_2022_09_08_20h52m20s.bag']
exp2 = ['2022-09-07/collection-070922_213530/ros/ts_all_mission_2022_09_07_21h31m19s.bag',
        '2022-09-07/collection-070922_220658/ros/ts_all_mission_2022_09_07_21h38m20s.bag']

experiments = [exp2]

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
        self.scalebar_height = 0.4
        self.legend_columns = 5
        self.plot_recovery = True
        self.plot_intervention = True
        self.multiple_runs = False

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