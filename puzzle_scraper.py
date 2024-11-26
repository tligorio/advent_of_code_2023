import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WebScraper:
    def __init__(self, output_directory):
        self.output_directory = output_directory
        self.session = requests.Session()
        
        # Get session cookie from environment variable
        session_cookie = os.getenv('AOC_SESSION')
        if not session_cookie:
            raise ValueError("Session cookie not found in environment variables")
            
        self.session.cookies.set('session', session_cookie, domain='adventofcode.com')
        self.session.headers.update({
            'User-Agent': 'Custom Web Scraper 1.0'
        })
        self.base_url = "https://adventofcode.com/2023/day"
        
        os.makedirs(output_directory, exist_ok=True)

    def get_page_content(self, url):
        """Fetch the content of a given URL"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def get_page_title(self, soup):
        """Extract the title from between --- symbols and clean it"""
        try:
            # Find text containing "---"
            title_element = soup.find(string=lambda string: string and "---" in string)
            if title_element:
                # Extract text between "---" symbols
                raw_title = title_element.strip().split("---")[1].strip()
                logger.debug(f"Raw title: {raw_title}")
                
                # Remove special characters and punctuation (keeping alphanumeric and spaces)
                title = ''.join(c for c in raw_title if c.isalnum() or c.isspace())
                logger.debug(f"Cleaned title: {title}")
                
                # Replace spaces with underscores
                title = title.replace(' ', '_')
                logger.debug(f"Final title: {title}")
                return title
            return None
        except AttributeError as e:
            logger.error(f"Error finding title: {e}")
            return None

    def get_puzzle_input_link(self, url):
        """Generate the puzzle input link directly"""
        return f"{url}/input"

    def save_puzzle_input(self, content, title):
        """Save the puzzle input to a file"""
        if not content or not title:
            return False
        
        filepath = os.path.join(self.output_directory, f"{title}.txt")
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Saved puzzle input to {filepath}")
            return True
        except IOError as e:
            logger.error(f"Error saving file {filepath}: {e}")
            return False

    def scrape_puzzles(self, start_num=1, end_num=24):
        """Main function to scrape all puzzle inputs"""
        for num in range(start_num, end_num + 1):
            url = f"{self.base_url}/{num}"
            logger.info(f"Processing puzzle {num}")
            
            # Get main page content
            content = self.get_page_content(url)
            if not content:
                continue
            
            # Get puzzle input content directly
            puzzle_input_url = self.get_puzzle_input_link(url)
            puzzle_content = self.get_page_content(puzzle_input_url)
            
            if puzzle_content:
                # New filename format: day01_input.txt, day02_input.txt, etc.
                filename = f"day{num:02d}_input"
                self.save_puzzle_input(puzzle_content, filename)
            
            # Be nice to the server
            time.sleep(1)

if __name__ == "__main__":
    scraper = WebScraper("data")
    # Run for all days (1 to 25)
    scraper.scrape_puzzles(start_num=1, end_num=25)