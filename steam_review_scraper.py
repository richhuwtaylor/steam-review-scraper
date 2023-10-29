import requests
import csv
from datetime import datetime

def scrape_steam_reviews(appid, num_reviews_to_retrieve=20):
    if not appid:
        raise ValueError("AppID is not supplied.")

    cursor = '*'
    reviews = []

    while num_reviews_to_retrieve > 0:
        reviews_url = f"https://store.steampowered.com/appreviews/{appid}?json=1&filter=recent"
        try:
            response = requests.get(reviews_url, params={'cursor': cursor})
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            break
        except ValueError as e:
            print(f"Failed to parse JSON: {e}")
            break

        if data.get("success") != 1:
            print("Error: Unable to retrieve data.")
            break

        num_reviews_on_page = data['query_summary']['num_reviews']
        reviews += data['reviews']

        if num_reviews_on_page == 0 or data['cursor'] == "":
            break

        num_reviews_to_retrieve -= num_reviews_on_page
        cursor = data['cursor']

    if reviews:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        flattened_reviews = []
        for review in reviews:
            author_info = review.pop('author')
            review.update(author_info)
            flattened_reviews.append(review)

        filename = f"steam_reviews_{appid}_{current_time}.csv"
        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=flattened_reviews[0].keys())
            writer.writeheader()
            writer.writerows(flattened_reviews)

        print(f"Scraped {len(reviews)} reviews and saved to {filename}")
    else:
        print("No reviews were scraped")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python steam_reviews_module.py <appid> <num_reviews_to_retrieve>")
    else:
        appid = sys.argv[1]
        num_reviews_to_retrieve = int(sys.argv[2])
        scrape_steam_reviews(appid, num_reviews_to_retrieve)