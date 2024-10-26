# Decathlon Turnover Forecasting API

This repository contains the code and resources for forecasting the 8-week turnover at the store-department level for Decathlon. The goal is to assist store managers in making data-driven mid-term economic decisions.

## Setup Instructions

1. **Clone the repository**:

git clone https://github.com/your-repo/decathlon-turnover-forecast.git


2. **Install dependencies**:
Navigate to the project directory and install the required Python packages:

pip install -r requirements.txt


3. **Run the Flask API**:

python main.py


## API Usage

### Root Endpoint
- **URL**: /
- **Method**: GET
- **Response**:
{
   "message": "Welcome to the Decathlon Turnover Forecasting API"
}

### Prediction Endpoint
- **URL**: /predict
- **Method**: POST

- **Request Body**:
{
    "but_num_business_unit": 100,
    "dpt_num_department": 112,
    "but_postcode": 75000,
    "but_latitude": 43.34,
    "but_longitude": 34.83,
    "but_region_idr_region": 23,
    "zod_idr_zone_dgr": 10,
    "day_id": "2017-11-25"
}

- **Response**:
{
    "resultats": {
        "but_latitude": 43.34,
        "but_longitude": 34.83,
        "but_num_business_unit": 100,
        "but_postcode": 75000,
        "but_region_idr_region": 23,
        "day_id": "2017-11-25",
        "dpt_num_department": 112,
        "prediction": 727,
        "zod_idr_zone_dgr": 10
    }
}