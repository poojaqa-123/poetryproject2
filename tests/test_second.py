import pytest
import logging
import requests  # type: ignore

# logging.basicConfig()
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)


def test_breeds():
    response = requests.get("https://catfact.ninja/breeds")
    # print(response.json())
    print(f"\ncurrent page : {response.json()['current_page']}")
    print(f"\npath : {response.json()['path']}")

    assert response.status_code == 200
    assert response.json()["current_page"] == 1
    assert response.json()["path"] == "https://catfact.ninja/breeds"


def test_fact():
    response = requests.get("https://catfact.ninja/fact")
    print(f"fact :{response.json()['fact']} ")
    print(f"length :{response.json()['length']} ")

    assert response.json()["fact"] is not None
    assert response.json()["length"] is not None


# @pytest.mark.skip
def test_fact_list():
    response = requests.get("https://catfact.ninja/facts")
    print(f"per_page :{response.json()['per_page']} ")
    print(f"total :{response.json()['total']} ")

    assert response.json()["per_page"] == 10
    assert response.json()["total"] == 332


def test_check():
    print(f"-------- check -------------- ")


def test_check2():
    print(f"-------- check 2 -------------- ")


def test_check3():
    print(f"-------- check 3 -------------- ")
