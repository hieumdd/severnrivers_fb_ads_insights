from unittest.mock import Mock

from main import main
from .utils import encode_data


def test_broadcast_ads_insights():
    data = {"broadcast": "ads_insights"}
    message = encode_data(data)
    req = Mock(get_json=Mock(return_value=message), args=message)
    res = main(req)
    assert res["message_sent"] > 0


def test_broadcast_ads_insights_manual():
    data = {"broadcast": "ads_insights", "start": "2021-01-01", "end": "2021-01-15"}
    message = encode_data(data)
    req = Mock(get_json=Mock(return_value=message), args=message)
    res = main(req)
    assert res["message_sent"] > 0


def test_broadcast_ads_creatives():
    data = {"broadcast": "ads_creatives", "initial": True}
    message = encode_data(data)
    req = Mock(get_json=Mock(return_value=message), args=message)
    res = main(req)
    assert res["message_sent"] > 0
