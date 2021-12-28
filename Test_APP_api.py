# coding: utf-8
#
import urllib.request
import json
import pytest
import logging

log = logging.getLogger(__name__)
class Test_after_tomorrow_humidity:
    def test_api(self):
        url = "https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml"
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        request = urllib.request.Request(url, headers=header)
        with urllib.request.urlopen(request) as res_status:
            staut_code = res_status.getcode()
            logging.info(staut_code)
            if staut_code == 200:
                data = json.loads(res_status.read())
                logging.info(data)
                data = dict(data)
            else:
                data = {}
        assert staut_code == 200
        assert data
        log.info(F"code staut:{staut_code}, after tomorrow humidity: {data['forecast_detail'][1]['min_rh']}~{data['forecast_detail'][1]['max_rh']}%")

if __name__ == '__main__':
    pytest.main()
