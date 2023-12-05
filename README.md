# Steam Review Scraper

## Overview
This Python project is designed to scrape user reviews from the Steam user reviews endpoint. It provides a simple and efficient way to retrieve reviews for a specified Steam application (game).

## Usage
To use the Steam Review Scraper, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/steam-review-scraper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd steam-review-scraper
   ```

3. Run the scraper script with the following command:
   ```bash
   python steam_review_scraper.py <appid> <num_reviews_to_retrieve>
   ```
   - `<appid>`: The Steam Application ID of the game you want to retrieve reviews for.
   - `<num_reviews_to_retrieve>`: The number of reviews to retrieve.

### Example
```bash
python steam_review_scraper.py 220 10000
```
This command will retrieve 10000 reviews for the game with the Steam Application ID 220 (Half Life 2).

## Dependencies
Make sure you have the required dependencies installed. You can install them using the following command:
```bash
pip install -r requirements.txt
```

## Notes
- Ensure that you have a stable internet connection before running the script.
- Be mindful of the Steam API usage policies and rate limits to avoid any disruptions.