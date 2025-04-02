import unittest
from src.main import createNewFolder, images_to_choose_from, search_and_populate_images, set_desktop_background
from pathlib import Path
from PIL import Image
import shutil
from unittest.mock import patch

def create_dummy_image(file_path):
        img = Image.new("RGB", (800, 1280), (255, 255, 255))
        img.save(file_path, "PNG")

class TestMain(unittest.TestCase):
    def tearDown(self):
        path = Path(str(Path.cwd()) + '\\Wallpapers')
        if path.exists():
            shutil.rmtree(str(path))

    def test_folder_creation(self):
        newFolder = createNewFolder()

        self.assertEqual(str(newFolder), str(Path.cwd()) + '\\Wallpapers')

        self.assertTrue(newFolder.is_dir())


        try: 
            createNewFolder()
        except:
            self.fail('The folder creation failed')

    def test_search_and_populate_images(self):
        newFolder = createNewFolder()

        self.assertEqual(len(images_to_choose_from), 0)

        for i in range(10):
            image_path = str(newFolder) + f"\\dummy_image_{i+1}.png"

            create_dummy_image(image_path)

        search_and_populate_images()

        self.assertEqual(len(images_to_choose_from), 10)

    @patch('ctypes.windll.user32.SystemParametersInfoW')
    @patch('random.randint')
    def test_set_desktop_background(self, mock_random, mock_system_params):
        newFolder = createNewFolder()

        mock_random.return_value = 0
        
        set_desktop_background()
        
        mock_system_params.assert_called_with(20, 0, str(newFolder) + '\\dummy_image_1.png', 0)

    @patch('ctypes.windll.user32.SystemParametersInfoW')
    def test_no_images_to_choose_from(self, mock_system_params):
        images_to_choose_from = []
        
        set_desktop_background()
        
        mock_system_params.assert_not_called()



if __name__ == '__main__':
    unittest.main()