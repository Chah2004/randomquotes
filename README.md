# 💬 RandomQuotes — Random Quote Generator

**RandomQuotes** is a simple one-page web application that displays random inspirational quotes using an external API.

The project was created to demonstrate how an external **REST API can be integrated with a Django application** and used to fetch and display data dynamically.

## ✨ Features

* 💭 **Daily Quote** – Displays one random quote that remains the same throughout the day.
* 🔄 **Refresh Quote** – Allows users to generate a new random quote without reloading the page.
* 🔍 **Search by Author** – Search for an author's quotes using the search bar.
* 🎲 **Random Author Quote** – If the author exists in the API data, one random quote from that author is displayed.
* ❌ **Author Not Found** – Displays an appropriate message when no matching author is available.


## 🛠️ Technologies Used

* **HTML5** – Structure of the webpage
* **CSS3** – Custom styling
* **Bootstrap** – Responsive layout and UI components
* **Python** – Backend programming
* **Django** – Web framework and API integration
* **DummyJSON Quotes API** – Source for quote data

### 🔗 API Used

The project uses the **DummyJSON Quotes API**:

[DummyJSON Quotes API](https://dummyjson.com/quotes?utm_source=chatgpt.com)

## ⚙️ How It Works

### 📅 Daily Quote

When the website is opened, a random quote is selected and displayed.

The selected quote remains the same throughout the day, even if the user:

* Refreshes the page
* Closes and reopens the website

The quote changes automatically on the next day.

### 🔄 Refresh Quote

The **Refresh Quote** option allows the user to generate another random quote without reloading the website.

However, this refreshed quote is temporary. If the page is reloaded, the website returns to the quote selected for that day.

### 🔍 Search Author

Users can search for an author using the search bar.

* If the author exists in the available quote data → a random quote by that author is displayed.
* If the author does not exist → a **"No such author in the database"** message is displayed.

## 📂 Project Structure

```text
randomquotes/
│
├── manage.py
├── requirements.txt
│
├── randomquotes/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── app/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │ 
│   └── ...
│
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Chah2004/Quotes.git
```

### 2. Navigate to the Project

```bash
cd randomquotes
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Django Server

```bash
python manage.py runserver
```

Open the local development server in your browser.

## 🎯 Purpose

This project was developed as a small **Django and API integration project** to demonstrate:

* Working with external APIs
* Fetching and processing JSON data
* Integrating API data into a Django application
* Implementing search functionality
* Generating random results
* Handling unavailable search results
* Using Bootstrap for basic frontend design

## 🔮 Future Improvements

Possible improvements include:

* Add categories for quotes
* Add a **Copy Quote** button
* Add social media sharing
* Add favorite/bookmark functionality
* Improve the overall UI/UX
* Add animations and transitions
* Add pagination or more advanced author search
