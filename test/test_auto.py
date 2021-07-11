from .utils import process

ADS_ACCOUNT_ID = "act_224655308375887"

def test_auto_standard():
    data = {"ads_account_id": ADS_ACCOUNT_ID, "mode": None}
    process(data)

def test_auto_hourly():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "hourly"
    }
    process(data)


def test_auto_age_genders():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "age_genders",
    }
    process(data)

def test_auto_devices():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "devices"
            }
    process(data)

def test_auto_region():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "country_region",
    }
    process(data)


def test_auto_ads_creatives():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "ads_creatives",

    }
    process(data)
