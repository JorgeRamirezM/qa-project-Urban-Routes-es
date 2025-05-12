from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UrbanRoutesLocators import Locators
import time

# no modificar

def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.from_field)).send_keys(from_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.to_field)).send_keys(to_address)

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_on_request_taxi_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.request_taxi_button)).click()

    def click_on_comfort_rate_icon(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.comfort_rate_icon)).click()

    def get_comfort_rate_icon_text(self):
        return self.driver.find_element(*self.locators.comfort_rate_icon).text

    def select_comfort_rate(self):
        self.click_on_request_taxi_button()
        self.click_on_comfort_rate_icon()

    def click_on_phone_field(self):
        self.driver.find_element(*self.locators.phone_field).click()

    def set_phone_number(self, phone):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.phone_input)).send_keys(phone)

    def get_phone_number(self):
        return self.driver.find_element(*self.locators.phone_input).get_property('value')

    def click_on_phone_next_button(self):
        self.driver.find_element(*self.locators.phone_next_button).click()

    def set_phone_number_method(self, phone):
        self.click_on_phone_field()
        self.set_phone_number(phone)
        self.click_on_phone_next_button()

    def set_phone_code(self, code):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.sms_input_code)).send_keys(code)

    def get_phone_code(self):
        return self.driver.find_element(*self.locators.sms_input_code).get_property('value')

    def click_on_sms_confirm_button(self):
        self.driver.find_element(*self.locators.sms_confirm_button).click()

    def set_phone_code_method(self, code):
        self.set_phone_code(code)
        self.click_on_sms_confirm_button()

    def click_on_payment_method_field(self):
        self.driver.find_element(*self.locators.payment_method_field).click()

    def add_card(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.add_card)).click()

    def set_card_number_and_code(self, card_number, card_code):
        self.driver.find_element(*self.locators.card_number).send_keys(card_number)
        self.driver.find_element(*self.locators.card_code).send_keys(card_code)

    def get_card_number(self):
        return self.driver.find_element(*self.locators.card_number).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.locators.card_code).get_property('value')

    def activate_add_button(self):
        self.driver.find_element(*self.locators.card_second_row).click()

    def click_on_add_button(self):
        self.driver.find_element(*self.locators.add_button).click()

    def close_payment_method_window(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.payment_method_close_button)).click()

    def set_payment_method(self, card_number, card_code):
        self.click_on_payment_method_field()
        self.add_card()
        self.set_card_number_and_code(card_number, card_code)
        self.activate_add_button()
        self.click_on_add_button()
        self.close_payment_method_window()

    def find_message_for_driver_field(self):
        message = self.driver.find_element(*self.locators.message_driver_field)
        self.driver.execute_script("arguments[0].scrollIntoView();", message)

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.locators.message_driver_field).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.locators.message_driver_field).get_property('value')

    def set_on_slider(self):
        slider = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.slider_round))
        self.driver.execute_script("arguments[0].scrollIntoView();", slider)
        slider.click()
        time.sleep(1)

    def verify_slider_still_on(self):
        slider_check = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.check_slider_still_on))
        self.driver.execute_script("arguments[0].scrollIntoView();", slider_check)
        time.sleep(1)
        return slider_check.text

    def click_on_ice_cream_counter_plus(self):
        counter = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.ice_cream_counter_plus))
        self.driver.execute_script("arguments[0].scrollIntoView();", counter)
        counter.click()

    def get_ice_cream_counter_value(self):
        return self.driver.find_element(*self.locators.ice_cream_counter_value).text

    def click_on_order_taxi_button(self):
        order_taxi_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.order_taxi_button))
        self.driver.execute_script("arguments[0].scrollIntoView();", order_taxi_button)
        order_taxi_button.click()

    def get_correct_taxi_button_text(self):
        return self.driver.find_element(*self.locators.order_taxi_button_text).text

    def show_order_body_window(self):
        try:
            order_body = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.locators.order_body_window)
            )
            return order_body.is_displayed()
        except Exception as e:
            print(f"Error al verificar la visibilidad de la ventana: {e}")
            return False

    def show_order_body_window_final(self):
        try:
            order_body = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located(self.locators.order_body_window_final)
            )
            return order_body.is_displayed()
        except Exception as e:
            print(f"Error al verificar la visibilidad de la ventana: {e}")
            return False