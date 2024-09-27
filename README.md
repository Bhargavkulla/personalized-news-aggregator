# Personalized News Aggregator API Documentation

## Overview
This API serves as a news aggregator that scrapes articles from various sources, categorizes them, and provides access through a RESTful interface.

## Base URL
http://127.0.0.1:5000/api

## Endpoints

### 1. Retrieve All Articles
- **Endpoint**: `/articles`
- **Method**: `GET`
- **Description**: Fetches all articles from the database.
- **Response**:
    ```json
    [
        {
            "category": "Health",
            "id": 1,
            "published_at": "2024-09-27",
            "source": "BBC",
            "summary": "More than 600 people have been killed by Israeli airstrikes in Lebanon since Monday, health officials say.",
            "title": "Israel striking Hezbollah with ‘full force’ despite ceasefire calls",
            "url": "http://example.com/article1"
        },
        ...
    ]
    ```
- **Screenshots**:
    ![Retrieve All Articles](screenshots/Screenshot%20(19).png)

### 2. Retrieve Specific Article
- **Endpoint**: `/articles/{id}`
- **Method**: `GET`
- **Parameters**:
    - `id`: ID of the article to retrieve.
- **Description**: Fetches a specific article by its ID.
- **Response**:
    ```json
    {
        "category": "Health",
        "id": 1,
        "published_at": "2024-09-27",
        "source": "BBC",
        "summary": "More than 600 people have been killed by Israeli airstrikes in Lebanon since Monday, health officials say.",
        "title": "Israel striking Hezbollah with ‘full force’ despite ceasefire calls",
        "url": "http://example.com/article1"
    }
    ```
- **Screenshots**:
    ![Retrieve Specific Article](screenshots/Screenshot%20(20).png)

### 3. Search Articles
- **Endpoint**: `/search`
- **Method**: `GET`
- **Parameters**:
    - `q`: Keyword to search for in articles.
- **Description**: Searches for articles based on the provided keyword.
- **Response**:
    ```json
    [
        {
            "category": "Technology",
            "id": 2,
            "published_at": "2024-09-26",
            "source": "CNN",
            "summary": "Tech companies are making strides in AI and automation.",
            "title": "The Rise of AI: What to Expect in the Coming Years",
            "url": "http://example.com/article2"
        }
    ]
    ```
- **Screenshots**:
    ![Search Articles](screenshots/Screenshot%20(21).png)

