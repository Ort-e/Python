import requests
import uuid


BASE_URL = "https://ru.yougile.com/api-v2"
API_KEY = "--"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


#            POST /projects

def test_create_project_positive():
    project_name = f"Test project {uuid.uuid4()}"

    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"title": project_name}
    )

    assert response.status_code == 201


def test_create_project_negative_empty_name():
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"title": ""}
    )

    assert response.status_code == 400


#            GET /projects/{id}

def test_get_project_positive():
    project_name = f"Get project {uuid.uuid4()}"

    create_response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"title": project_name}
    )

    project_id = create_response.json()["id"]

    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative_wrong_id():
    response = requests.get(
        f"{BASE_URL}/projects/999999999",
        headers=HEADERS
    )

    assert response.status_code == 404


#            PUT /projects/{id}

def test_update_project_positive():
    project_name = f"Old name {uuid.uuid4()}"
    new_name = f"New name {uuid.uuid4()}"

    create_response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"title": project_name}
    )

    project_id = create_response.json()["id"]

    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
        json={"title": new_name}
    )

    assert response.status_code == 200


def test_update_project_negative_wrong_id():
    response = requests.put(
        f"{BASE_URL}/projects/999999999",
        headers=HEADERS,
        json={"title": "Does not matter"}
    )

    assert response.status_code == 404
