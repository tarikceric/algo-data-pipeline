import datetime
import logging
import sys
from typing import Any, Dict, List, Optional

import psycopg2.extras as p
import requests

from algopipeline.utils.db import WarehouseConnection
from algopipeline.utils.sde_config import get_warehouse_creds

# using vestige app: https://api.tinychart.org

# #gets all assets with some data but not price
# request_all_assets = f'{BASE_URL}/assets'
# all_assets_response = requests.get(request_all_assets).json()
#
# #get current coin price in usd
# asset_id = "388502764"
# request_price = f'{BASE_URL}/asset/{asset_id}/price'
# price_response = requests.get(request_price).json()
#
# # get providers
# request_exchanges = f'{BASE_URL}/providers'
# exchanges_response = requests.get(request_exchanges).json()


def get_exchange_data() -> List[Dict[str, Any]]:
    url = 'https://free-api.vestige.fi/providers'
    try:
        request = requests.get(url)
    except request.ConnectionError as e:
        logging.error(f"There was an error with the request, {e}")
        sys.exit(1)
    return request.json()

def add_utc_time (exchange_data: List):
    for exchange in exchange_data:
        exchange['utc_dt'] = datetime.datetime.utcnow()
    return exchange_data


def _get_exchange_insert_query() -> str:
    return '''
    INSERT INTO algo.exchange (
        exchangeid,
        name,
        url,
        active,
        volumedaily,
        totalvaluelocked,
        dt
    )
    VALUES (
        %(id)s,
        %(name)s,
        %(url)s,
        %(active)s,
        %(volume24h)s,
        %(tvl)s,
        %(utc_dt)s
    );
    '''


def run() -> None:
    data_wo_time = get_exchange_data()
    data = add_utc_time(data_wo_time)

    # get the warehouse connection credentials using 'get_warehouse_creds' util and pass to WarehouseConnection class
    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        p.execute_batch(curr, _get_exchange_insert_query(), data)


if __name__ == '__main__':
    run()
