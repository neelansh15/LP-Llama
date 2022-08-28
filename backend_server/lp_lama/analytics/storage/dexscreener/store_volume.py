import logging

logger = logging.getLogger(__name__)


def get_data_from_chart_url(self, chart_url: str):
    logger.info("Fetching data from dexscreener")
    headers = {
        # "Host": "io.dexscreener.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        # "Accept-Language": "en-US,en;q=0.5",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Alt-Used": "io.dexscreener.com",
        "Connection": "keep-alive",
        # "Upgrade-Insecure-Requests": "1",
        # "Sec-Fetch-Dest": "document",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "none",
        # "Sec-Fetch-User": "?1",
        # "TE": "trailers"
    }
    url = f"https://io.dexscreener.com/u/chart/bars/{chart_address}"
    chart_url = f"{self.url}?from={dex_timestamp}&to={dex_timestamp}&res={dex_timeframe}&cb={num_of_bars}"
    response = self.session.get(chart_url, headers=headers)
    logger.info("Fetched data from dexscreener")
    # self.dex_io = max((self.dex_io + 1) % 10, 3)
    try:
        json_resp = response.json()
    except Exception as error:
        logger.error(f"{response.text=}")
        breakpoint()
        raise error
    return json_resp
