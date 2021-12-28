# coding: utf-8
#
import uiautomator2 as u2
import pytest
import logging

log = logging.getLogger(__name__)

class TestUI:
    def setup(self):
        self.d = u2.connect('399ab7c6')
        self.d.app_start("hko.MyObservatory_v1_0")
        self.d.settings['operation_delay'] = (.5, 1)

    def test_tomorrow_weather(self):
        self.d.xpath('//*[@content-desc="转到上一层级"]').click()
        self.d.swipe(496, 2106, 548, 896)
        self.d.xpath('//*[@text="九天預報"]').click()
        tomorrow_weather = self.d.xpath(
            '//*[@resource-id="hko.MyObservatory_v1_0:id/mainAppSevenDayView"]/android.widget.LinearLayout[1]').attrib.get(
            "content-desc", "")
        log.info(tomorrow_weather)
        assert self.d.xpath('//*[@text="九天預報"]').get_text() == '九天預報'

    def teardown(self):
        self.d.app_stop("hko.MyObservatory_v1_0")



if __name__ == '__main__':
    pytest.main(['-s', 'Test_ui.py'])

