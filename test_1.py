import time

import yaml
from module import Site

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata['address'])
name = testdata['username']
passw = testdata['password']
title = testdata['title']
description = testdata['description']
content = testdata['content']


def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, er1):
    input1 = site.find_element('xpath', x_selector1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector)
    btn.click()
    err_label = site.find_element('xpath', x_selector3)
    text = err_label.text
    assert text == er1


def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, er2):
    input1 = site.find_element('xpath', x_selector1)
    input1.clear()
    input1.send_keys(name)
    input2 = site.find_element('xpath', x_selector2)
    input2.clear()
    input2.send_keys(passw)
    btn = site.find_element('css', btn_selector)
    btn.click()
    user_label = site.find_element('xpath', x_selector4)
    text = user_label.text
    assert text == er2


def test_step3(x_selector1, x_selector2, btn_selector, blog_button, blog_title, blog_description, blog_content,
               blog_create_but, blog_name):
    blog_button = site.find_element('xpath', blog_button)
    blog_button.click()
    time.sleep(2)
    input_title_blog = site.find_element('xpath', blog_title)
    input_title_blog.clear()
    input_title_blog.send_keys(title)
    input_blog_description = site.find_element('xpath', blog_description)
    input_blog_description.clear()
    input_blog_description.send_keys(description)
    input_blog_content = site.find_element('xpath', blog_content)
    input_blog_content.clear()
    input_blog_content.send_keys(content)
    create_button = site.find_element('xpath', blog_create_but)
    create_button.click()
    time.sleep(2)
    name_blog = site.find_element('xpath', blog_name)
    text_blog = name_blog.text
    assert text_blog == title

