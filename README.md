# Web Scraping & Visualization Application

A full-stack web application for scraping ikman.lk listings with batch processing and real-time single ad analysis. Built with **FastAPI** (Python) backend and **React + Vite** frontend.

## 🎯 Features

### Batch Scraper Dashboard
- Scrape multiple pages from ikman.lk search results
- Store data in MySQL database with automatic deduplication
- Visual analytics with Chart.js:
  - Items per location (Bar Chart)
  - Price distribution (Line Chart)
- Statistics cards showing total items and average price
- Data table with all scraped products

### Single Ad Inspector
- Analyze individual ikman.lk ads in real-time
- Beautiful product card UI with:
  - Image gallery with thumbnails
  - Large price display
  - Location badges
  - Seller information
  - Full description
  - Direct link to original ad

## 🛠️ Tech Stack

**Backend:**
- Python 3.8+
- FastAPI - Modern, fast web framework
- SQLAlchemy - ORM for database operations
- BeautifulSoup4 - Web scraping
- PyMySQL - MySQL connector
- Uvicorn - ASGI server

**Frontend:**
- React 18
- Vite - Build tool
- Tailwind CSS - Styling
- Chart.js & react-chartjs-2 - Data visualization
- Axios - HTTP client
- React Router - Navigation

**Database:**
- MySQL 8.0+

## 📁 Project Structure

```
CSV_to_visualization/
├── backend/
│   ├── main.py              # FastAPI application & endpoints
│   ├── models.py            # SQLAlchemy database models
│   ├── database.py          # Database configuration
│   ├── scraper.py           # Web scraping logic
│   ├── config.py            # Settings management
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx          # Main dashboard page
│   │   │   └── SingleAdInspector.jsx  # Ad inspector page
│   │   ├── App.jsx          # Main app component
│   │   ├── api.js           # API client
│   │   ├── main.jsx         # Entry point
│   │   └── index.css        # Global styles
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
└── README.md
```

## 🚀 Getting Started

### Prerequisites

1. **Python 3.8+** - [Download here](https://www.python.org/downloads/)
2. **Node.js 16+** - [Download here](https://nodejs.org/)
3. **MySQL 8.0+** - [Download here](https://dev.mysql.com/downloads/)

### Database Setup

1. Install and start MySQL server

2. Create a database:
```sql
CREATE DATABASE scraper_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. Create a user (optional but recommended):
```sql
CREATE USER 'scraper_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON scraper_db.* TO 'scraper_user'@'localhost';
FLUSH PRIVILEGES;
```

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Windows CMD:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create `.env` file from template:
```bash
copy .env.example .env
```

6. Edit `.env` with your MySQL credentials:
```env
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/scraper_db
MAX_PAGES=5
```

7. Run the FastAPI server:
```bash
python main.py
```

The backend will be available at: **http://localhost:8000**

API Documentation (auto-generated): **http://localhost:8000/docs**

### Frontend Setup

1. Open a new terminal and navigate to frontend:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at: **http://localhost:5173**

## 📖 Usage

### Batch Scraper

1. Open the Dashboard at http://localhost:5173
2. Enter an ikman.lk search URL (e.g., `https://ikman.lk/en/ads/sri-lanka/electronics`)
3. Set the number of pages to scrape (1-10)
4. Click "Run Batch Scraper"
5. Wait for scraping to complete
6. View statistics, charts, and product table

### Single Ad Inspector

1. Navigate to "Ad Inspector" tab
2. Paste a specific ikman.lk ad URL
3. Click "Analyze Ad"
4. View the detailed product card with images, price, description, and seller info

## 🔌 API Endpoints

### `POST /api/scrape-batch`
Scrape multiple pages and store in database.

**Request:**
```json
{
  "url": "https://ikman.lk/en/ads/sri-lanka/electronics",
  "max_pages": 5
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Scraping completed...",
  "scraped_count": 150,
  "added": 120,
  "updated": 30
}
```

### `GET /api/stats`
Get dashboard statistics.

**Response:**
```json
{
  "total_items": 150,
  "average_price": 45000.50,
  "items_by_location": [
    {"location": "Colombo", "count": 50},
    {"location": "Kandy", "count": 30}
  ],
  "price_distribution": [
    {"range": "0-10k", "count": 20},
    {"range": "10k-50k", "count": 80}
  ]
}
```

### `POST /api/scrape-single`
Scrape a single ad page.

**Request:**
```json
{
  "url": "https://ikman.lk/en/ad/..."
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "title": "iPhone 13 Pro Max",
    "price": 250000,
    "description": "...",
    "location": "Colombo 3",
    "images": ["url1", "url2"],
    "seller_name": "John Doe",
    "url": "..."
  }
}
```

### `GET /api/products`
Get all scraped products with pagination.

**Query Parameters:**
- `skip`: Number of items to skip (default: 0)
- `limit`: Max items to return (default: 100)

### `DELETE /api/products/clear`
Clear all products from database (useful for testing).

## 🔧 Customization

### Adjusting Scraper Selectors

If ikman.lk changes their HTML structure, update the CSS selectors in `backend/scraper.py`:

```python
# Example: Update the ad listing selector
ads = soup.find_all('li', class_='normal--2QYVk')  # Change class name here

# Update individual field selectors
title_elem = ad.find('h2')  # Adjust element/class
price_elem = ad.find('div', class_='price--3SnqI')
```

### Changing Price Ranges

Modify price distribution ranges in `backend/main.py`:

```python
price_ranges = [
    {"range": "0-10k", "min": 0, "max": 10000},
    {"range": "10k-50k", "min": 10000, "max": 50000},
    # Add more ranges...
]
```

### Styling

Edit Tailwind configuration in `frontend/tailwind.config.js` to customize colors, fonts, etc.

## 🐛 Troubleshooting

### Backend Issues

**"ModuleNotFoundError"**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

**"Can't connect to MySQL server"**
- Check MySQL is running: `mysql -u root -p`
- Verify credentials in `.env` file
- Check DATABASE_URL format

**"No products found"**
- ikman.lk may have changed their HTML structure
- Update CSS selectors in `scraper.py`
- Check if the URL is accessible

### Frontend Issues

**"Module not found"**
- Run `npm install` in frontend directory
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`

**"Network Error"**
- Ensure backend is running on port 8000
- Check CORS settings in `backend/main.py`
- Verify API_BASE_URL in `frontend/src/api.js`

**Charts not displaying**
- Check browser console for errors
- Ensure chart.js is installed: `npm install chart.js react-chartjs-2`

## 📊 Database Schema

**Products Table:**
```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(500) NOT NULL,
    price DECIMAL(10,2),
    location VARCHAR(200),
    posted_time VARCHAR(100),
    link VARCHAR(1000) UNIQUE NOT NULL,
    image_url VARCHAR(1000),
    scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- ikman.lk for providing the marketplace
- FastAPI for the excellent framework
- React and Vite for the modern frontend stack
- Chart.js for beautiful visualizations

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Built with ❤️ using Python FastAPI and React**