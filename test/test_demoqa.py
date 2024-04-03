import os
from selene import browser, be, have, command

def test_enter_data():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('first name')
    browser.element('#lastName').type('last name')
    browser.element('#userEmail').type('test@test.test')
    browser.element('#userNumber').type('1234567890')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('.react-datepicker-wrapper').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="2"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1998"]').click()
    browser.element('.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('images/Screenshot_1.png'))
    browser.element('#currentAddress').type('Address')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').click()

    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
        (
        'first name last name',
        'test@test.test',
        'Female',
        '1234567890',
        '02 March,1998',
        'Computer Science',
        'Music',
        'Screenshot_1.png',
        'Address',
        'Haryana Karnal'
    ))
