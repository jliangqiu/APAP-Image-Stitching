import argparse


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.initialized = False
        self.opt = None

    def initialize(self):
        # Optimized for PyCharm Editor
        # unit image directory list
        self.parser.add_argument('--img1', type=str, default=None)
        self.parser.add_argument('--img2', type=str, default=None)
        self.parser.add_argument('--imgs', '-i', type=str, nargs='+', default=None, help='image directiory <list>')

        # root + unit directory merging (os.path.join)
        self.parser.add_argument('--imgroot', type=str, default=None, help='directory for merging')
        self.parser.add_argument('--imglist', type=str, default=None, help='merging path or absolute path txt file')

        # stitching settings
        self.parser.add_argument('--mesh_size', type=int, default=100, help='# of square matrix (local-homography mesh)')
        self.parser.add_argument('--mask_dir', type=str, default=None, help='mask image directory for carving')
        self.parser.add_argument('--mask_root', type=str, default=None, help='mask image root directory')
        self.parser.add_argument('--ransac_max', type=int, default=500, help='RANSAC MAX trial')
        self.parser.add_argument('--resize', type=int, default=(400, 300), nargs='+',
                                 help='unit resizing (width, height)')

        # print settings
        self.parser.add_argument('--print_n', type=bool, default=True, help='print <n>th process')
        self.parser.add_argument('--verbose', type=bool, default=False, help='print detail process')
        self.parser.add_argument('--warping_progress', type=bool, default=False, help='local-warping tqdm bar print')
        self.parser.add_argument('--unit_time', type=bool, default=False, help='print time spent per image')
        self.parser.add_argument('--image_show', type=int, default=0, help='# of result images to be printed, -1 show all')
        self.parser.add_argument('--match_print', type=bool, default=False, help='print feature matching image or not.')
        self.parser.add_argument('--matching_line', type=int, default=15, help='# of matching lines on matching image')
        self.parser.add_argument('--saveprint', type=bool, default=True, help='print save directory')

        # save settings
        self.parser.add_argument('--saveroot', type=str, default=None, help='save or not, save folder directory')
        self.parser.add_argument('--savename', type=str, default='out_', help='result save naming variable')
        self.parser.add_argument('--savefmt', type=str, default='jpg', help='save file extension format')

    def parse(self):
        if not self.initialized:
            self.initialize()
        self.opt = self.parser.parse_args()
        return self.opt