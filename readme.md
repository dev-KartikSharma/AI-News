# AI News Web App

A clean and simple news aggregator web application built with Python and Flask that fetches and displays the latest articles on Artificial Intelligence and technology.

![AI News App Screenshot](https://i.imgur.com/your-screenshot-url.png)
*Note: You should replace the URL above with a link to a screenshot of your finished app.*

---

## ✨ Features

-   **Live News:** Fetches the latest AI and tech news in real-time from the NewsAPI.
-   **Clean UI:** A modern, responsive user interface built with Bootstrap 5.
-   **Secure API Handling:** Uses environment variables to securely manage API keys.
-   **Production Ready:** Includes a `gunicorn` setup for easy deployment.

---

## 🛠️ Tech Stack

-   **Backend:** Python, Flask
-   **Frontend:** HTML, Bootstrap 5
-   **API:** [NewsAPI.org](https://newsapi.org/)
-   **Deployment:** Gunicorn, Render (or any other platform)

---

## 🚀 Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dev-KartikSharma/AI-News.git](https://github.com/dev-KartikSharma/AI-News.git)
    cd AI-News
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv env
    .\env\Scripts\activate

    # For macOS/Linux
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project folder and add your NewsAPI key to it. You can get a free key from [newsapi.org](https://newsapi.org/).
    ```
    NEWS_API_KEY="your_secret_api_key_goes_here"
    ```

5.  **Run the application:**
    ```bash
    flask run
    ```
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

---

## ☁️ Deployment

This application is ready for deployment. It was successfully deployed using **Render**.

-   **Build Command:** `pip install -r requirements.txt`
-   **Start Command:** `gunicorn app:app`

Remember to set the `NEWS_API_KEY` as an environment variable in your hosting service's dashboard.