import os
from selene import browser, command, have

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_gender(self, value):
        browser.element(value).click()

    def fill_date_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--00{day}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self, value):
        browser.element(value).click()

    def upload_photo(self, path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(path))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state_and_city(self, state, city):
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()

    def click_submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_registered(self, full_name, email, gender, number, date_birth, subjects, hobbies, photo, state, city):
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

