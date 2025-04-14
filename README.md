# RentWise - Smarter Rents, Better Living

![RentWise UI Screenshot](images/image1.jpeg)
![RentWise Form Screenshot](images/image2.jpeg)

RentWise is a Rent Prediction System that leverages machine learning to predict rental prices based on property features like location, carpet area, and BHK. It features an interactive web interface and a trained machine learning model built using real-world data scraped from **MagicBricks.com**.

---

##  Problem Statement
In metropolitan cities, rent pricing is often inconsistent and lacks transparency. Tenants struggle to determine fair market prices, and landlords may over or undercharge due to insufficient insights. RentWise solves this by offering:
- Reliable rent estimates based on real listings
- A user-friendly interface for tenants and landlords

---

##  Data Collection (Web Scraping)
Data was scraped from **MagicBricks.com**, covering key attributes:
- **Location** (e.g., Jaipur)
- **BHK (Bedrooms)**
- **Carpet Area** (in sq. ft.)
- **Rent Price** (target variable)

Libraries used:
- `requests`, `BeautifulSoup` for web scraping
- `pandas` for data organization and cleaning

---

##  Machine Learning Pipeline
1. **Data Cleaning**
   - Removed null entries and outliers
   - Converted text to numeric types where needed

2. **Feature Engineering**
   - One-hot encoded location column
   - Scaled `Carpet Area` using `MinMaxScaler`

3. **Model Used**
   - Trained an **XGBoost Regressor** for high accuracy
   - Saved using `pickle` for deployment

4. **Evaluation**
   - RMSE and R² score used to evaluate performance

---

##  Web Interface (Frontend + Backend)
- Built using **Flask** (Python)
- **HTML + CSS** for frontend layout
- Integrated the ML model via Flask backend to provide predictions

### Features:
- Dropdown to select location
- Inputs for BHK and Area
- Button to generate predicted rent
- Responsive UI design with styled layout and background image

---

##  Folder Structure
```
RentPrediction/
├── app.py                      # Flask backend
├── model.pkl                  # Trained ML model
├── scaler.pkl                 # Scaler for area
├── location.pkl               # Location list
├── feature_columns.pkl        # All feature columns
├── templates/
│   └── index.html             # HTML page
├── static/
│   └── style.css              # CSS styling
├── images/
│   └── image1.jpeg            # Background image
```

---

##  Real-World Use Cases
- Rent estimation tool for tenants
- Price benchmarking for property owners
- Real estate aggregators integrating predictive pricing
- Property management dashboards

---

##  Future Scope
- Add more features like furnishing status, number of bathrooms, amenities
- Improve model using deep learning or ensemble stacking
- Deploy on **Render**, **Heroku**, or **AWS EC2**
- Use live data APIs to avoid outdated data
- Integrate location map using Google Maps API

---

##  Acknowledgement
This project is part of a learning journey to explore Machine Learning, Web Development, and Data Analytics using real-world problems.

---

**Made with ❤️ by Harsh Agarwal**

