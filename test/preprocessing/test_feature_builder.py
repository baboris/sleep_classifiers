from unittest import TestCase, mock

from sleep_classifiers import utils
from sleep_classifiers.preprocessing.epoch import Epoch
from sleep_classifiers.preprocessing.feature_builder import FeatureBuilder
from sleep_classifiers.preprocessing.psg.psg_service import PSGService
from sleep_classifiers.preprocessing.raw_data_processor import RawDataProcessor
from test.test_helper import TestHelper


class TestFeatureBuilder(TestCase):

    @mock.patch.object(FeatureBuilder, 'build_from_time')
    @mock.patch.object(FeatureBuilder, 'build_from_wearables')
    @mock.patch.object(FeatureBuilder, 'build_labels')
    @mock.patch.object(RawDataProcessor, 'get_valid_epochs')
    def test_builds_features(self, mock_get_valid_epochs, mock_build_labels, mock_build_from_wearables,
                             mock_build_from_time):
        subject_id = "subjectA"
        mock_get_valid_epochs.return_value = valid_epochs = [Epoch(timestamp=1, index=1000)]

        FeatureBuilder.build(subject_id)

        mock_get_valid_epochs.assert_called_once_with(subject_id)
        mock_build_labels.assert_called_once_with(subject_id, valid_epochs)
        mock_build_from_wearables.assert_called_once_with(subject_id, valid_epochs)
        mock_build_from_time.assert_called_once_with(subject_id, valid_epochs)
