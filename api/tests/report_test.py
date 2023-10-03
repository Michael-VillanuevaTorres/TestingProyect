def test_add_comment(client):
    """
    GIVEN
    WHEN
    THEN
    """
    
    response = client.get('reports/all')
    
    assert response.status_code == 200