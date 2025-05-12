from UrbanRoutesMethods import UrbanRoutesPage
from UrbanRoutesMethods import retrieve_phone_code
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import data


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.page.set_route(address_from, address_to)
        assert self.page.get_from() == address_from
        assert self.page.get_to() == address_to

    def test_select_comfort_rate(self):
        self.page.select_comfort_rate()
        comfort_rate = self.page.get_comfort_rate_icon_text()
        assert  comfort_rate in "Comfort"

    def test_set_phone_number_method(self):
        self.page.set_phone_number_method(data.phone_number)
        assert self.page.get_phone_number() == data.phone_number

    def test_set_phone_code_method(self):
        code = retrieve_phone_code(self.driver)
        self.page.set_phone_code_method(code)
        assert self.page.get_phone_code() == code

    def test_set_payment_method(self):
        card_number = data.card_number
        card_code = data.card_code
        self.page.set_payment_method(card_number, card_code)
        assert self.page.get_card_number() == card_number
        assert self.page.get_card_code() == card_code

    def test_set_message_for_driver(self):
        message = data.message_for_driver
        self.page.find_message_for_driver_field()
        self.page.set_message_for_driver(message)
        assert self.page.get_message_for_driver() == message

    def test_set_on_slider(self):
        self.page.set_on_slider()

    def test_click_on_ice_cream_counter(self):
        self.page.click_on_ice_cream_counter_plus()
        self.page.click_on_ice_cream_counter_plus()
        counter = self.page.get_ice_cream_counter_value()
        slider_text = self.page.verify_slider_still_on()
        assert counter == '2'
        assert slider_text == 'Manta y pañuelos'

    def test_click_on_order_taxi_button(self):
        button_text = self.page.get_correct_taxi_button_text()
        self.page.click_on_order_taxi_button()
        assert button_text == 'Pedir un taxi'

    def test_show_order_body_window(self):
        try:
            assert self.page.show_order_body_window() is True
            print("La validación de la visibilidad de la ventana fue exitosa.")
        except AssertionError:
            print("Error: La validación de la visibilidad de la ventana falló.")
            raise
        except Exception as e:
            print(f"Ocurrió un error durante la prueba: {e}")
            raise
        finally:
            pass

    def test_show_order_body_window_final(self):
        try:
            assert self.page.show_order_body_window_final() is True
            print("La validación de la visibilidad de la ventana fue exitosa.")
        except AssertionError:
            print("Error: La validación de la visibilidad de la ventana falló.")
            raise
        except Exception as e:
            print(f"Ocurrió un error durante la prueba: {e}")
            raise
        finally:
            pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()