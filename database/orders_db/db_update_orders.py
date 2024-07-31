import asyncio

from client.order_status import OrdersAtTheMoment

from database.orders_db.db_orders_manage import OrdersEngineDB
from database.db_config import SettingsDB


async def db_loop_update_orders_data(timeout=SettingsDB.update_timeout):
    # init orders database engine class:
    orders_engine_db = OrdersEngineDB()
    # init orders at the moment class:
    orders_at_the_moment = OrdersAtTheMoment()
    # first orders transaction:
    orders = await orders_at_the_moment.orders_at_the_moment()
    await orders_engine_db.db_insert_orders_data(orders=orders)
    # start update database:
    while True:
        new_orders = await OrdersAtTheMoment().orders_at_the_moment()
        await orders_engine_db.db_update_orders_data(orders=new_orders)
        # wait timeout:
        await asyncio.sleep(timeout)