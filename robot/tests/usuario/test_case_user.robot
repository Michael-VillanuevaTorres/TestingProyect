*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://localhost:5173/
${product}  product_name
${comment}  bug_comment
${state}  expected_state_value


*** Test Cases ***
Open firefox accessing an URL, wait 10 sec and close it
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s    
    [Teardown]    Close Browser

Client wants to get the list of all bugs and their states for a product
    [Documentation]    Test to verify the list of reports and their states.
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s    # Wait for 3 seconds to allow the page to load completely

    #Go to right page
    Go To    ${URL}/MisReportes

    # Select a specific product
    Click Link  id:product-2

    # check if page contains this product and not orthers
    Page Should Contain Element  class:product-2
    Page Should Not Contain Element  class:product-1

    [Teardown]    Close Browser

Client wants to report bugs for a software
    [Documentation]    Test to verify reporting bugs functionality.
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s    # Wait for 3 seconds to allow the page to load completely

    # Actions for the test
    Go To    ${URL}/IngresarBug
    # Enter bug report details in the form
    Input Text    id:bug-name    bug_name
    Select From List by Value    id:product-select    class:product-1
    Input Text    id:bug-description    bug_description
    Click Button  id:send-button

    # Verify redirection to the homepage after form submission
    Wait Until Page Contains    ${URL}

    [Teardown]    Close Browser

Client wants to comment on a bug report
    [Documentation]    Test to verify commenting on a bug report functionality.
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s    # Wait for 3 seconds to allow the page to load completely

    # Actions for the test
    Go To    ${URL}/MisReportes

    # View a specific bug report
    Click Button   id:default_report

    # Add a comment to the bug report
    Input Text    xpath=//textarea[@id='input-box']    comment
    Click Button    xpath=//button[@id='comment-button']

    # Verify that the comment appears immediately in the interface
    Page Should Contain Element    class:comment

    [Teardown]    Close Browser

Client wants to give a +1 or "like" to a bug report
    [Documentation]    Test to verify giving a +1 or "like" functionality to a bug report.
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s    # Wait for 3 seconds to allow the page to load completely

    # Actions for the test
    Go To    ${URL}/MisReportes

    # View a specific bug report
    Click Element    xpath=//div[@id='default_report']

    # Give a +1 or "like" to the bug report
    Click Button    xpath=//button[@class='like-button']

    # Verify that the like counter increased by 1
    ${likes}    Get Text    xpath=//span[@class='like-counter']
    Should Be Equal As Numbers    ${likes}    1

    [Teardown]    Close Browser

Client wants to view their contributions on the web application
    [Documentation]    Test to verify viewing own contributions functionality.
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s    # Wait for 3 seconds to allow the page to load completely

    # Actions for the test
    Go To    ${URL}/MisReportes

    # View all reports contributed by the client
    ${reports}    Get WebElements    xpath=//div[@class='user-reports']

    # Verify the information for each report
    FOR    ${report}    IN    @{reports}
        ${title}    Get Text    xpath=${report}//span[@class='report_title']
        ${state}    Get Text    xpath=${report}//span[@class='report_state']
        ${date}     Get Text    xpath=${report}//span[@class='report_date']
        ${likes}    Get Text    xpath=${report}//span[@class='report_likes']

        Log    Report: ${title} | State: ${state} | Date: ${date} | Likes: ${likes}

        # Access a specific report to view comments or add a new one
        Click Element    xpath=${report}//a[@class='view_report_link']

        # Verify the ability to view comments and add a new one on the specific report page
        
        # Go back to the list of user contributions
        Go Back
    END

    [Teardown]    Close Browser

Client wants to view liked reports
    [Documentation]    Test to verify viewing liked reports functionality.
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Sleep    3s    # Wait for 3 seconds to allow the page to load completely

    # Actions for the test
    Go To    ${URL}/MisReportes

    # View all reports liked by the client
    ${liked_reports}    Get WebElements    xpath=//div[@class='liked_reports']

    # Verify the information for each liked report
    FOR    ${report}    IN    @{liked_reports}
        ${title}    Get Text    xpath=${report}//span[@class='report_title']
        ${date}     Get Text    xpath=${report}//span[@class='report_date']
        ${state}    Get Text    xpath=${report}//span[@class='report_state']
        ${likes}    Get Text    xpath=${report}//span[@class='report_likes']

        Log    Liked Report: ${title} | Date: ${date} | State: ${state} | Likes: ${likes}

        # Access a specific liked report (adjust the selector)
        Click Element    xpath=${report}//a[@class='view_liked_report_link']

        # Verify the ability to view details of the specific liked report?

        # Go back to the list of liked reports
        Go Back

    END

    [Teardown]    Close Browser