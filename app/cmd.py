import asyncio
import typer
import logging

from database.manage import init_models

from app.settings import AppLogs


cli = typer.Typer()

logging.basicConfig(level=logging.INFO)


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    logging.info(AppLogs.init_models_log)
