import requests
import os
from urllib.parse import urlparse


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get number of images from user
    counter = int(input("How many images do you want to fetch? "))

    for i in range(counter):
        url = input("\nPlease enter the image URL: ")

        print("\nDon't download from untrusted sources. Stay safe!")

        trust = input("Do you trust this source? (yes/no): ").strip().lower()
        if trust != "yes":
            print("✗ Source not trusted. Skipping download.")
            continue  # go to the next image in the loop

        print(f"\nAttempting to fetch image from: {url}")

        try:
            # Create directory if it doesn't exist
            os.makedirs("Fetched_Images", exist_ok=True)

            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # -------------------------------
            #HTTP header checks
            # -------------------------------
            content_type = response.headers.get("Content-Type", "")
            if "image" not in content_type:
                print(f"✗ Not an image file (Content-Type: {content_type}). Skipping.")
                continue

            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > 5 * 1024 * 1024:  # > 5 MB
                print(f"✗ File too large ({int(content_length) / 1024:.1f} KB). Skipping.")
                continue
            # -------------------------------

            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename:
                filename = "downloaded_image.jpg"

            # Save the path
            filepath = os.path.join("Fetched_Images", filename)

            # check if file already exists
            if os.path.exists(filepath):
                choice = input(f"File {filename} already exists. Overwrite? (yes/no): ").strip().lower()
                if choice != "yes":
                    print(" Skipping download to avoid overwrite.")
                    continue

            # Save the image
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("\nConnection strengthened. Community enriched.")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")


if __name__ == "__main__":
    main()
