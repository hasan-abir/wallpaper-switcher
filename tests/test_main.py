import unittest
from src.main import createNewFolder, images_to_choose_from, search_and_populate_images, set_desktop_background, randomizeImage
from pathlib import Path
from PIL import Image
import shutil
from unittest.mock import patch, MagicMock
import winreg

def create_dummy_image(file_path):
        img = Image.new("RGB", (800, 1280), (255, 255, 255))
        img.save(file_path, "PNG")

class TestMain(unittest.TestCase):
    def tearDown(self):
        path = Path(str(Path.cwd()) + '\\Wallpapers')
        if path.exists():
            images_to_choose_from.clear()
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

    def test_randomize_image(self):
        newFolder = createNewFolder()

        for i in range(10):
            image_path = str(newFolder) + f"\\dummy_image_{i+1}.png"

            create_dummy_image(image_path)

        search_and_populate_images()

        image_chosen = randomizeImage()

        self.assertTrue(image_chosen.endswith('.png'))

    @patch('random.randint')
    @patch('ctypes.windll.user32.SystemParametersInfoW')
    @patch("winreg.CloseKey")
    @patch("winreg.SetValueEx")
    @patch("winreg.QueryValueEx")
    @patch("winreg.OpenKey")
    def test_set_desktop_background(self, mock_openkey, mock_queryvalueex, mock_setvalueex, mock_closekey, mock_system_params,  mock_random):
        newFolder = createNewFolder()
        for i in range(10):
            image_path = str(newFolder) + f"\\dummy_image_{i+1}.png"

            create_dummy_image(image_path)

        search_and_populate_images()


        mock_key = MagicMock()
        mock_openkey.return_value = mock_key
        mock_random.return_value = 0
        
        set_desktop_background()

        image_path = str(newFolder) + '\\dummy_image_1.png'
        
        mock_system_params.assert_called_with(20, 0, image_path, 0)
        mock_openkey.assert_called_with(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_SET_VALUE)
        mock_setvalueex.assert_called_once_with(mock_key, "Wallpaper", 0, winreg.REG_SZ, image_path)
        mock_closekey.assert_called_once_with(mock_key)

    @patch('ctypes.windll.user32.SystemParametersInfoW')
    def test_no_images_to_choose_from(self, mock_system_params):
        images_to_choose_from = []
        
        set_desktop_background()
        
        mock_system_params.assert_not_called()



if __name__ == '__main__':
    unittest.main()