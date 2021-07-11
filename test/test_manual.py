from .utils import process

ADS_ACCOUNT_ID = "act_224655308375887"


def test_manual_standard():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": None,
        "start": "2021-06-01",
        "end": "2021-06-30",
    }
    process(data)


def test_manual_hourly():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "hourly",
        "start": "2021-07-01",
        "end": "2021-07-02",
    }
    process(data)


def test_manual_age_genders():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "age_genders",
        "start": "2021-07-01",
        "end": "2021-07-02",
    }
    process(data)


def test_manual_devices():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "devices",
        "start": "2021-07-01",
        "end": "2021-07-02",
    }
    process(data)


def test_manual_region():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "country_region",
        "start": "2021-07-01",
        "end": "2021-07-02",
    }
    process(data)


def test_manual_ads_creatives():
    data = {
        "ads_account_id": ADS_ACCOUNT_ID,
        "mode": "ads_creatives",
        "start": "2021-07-01",
        "end": "2021-07-02",
    }
    process(data)
