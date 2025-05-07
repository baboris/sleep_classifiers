import os

from sleep_classifiers import utils
from sleep_classifiers.constants import Constants


class CircadianService(object):

    @staticmethod
    def build_circadian_model():
        os.system(Constants.MATLAB_PATH + ' -nodisplay -nosplash -nodesktop -r \"run(\'' + str(
            utils.get_project_root()) + '/sleep_classifiers/preprocessing/time/clock_proxy/runCircadianModel.m\'); exit;\"')

    @staticmethod
    def build_circadian_mesa():
        os.system(Constants.MATLAB_PATH + ' -nodisplay -nosplash -nodesktop -r \"run(\'' + str(
            utils.get_project_root()) + '/sleep_classifiers/preprocessing/time/clock_proxy/runCircadianMESA.m\'); exit;\"')
