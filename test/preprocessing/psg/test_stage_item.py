from unittest import TestCase

from sleep_classifiers.preprocessing.epoch import Epoch
from sleep_classifiers.preprocessing.psg.stage_item import StageItem
from sleep_classifiers.sleep_stage import SleepStage


class TestStageItem(TestCase):

    def test_constructor(self):
        stage = SleepStage.rem
        epoch_time = 3
        epoch_index = 4
        stage_item = StageItem(Epoch(timestamp=epoch_time, index=epoch_index), stage=stage)
        self.assertEqual(stage, stage_item.stage)
        self.assertEqual(epoch_time, stage_item.epoch.timestamp)
        self.assertEqual(epoch_index, stage_item.epoch.index)
