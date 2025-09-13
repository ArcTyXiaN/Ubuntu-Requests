# Ubuntu-Requests
---

# Ubuntu-Inspired Image Fetcher

> “I am because we are.”

This project was built as part of my Ubuntu-inspired assignment, where the focus is not just on coding, but on the deeper values of community, respect, and sharing.

With this script, you can fetch images from the web in a mindful and responsible way. Think of it as a little digital practice of Ubuntu — connecting to the wider web community, appreciating shared resources, and organizing them for later use.

---

## What It Does

* Lets you fetch **multiple images** at once by entering several URLs
* Creates a directory called `Fetched_Images` if it doesn’t exist
* Downloads each image and saves it with an appropriate filename
* Handles errors gracefully (because sometimes connections fail, and that’s okay)
* Asks if you trust the source before downloading, respecting your choice
* Checks HTTP headers to confirm the file is really an image and not too large
* Prevents duplicates by asking before overwriting an existing file

---

## Technologies Used

* Python (the language of choice)
* requests for fetching images
* os for managing directories and paths
* urllib.parse for handling URLs

---

## Why Ubuntu?

Ubuntu is about people. It’s about community. This project may look like a simple image downloader, but the philosophy behind it is what makes it special.

* **Community**: It connects to the global web and fetches shared resources.
* **Respect**: It won’t crash on you. It will tell you gently when something went wrong.
* **Sharing**: Every image is saved neatly in a folder, ready to be reused or shared later.
* **Practicality**: A real, working tool that serves a small but useful purpose.

---

## How to Run It

1. Clone this repo:

   ```bash
   git clone https://github.com/<your-username>/Ubuntu_Requests.git
   cd Ubuntu_Requests
   ```

2. Install requirements:

   ```bash
   pip install requests
   ```

3. Run the program:

   ```bash
   python fetch_images.py
   ```

4. Follow the prompts, trust only good sources, and watch your images get saved into `Fetched_Images/`.

---

## Example Run

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

How many images do you want to fetch? 2

Please enter the image URL: https://example.com/image1.jpg
Don't download from untrusted sources. Stay safe!
Do you trust this source? (yes/no): yes

✓ Successfully fetched: image1.jpg
✓ Image saved to Fetched_Images/image1.jpg

Please enter the image URL: https://example.com/image2.jpg
Don't download from untrusted sources. Stay safe!
Do you trust this source? (yes/no): yes
File image2.jpg already exists. Overwrite? (yes/no): no
Skipping download to avoid overwrite.
```

---

## Final Thoughts

This isn’t just about fetching images. It’s about practicing a mindset where even in something as small as coding, we can embody respect and responsibility.

The internet is a community. Let’s use it mindfully.

-
