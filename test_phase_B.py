import unittest
import os
from tasksB import B3, clone_git_repo, B5, B6, B7, B8, B9

class TestPhaseB(unittest.TestCase):
    def test_B3(self):
        # Test Fetch Data from an API
        url = "https://api.github.com"
        save_path = "/data/fetched_data.json"
        if os.path.exists(save_path):
            os.remove(save_path)
        result = B3(url, save_path)
        self.assertTrue(os.path.exists(save_path))
        self.assertIn("success", result["status"])

    def test_clone_git_repo(self):
        # Test Clone Git Repo and Commit
        repo_url = "https://github.com/masud450/tds_proj1_jan25"
        commit_message = "Initial commit"
        result = clone_git_repo(repo_url, commit_message)
        self.assertIn("success", result["status"])

    def test_B5(self):
        # Test SQL Query Execution
        db_path = "/data/ticket-sales.db"
        query = "SELECT SUM(units * price) FROM tickets WHERE type = 'Gold';"
        output_filename = "/data/ticket-sales-gold.txt"
        if os.path.exists(output_filename):
            os.remove(output_filename)
        result = B5(db_path, query, output_filename)
        self.assertTrue(os.path.exists(output_filename))
        self.assertIn("success", result["status"])

    def test_B6(self):
        # Test Web Scraping
        url = "https://example.com"
        output_filename = "/data/web_scraped.txt"
        if os.path.exists(output_filename):
            os.remove(output_filename)
        result = B6(url, output_filename)
        self.assertTrue(os.path.exists(output_filename))

    def test_B7(self):
        # Test Image Processing
        image_path = "/data/sample_image.png"
        output_path = "/data/resized_image.png"
        resize = (100, 100)
        result = B7(image_path, output_path, resize)
        self.assertTrue(os.path.exists(output_path))

    def B8(audio_path, output_path):
     import openai
     if not B12(audio_path):
        return None
     with open(audio_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
     with open(output_path, 'w') as file:
        file.write(transcription)
     return {
        "status": "success",
        "message": "Transcription saved",
        "transcription": transcription
     }


    def test_B9(self):
        # Test Markdown to HTML Conversion
        md_path = "/data/format.md"
        output_path = "/data/formta.html"
        if os.path.exists(output_path):
            os.remove(output_path)
        result = B9(md_path, output_path)
        self.assertTrue(os.path.exists(output_path))

if __name__ == "__main__":
    unittest.main()
