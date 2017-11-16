# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import datetime

from pages.google_form import GoogleForm
from config.enviroment import google_form


@pytest.fixture()
def chrome_driver(request):
    b = webdriver.Chrome()
    request.addfinalizer(lambda *args: b.quit())
    return b

date = datetime.datetime.now()
current_year = date.year
current_day = date.day
current_month = date.month


@pytest.mark.parametrize('email', ['qwe', 'qwe@.', '1123@123', '@.com'])
def test_negative_email(chrome_driver, email):
    """Negative test - check if Error will displayed for Not Valid email address"""
    google = GoogleForm(chrome_driver)
    google.driver.get(google_form())
    try:
        google.google_email_field().send_keys(email)
        assert google.email_exception_field().text == u'Потрібна дійсна електронна адреса'
    except AssertionError:
        assert False


@pytest.mark.parametrize('email', ['abc@def.com', 'qwerty+10@gmail.com', '1123@123.allo'])
def test_positive_email(chrome_driver, email):
    """Negative test - check that Error will not displayed for Valid email address"""
    google = GoogleForm(chrome_driver)
    google.driver.get(google_form())
    try:
        google.google_email_field().send_keys(email)
        assert google.email_exception_field().is_displayed() is False
    except AssertionError:
        assert False


@pytest.mark.parametrize(('day', 'month', 'year'), [(12, 13, -1), (13, -1, 2017), (0, 's', 2018)])
def test_negative_born_date(chrome_driver, day, month, year):
    """Check that Not Valid date of born will be automatically changed by Google page"""
    google = GoogleForm(chrome_driver)
    google.driver.get(google_form())
    try:
        for _ in day, month, year:
            google.day_field().send_keys(_)
        assert google.date_exception_field().is_displayed() is False
    except AssertionError:
        assert False
