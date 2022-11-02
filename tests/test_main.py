from main import resp_v4, resp_geo

def test_resp_v4():
    assert resp_v4.status_code == 200


def test_resp_geo():
    assert resp_geo.status_code == 200
