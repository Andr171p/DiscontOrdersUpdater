class VisualInfo:
    def __init__(self):
        self.info_messages = InfoMessages

    def info_orders_at_the_time(self, orders):
        print(f"{self.info_messages.info_orders_at_the_time}\n"
              f"{orders}")

    def info_db_successfully_connect(self):
        print(self.info_messages.info_db_successfully_connect)

    def info_request(self, response):
        print(f"{self.info_messages.info_successfully_get_request_data}\n"
              f"{response}")


class InfoMessages:
    info_orders_at_the_time = "***************************" \
                              "[INFO] [ORDERS AT THE TIME]" \
                              "***************************"
    info_db_successfully_connect = "[INFO] [`users_orders`] [database connection successfully..]"
    info_successfully_get_request_data = "[INFO] [REQUEST DATA]"
