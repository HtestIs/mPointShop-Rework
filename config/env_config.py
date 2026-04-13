import os
from dotenv import load_dotenv

load_dotenv()
ENV_CONFIG = {
    "dev" : {
        "base_url" : os.getenv("DEV_WEB_BASE_URL"),
        "mexchange_web_url" : os.getenv("DEV_MEXCHANGE_WEB_URL"),
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
        "dup_username" : os.getenv("DEV_DUP_USERNAME"),
        "mexchange_api_url": os.getenv("DEV_MEXCHANGE_API_URL"),
        "mexchange_username": os.getenv("DEV_MEXCHANGE_USERNAME"),
        "mexchange_password": os.getenv("DEV_MEXCHANGE_PASSWORD"),
        "aap_base_url": os.getenv("DEV_AAP_BASE_URL"),
        "aap_username": os.getenv("DEV_AAP_USERNAME"),
        "aap_password": os.getenv("DEV_AAP_PASSWORD"),
        "app_username": os.getenv("DEV_APP_USERNAME"),
        "app_password": os.getenv("DEV_APP_PASSWORD"),
        "aap_token": os.getenv("DEV_AAP_TOKEN")
    },

    "prod" :{
        "base_url" : os.getenv("PROD_WEB_BASE_URL"),
        "mexchange_web_url" : os.getenv("PROD_MEXCHANGE_WEB_URL"),
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
        "dup_username" : os.getenv("PROD_DUP_USERNAME"),
        "mexchange_api_url": os.getenv("PROD_MEXCHANGE_API_URL"),
        "mexchange_username": os.getenv("PROD_MEXCHANGE_USERNAME"),
        "mexchange_password": os.getenv("PROD_MEXCHANGE_PASSWORD"),
        "aap_base_url": os.getenv("PROD_AAP_BASE_URL"),
        "aap_username": os.getenv("PROD_AAP_USERNAME"),
        "aap_password": os.getenv("PROD_AAP_PASSWORD"),
        "app_username": os.getenv("PROD_APP_USERNAME"),
        "app_password": os.getenv("PROD_APP_PASSWORD")
    }    
}