from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

        #Añadidos los localizadores a la clase

        self.from_field = (By.ID, 'from')
        self.to_field = (By.ID, 'to')
        self.request_taxi_button = (By.CSS_SELECTOR, ".button.round")
        self.comfort_rate_icon = (By.XPATH, "//div[@class='tcard']/div[@class='tcard-title' and text()='Comfort']") #Modificado el localizador. No sé si sea asi porque la clase tcard active solo aparece hasta
        # que se le da click a alguna tarifa, antes de eso, solo aparece como tcard, y si pongo directo la clase como tcard active arroja un error. Entonces, según yo, no hay manera de seleccionar la tarifa
        #comfort mas que con la clase tcard-title junto con el texto. A final de cuentas, aunque modifique el localizador, me parece que es el mismo solo más alargado, más el localizador extra de abajo (el mismo que ya tenía arriba)
        self.comfort_rate_icon_text = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
        self.phone_field = (By.CLASS_NAME, 'np-text')
        self.phone_input = (By.ID, 'phone')
        self.phone_next_button = (By.XPATH, "//button[text()='Siguiente']")
        self.sms_input_code = (By.XPATH, "//div[@class='np-input']/div/input[@id='code']")
        self.sms_confirm_button = (By.XPATH, "//button[text()='Confirmar']")
        self.payment_method_field = (By.CLASS_NAME, "pp-text")
        self.add_card_window = (By.CLASS_NAME, "pp-plus-container")
        self.card_number = (By.ID, 'number')
        self.card_code = (By.XPATH, "//div[@class='card-code-input']/input[@id='code']")
        self.card_second_row = (By.CLASS_NAME, "card-second-row")
        self.add_button = (By.XPATH, "//button[@class='button full' and text()='Agregar']")
        self.payment_method_field_text = (By.CLASS_NAME, "pp-value-text") #Añadido localizador para validar pago con tarjeta
        self.payment_method_close_button = (By.XPATH, "//div[@class='payment-picker open']/div/div[@class='section active']/button[@class='close-button section-close']")
        self.message_driver_field = (By.ID, "comment")
        self.slider_round = (By.XPATH, "//div[@class='r-sw-label'][contains(text(), 'Manta y pañuelos')]/following-sibling::div[@class='r-sw']/div[@class='switch']/span[@class='slider round']")
        self.slider_status = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div[@class='r-sw']//input[@type='checkbox' and @class='switch-input']")
        self.ice_cream_counter_plus = (By.XPATH, "//div[@class='r sub r-type-counter'][.//div[@class='r-counter-label' and contains(text(), 'Helado')]]//div[@class='counter-plus']")
        self.ice_cream_counter_value = (By.XPATH, "//div[@class='r sub r-type-counter'][.//div[@class='r-counter-label' and contains(text(), 'Helado')]]//div[@class='counter']/div[@class='counter-value']")
        self.order_taxi_button_text = (By.XPATH, "//span[text()='Pedir un taxi']")
        self.order_taxi_button = (By.CLASS_NAME, "smart-button")
        self.order_body_window = (By.CLASS_NAME, "order-header-title")
        self.order_body_window_final = (By.CLASS_NAME, "order-btn-rating")

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_on_request_taxi_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.request_taxi_button)).click()

    def click_on_comfort_rate_icon(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.comfort_rate_icon)).click()

    def get_comfort_rate_icon_text(self):
        return self.driver.find_element(*self.comfort_rate_icon_text).text

    def select_comfort_rate(self):
        self.click_on_request_taxi_button()
        self.click_on_comfort_rate_icon()

    def click_on_phone_field(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.phone_field)).click()

    def set_phone_number(self, phone):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.phone_input)).send_keys(phone)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_field).text #Validación del número con la clase np-text

    def click_on_phone_next_button(self):
        self.driver.find_element(*self.phone_next_button).click()

    def set_phone_code(self, code):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.sms_input_code)).send_keys(code)

    def get_phone_code(self):
        return self.driver.find_element(*self.sms_input_code).get_property('value')

    def click_on_sms_confirm_button(self):
        self.driver.find_element(*self.sms_confirm_button).click()

    def set_phone_number_method(self, phone):
        self.click_on_phone_field()
        self.set_phone_number(phone)
        self.click_on_phone_next_button()

    def set_phone_code_method(self, code):
        self.set_phone_code(code)
        self.click_on_sms_confirm_button()

    def click_on_payment_method_field(self):
        self.driver.find_element(*self.payment_method_field).click()

    def add_card(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.add_card_window)).click()

    def set_card_number_and_code(self, card_number, card_code):
        self.driver.find_element(*self.card_number).send_keys(card_number)
        self.driver.find_element(*self.card_code).send_keys(card_code)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.card_code).get_property('value')

    def activate_add_button(self):
        self.driver.find_element(*self.card_second_row).click()

    def click_on_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def close_payment_method_window(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.payment_method_close_button)).click()

    def get_payment_method_text(self): #Validar pago con tarjeta
        return self.driver.find_element(*self.payment_method_field_text).text

    def set_payment_method(self, card_number, card_code):
        self.click_on_payment_method_field()
        self.add_card()
        self.set_card_number_and_code(card_number, card_code)
        self.activate_add_button()
        self.click_on_add_button()
        self.close_payment_method_window()

    def find_message_for_driver_field(self):
        message = self.driver.find_element(*self.message_driver_field)
        self.driver.execute_script("arguments[0].scrollIntoView();", message)

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.message_driver_field).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_driver_field).get_property('value')

    def set_on_slider(self):
        slider = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.slider_round))
        self.driver.execute_script("arguments[0].scrollIntoView();", slider)
        slider.click()
        time.sleep(1)

    def get_slider_status(self): #Añadido método para comprobar el estado del slider
        return self.driver.find_element(*self.slider_status).is_selected()

    def click_on_ice_cream_counter_plus(self):
        counter = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ice_cream_counter_plus))
        self.driver.execute_script("arguments[0].scrollIntoView();", counter)
        counter.click()

    def get_ice_cream_counter_value(self):
        return self.driver.find_element(*self.ice_cream_counter_value).text

    def click_on_order_taxi_button(self):
        order_taxi_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.order_taxi_button))
        self.driver.execute_script("arguments[0].scrollIntoView();", order_taxi_button)
        order_taxi_button.click()

    def get_correct_taxi_button_text(self):
        return self.driver.find_element(*self.order_taxi_button_text).text

    def show_order_body_window(self):
        try:
            order_body = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.order_body_window)
            )
            return order_body.is_displayed()
        except Exception as e:
            print(f"Error al verificar la visibilidad de la ventana: {e}")
            return False

    def show_order_body_window_final(self):
        try:
            order_body = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located(self.order_body_window_final)
            )
            return order_body.is_displayed()
        except Exception as e:
            print(f"Error al verificar la visibilidad de la ventana: {e}")
            return False