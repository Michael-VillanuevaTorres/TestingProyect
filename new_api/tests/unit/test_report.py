import pytest

from app.extensions import db


def test_add_comment_to_report(test_client, init_database):
    # GIVEN that we have an existing report (id_report=1)
    # WHEN a POST request is made to add a comment to the report with JSON data {"text": "Test comment"}
    response = test_client.post('/report/add/comment?id_report=1', json={"text": "Test comment"})
    # THEN we expect a successful response with a status code of 201 and a success message
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'Comment added successfully.'

    # GIVEN that the id_report does not exist
    # WHEN a POST request is made to add a comment to a non-existing report (id_report=100)
    response = test_client.post('/report/add/comment?id_report=100', json={"text": "Test comment"})
    # THEN we expect a response with a status code of 400 and an error message
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_report is not in the database'

    # GIVEN that the request JSON data does not include the 'text' field
    # WHEN a POST request is made to add a comment to the report (id_report=1) without the 'text' field
    response = test_client.post('/report/add/comment?id_report=1', json={})
    # THEN we expect a response with a status code of 400 and an error message
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'Comment not added. Text is needed'

def test_add_like_to_report(test_client, init_database):
    # GIVEN: An existing report and an existing user
    # WHEN: A like is added to the report by the user
    response = test_client.post('/report/add/like?id_report=1&id_user=1')
    # THEN: It should receive a successful response and a message indicating that the like was added successfully
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'like added successfully.'

    # WHEN: An attempt is made to add a like again to the same report by the same user
    response = test_client.post('/report/add/like?id_report=1&id_user=1')
    # THEN: It should receive an error response and a message indicating that the like is already in the database

    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The like is already in the database'

def test_add_report(test_client, init_database):
    # GIVEN: Data for a new report with a title and description
    data = {
        "title": "Test Report",
        "description": "Test Description"
    }
    
    # WHEN: A request is made to add the report with an existing product and user
    response = test_client.post('/report/add?id_product=1&id_user=1', json=data)
    # THEN: It should receive a successful response and a message indicating that the report was added successfully
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'Report added successfully.'

    # WHEN: A request is made to add the report with a non-existent product
    response = test_client.post('/report/add?id_product=100&id_user=1', json=data)
    # THEN: It should receive an error response and a message indicating that the id_product is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_product is not in the database'

    # WHEN: A request is made to add the report with missing 'title' in the data
    response = test_client.post('/report/add?id_product=1&id_user=1', json={"description": "Test Description"})
    # THEN: It should receive an error response and a message indicating that 'title' is needed
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'Report not added. Title is needed'

    # WHEN: A request is made to add the report with missing 'description' in the data
    response = test_client.post('/report/add?id_product=1&id_user=1', json={"title": "Test Report"})
    # THEN: It should receive an error response and a message indicating that 'description' is needed
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'Report not added. Description is needed'

def test_get_all_reports(test_client, init_database):
    # GIVEN: that we have an existing reports
    
    # WHEN: A request is made to get all reports
    response = test_client.get('/report/get/all')
    # THEN: It should receive a successful response with a status code 200
    # and the response data should be a list
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_comments_form_report(test_client, init_database):
    # GIVEN: that we have an existing reports
    
    # WHEN: A request is made to get comments for a valid report (id_report=1)
    response = test_client.get('/report/comments?id_report=1')
    
    # THEN: It should receive a successful response with a status code 200,
    # and the response data should be a list
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # WHEN: A request is made to get comments for a report that doesn't exist (id_report=100)
    response = test_client.get('/report/comments?id_report=100')
    
    # THEN: It should receive a response with a status code 400,
    # and the response should contain an error message indicating that the id_report is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_report is not in the database'

def test_get_number_of_reports(test_client, init_database):
    # GIVEN: that we have an existing product (id_product=1)

    # WHEN: A request is made to get a specified quantity of reports (id_product=1, quantity=1)
    response = test_client.get('/report/get/more?id_product=1&quantity=1')
    
    # THEN: It should receive a successful response with a status code 200,
    # and the response data should be a list
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # WHEN: A request is made to get reports for a product that doesn't exist (id_product=100, quantity=1)
    response = test_client.get('/report/get/more?id_product=100&quantity=1')
    
    # THEN: It should receive a response with a status code 400,
    # and the response should contain an error message indicating that the id_product is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_product is not in the database'

    # WHEN: A request is made to get reports without specifying the quantity (id_product=1)
    response = test_client.get('/report/get/more?id_product=1')
    
    # THEN: It should receive a response with a status code 400,
    # and the response should contain an error message indicating that the quantity is not specified
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'Quantity not specified'

    # WHEN: A request is made to get a quantity of reports larger than the available number (id_product=1, quantity=1000)
    response = test_client.get('/report/get/more?id_product=1&quantity=1000')
    
    # THEN: It should receive a response with a status code 400,
    # and the response should contain an error message indicating that the quantity is bigger than the number of reports
    assert response.status_code == 400
    assert 'message' in response.json
    assert 'The quantity is bigger than the number of reports' in response.json['message']

