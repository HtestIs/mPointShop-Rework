import os
from dotenv import load_dotenv

load_dotenv()
ENV_CONFIG = {
    "dev" : {
        "base_url" : os.getenv("DEV_WEB_BASE_URL"),
        "api_url" : os.getenv("DEV_API_BASE_URL"),
        "users": {
            "partner": {
                "username": os.getenv("DEV_PARTNER_USERNAME"),
                "password": os.getenv("DEV_PARTNER_PASSWORD")
            },
            "merchant": {
                "username": os.getenv("DEV_MERCHANT_USERNAME"),
                "password": os.getenv("DEV_MERCHANT_PASSWORD")
            }
        },
        "dup_username" : os.getenv("DEV_DUP_USERNAME")
    },

    "prod" :{
        "base_url" : os.getenv("PROD_WEB_BASE_URL"),
        "api_url" : os.getenv("PROD_API_BASE_URL"),
        "users": {
            "partner": {
                "username": os.getenv("PROD_PARTNER_USERNAME"),
                "password": os.getenv("PROD_PARTNER_PASSWORD")
            },
            "merchant": {
                "username": os.getenv("PROD_MERCHANT_USERNAME"),
                "password": os.getenv("PROD_MERCHANT_PASSWORD")
            }
        },
        "dup_username" : os.getenv("PROD_DUP_USERNAME")
    }    
}