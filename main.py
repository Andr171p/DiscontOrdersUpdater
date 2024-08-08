from database.db_loader import create_event_loop
from database.orders_db.db_update_orders import db_loop_update_orders_data


if __name__ == "__main__":
    db_loop_update_orders_data()