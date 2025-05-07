from sleep_classifiers import utils
from pathlib import Path


class Constants(object):
    # WAKE_THRESHOLD = 0.3  # These values were used for scikit-learn 0.20.3, See:
    # REM_THRESHOLD = 0.35  # https://scikit-learn.org/stable/whats_new.html#version-0-21-0
    WAKE_THRESHOLD = 0.5  #
    REM_THRESHOLD = 0.35

    INCLUDE_CIRCADIAN = False
    EPOCH_DURATION_IN_SECONDS = 30
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_DAY = 3600 * 24
    SECONDS_PER_HOUR = 3600
    VERBOSE = True
    DATA_PATH = Path('/Users/bboris/fs/projects/edu/msc_thesis_p/data/motion-and-heart-rate-from-a-wrist-worn-wearable-and-labeled-sleep-from-polysomnography-1.0.0')
    OUTPUT_PATH = Path('/Users/bboris/fs/projects/edu/msc_thesis_p/data/aw_dataset')
    CROPPED_FILE_PATH = OUTPUT_PATH / 'cropped/'
    FEATURE_FILE_PATH = OUTPUT_PATH / 'features/'
    FIGURE_FILE_PATH = OUTPUT_PATH / 'figures/'
    LOWER_BOUND = -0.2
    MATLAB_PATH = '/Applications/MATLAB_R2019a.app/bin/matlab'  # Replace with your MATLAB path