def test_get_all_reports_from_product(test_client, init_database):
    # GIVEN: that we have an existing product (id_product=1)
    
    # WHEN: A request is made to get all reports for a specified product (id_product=1)
    response = test_client.get('/report/product/all?id_product=1')
    
    # THEN: It should receive a successful response with a status code 200,
    # and the response data should be a list
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # WHEN: A request is made to get reports for a product that doesn't exist (id_product=100)
    response = test_client.get('/report/product/all?id_product=100')
    
    # THEN: It should receive a response with a status code 400,
    # and the response should contain an error message indicating that the id_product is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_product is not in the database'

def test_get_report(test_client, init_database):
    # GIVEN: that we have an existing report (id_report=1)
    
    # WHEN: A request is made to get a report by its ID (id_report=1)
    response = test_client.get('/report/get?id_report=1')
    
    # THEN: It should receive a successful response with a status code 200,
    # and the response data should be a dictionary
    assert response.status_code == 200
    assert isinstance(response.json, dict)

    # WHEN: A request is made to get a report with an ID that doesn't exist (id_report=100)
    response = test_client.get('/report/get?id_report=100')
    
    # THEN: It should receive a response with a status code 404
    # indicating that the requested report was not found
    assert response.status_code == 404

def test_update_state_of_report(test_client, init_database):
    # GIVEN: that we have an existing report (id_report=1)
    # WHEN: A request is made to update the state of a report (id_report=1) to state (id_state=1)
    response = test_client.post('/report/update/state?id_report=1&id_state=1')
    
    # THEN: It should receive a successful response with a status code 201,
    # and the response message should indicate that the state was updated successfully
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'state updated successfully.'

    # WHEN: A request is made to update the state of a report with an ID that doesn't exist (id_report=100)
    response = test_client.post('/report/update/state?id_report=100&id_state=1')
    
    # THEN: It should receive a response with a status code 400
    # and the response message should indicate that the id_report is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_report is not in the database'

    # WHEN: A request is made to update the state of a report (id_report=1) to a state that doesn't exist (id_state=100)
    response = test_client.post('/report/update/state?id_report=1&id_state=100')
    
    # THEN: It should receive a response with a status code 400
    # and the response message should indicate that the id_state is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_state is not in the database'

def test_update_priority_of_report(test_client, init_database):
   # GIVEN: that we have an existing report (id_report=1)
    
    # WHEN: A request is made to update the priority of a report (id_report=1) to priority (id_priority=2)
    response = test_client.post('/report/update/priority?id_report=1&id_priority=2')
    # THEN: It should receive a successful response with a status code 201,
    # and the response message should indicate that the priority was updated successfully
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'state updated successfully.'

    # WHEN: A request is made to update the priority of a report with an ID that doesn't exist (id_report=100)
    response = test_client.post('/report/update/priority?id_report=100&id_priority=2')
    # THEN: It should receive a response with a status code 400
    # and the response message should indicate that the id_report is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_report is not in the database'

    # WHEN: A request is made to update the priority of a report (id_report=1) to a priority that doesn't exist (id_priority=100)
    response = test_client.post('/report/update/priority?id_report=1&id_priority=100')
    # THEN: It should receive a response with a status code 400
    # and the response message should indicate that the id_priority is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_state is not in the database'

def test_check_possibles_states_to_report(test_client, init_database):
    # GIVEN: that we have an existing report (id_report=1)
    
    # WHEN: A request is made to check possible states for a report with id_report=1
    response = test_client.get('/report/state?id_report=1')
    
    # THEN: It should receive a successful response with a status code 200,
    # and the response should be a list
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # WHEN: A request is made to check possible states for a report with an ID that doesn't exist (id_report=100)
    response = test_client.get('/report/state?id_report=100')
    
    # THEN: It should receive a response with a status code 400,
    # and the response message should indicate that the id_report is not in the database
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'The id_report is not in the database'


def test_all_states(test_client, init_database):
    # GIVEN: that we have an existinG states
    
    # WHEN: A request is made to retrieve all possible states for reports
    response = test_client.get('/report/state/all')
    
    # THEN: It should receive a successful response with a status code 200,
    # and the response should be a list
    assert response.status_code == 200
    assert isinstance(response.json, list)

    