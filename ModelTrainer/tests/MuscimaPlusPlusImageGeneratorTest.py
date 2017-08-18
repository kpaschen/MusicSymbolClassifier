import os
import shutil
import unittest
from glob import glob

from datasets.MuscimaPlusPlusDatasetDownloader import MuscimaPlusPlusDatasetDownloader
from datasets.MuscimaPlusPlusImageGenerator import MuscimaPlusPlusImageGenerator


class MuscimaPlusPlusImageGeneratorTest(unittest.TestCase):
    def test_download_extract_and_render_all_symbols(self):
        # Arrange
        datasetDownloader = MuscimaPlusPlusDatasetDownloader("temp/muscima_pp_raw")

        # Act
        datasetDownloader.download_and_extract_dataset()
        image_generator = MuscimaPlusPlusImageGenerator()
        image_generator.extract_all_symbols_as_they_are("temp/muscima_pp_raw", "temp/muscima_img")
        all_image_files = [y for x in os.walk("temp/muscima_img") for y in glob(os.path.join(x[0], '*.png'))]
        actual_number_of_files = len(all_image_files)

        # Assert
        self.assertEqual(91255, actual_number_of_files)

        # Cleanup
        os.remove(datasetDownloader.get_dataset_filename())
        shutil.rmtree("temp")

    def test_download_extract_and_render_training_symbols(self):
        # Arrange
        datasetDownloader = MuscimaPlusPlusDatasetDownloader("temp/muscima_pp_raw")

        # Act
        datasetDownloader.download_and_extract_dataset()
        image_generator = MuscimaPlusPlusImageGenerator()
        image_generator.extract_symbols_for_training("temp/muscima_pp_raw", "temp/muscima_img")
        all_image_files = [y for x in os.walk("temp/muscima_img") for y in glob(os.path.join(x[0], '*.png'))]
        actual_number_of_files = len(all_image_files)

        # Assert
        self.assertEqual(55458, actual_number_of_files)

        # Cleanup
        os.remove(datasetDownloader.get_dataset_filename())
        shutil.rmtree("temp")


if __name__ == '__main__':
    unittest.main()
