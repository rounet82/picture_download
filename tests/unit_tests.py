import pytest
from unittest.mock import Mock, patch, MagicMock
from picture_download.main import download_picture


class TestDownloadPictureAPICalls:
    """Test suite to verify that download_picture calls the correct APIs"""

    @patch('picture_download.main.requests.get')
    @patch('picture_download.main.sqlite3.connect')
    @patch('picture_download.main.os.path.exists')
    @patch('picture_download.main.os.makedirs')
    @patch('picture_download.main.os.remove')
    def test_download_picture_calls_cat_api(self, mock_remove, mock_makedirs, mock_exists, 
                                            mock_db_connect, mock_requests_get):
        """Verify that download_picture calls the cat API endpoint"""
        # Setup mocks
        mock_exists.return_value = True
        mock_response = MagicMock()
        mock_response.content = b'fake_image_data'
        mock_requests_get.return_value = mock_response
        mock_cursor = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_db_connect.return_value = mock_conn

        # Execute
        result = download_picture(item_id="cat", q=1)

        # Verify
        mock_requests_get.assert_called_once_with("https://placekittens.com/200/300")
        assert result == {"message": "Picture(s) downloaded"}

    @patch('picture_download.main.requests.get')
    @patch('picture_download.main.sqlite3.connect')
    @patch('picture_download.main.os.path.exists')
    @patch('picture_download.main.os.makedirs')
    @patch('picture_download.main.os.remove')
    def test_download_picture_calls_dog_api(self, mock_remove, mock_makedirs, mock_exists,
                                            mock_db_connect, mock_requests_get):
        """Verify that download_picture calls the dog API endpoint"""
        # Setup mocks
        mock_exists.return_value = True
        mock_response = MagicMock()
        mock_response.content = b'fake_image_data'
        mock_requests_get.return_value = mock_response
        mock_cursor = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_db_connect.return_value = mock_conn

        # Execute
        result = download_picture(item_id="dog", q=1)

        # Verify
        mock_requests_get.assert_called_once_with("https://place.dog/300/200")
        assert result == {"message": "Picture(s) downloaded"}

    @patch('picture_download.main.requests.get')
    @patch('picture_download.main.sqlite3.connect')
    @patch('picture_download.main.os.path.exists')
    @patch('picture_download.main.os.makedirs')
    @patch('picture_download.main.os.remove')
    @patch('picture_download.main.random.randint')
    def test_download_picture_calls_fox_api(self, mock_randint, mock_remove, mock_makedirs,
                                            mock_exists, mock_db_connect, mock_requests_get):
        """Verify that download_picture calls the fox API endpoint with correct URL format"""
        # Setup mocks
        mock_exists.return_value = True
        mock_randint.return_value = 42
        mock_response = MagicMock()
        mock_response.content = b'fake_image_data'
        mock_requests_get.return_value = mock_response
        mock_cursor = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_db_connect.return_value = mock_conn

        # Execute
        result = download_picture(item_id="fox", q=1)

        # Verify
        mock_requests_get.assert_called_once_with("https://randomfox.ca/images/42.jpg")
        assert result == {"message": "Picture(s) downloaded"}

    def test_download_picture_invalid_item_id_returns_error(self):
        """Verify that download_picture returns error for invalid item_id without calling APIs"""
        # Execute
        result = download_picture(item_id="invalid", q=1)

        # Verify
        assert result == 'Item not found'
