class Config(dict):
    def __init__(self):
        # dataset parameters
        self.root  = r'/home/andres/Documents/traversibility_paper/new_data/rgb_tests/temp'

        self.folders = [self.root + '/bag_tmp',
                        self.root + '/bag_tmp']

        self.gpslon = [-88.2272, -88.2271]
        self.gpslat = [ 40.1028,  40.10286]

        self.colorlines     = ['red', 'blue']#, 'red', 'blue']
        self.label_lines    = ['RGB only', 'RGB+Depth']#'BADGR']#, 'LiDAR', 'WayFAST (Ours)']
        self.marks          = ['solid', 'solid']