class Config(dict):
    def __init__(self):
        # dataset parameters
        self.root  = r'/home/andres/Documents/traversibility_paper/new_data/rgb_tests/temp'

        self.folders = [self.root + '/bag_tmp',
                        self.root + '/bag_tmp']