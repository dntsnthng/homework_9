from selene import browser, command, have
import resource

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element('[for="gender-radio-2"]').click()
        browser.element('#userNumber').type(user.number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(f'.react-datepicker__day--00{user.day}').click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.element('[for="hobbies-checkbox-3"]').click()
        browser.element('#uploadPicture').send_keys(resource.path(user.photo))
        browser.element('#currentAddress').type(user.address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_registered(self, user):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts
            (
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.number,
            f'{user.day} {user.month},{user.year}',
            user.subjects,
            user.hobbies,
            user.photo,
            user.address,
            f'{user.state} {user.city}'
        ))
