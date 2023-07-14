import pytest
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    name = testdata['username']


@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def btn_selector():
    return """button"""


@pytest.fixture()
def er1():
    return "401"


@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def er2():
    return f"Hello, {name}"


@pytest.fixture()
def blog_button():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def blog_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def blog_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def blog_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def blog_create_but():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def blog_name():
    return """//*[@id="app"]/main/div/div[1]/h1"""
