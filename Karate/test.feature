Feature : typicode API testing

Backgroumd:
* url 'https://jsonplaceholder.typicode.com/posts'
* configure report = {format: 'html', output: 'test-report,html'}

Scenario: Verify API Response

    Given path '/endpoint'
    When method get
    Then status 200

    # match response fields
    And match response.id == '#number'
    And match response.title == '#string'
    And match response.body == '#string'
    And match response.userId != null

    # generate HTML report
    * karate.callSingle('classpath:com/intuit/karate/core/HtmlUtils.feature')