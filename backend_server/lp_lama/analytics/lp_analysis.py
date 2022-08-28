from datetime import timedelta, datetime

from django.utils import timezone

from lp_lama.analytics.storage.store_lp_rewards import LpRewardStore
from lp_lama.models import Lp


def get_lp_details(lp_id):
    lp_reward_store = LpRewardStore(lp_id)
    df = lp_reward_store.get_df()
    end_date = timezone.now().date()
    fee = get_fee(lp_id)
    lp = Lp.objects.get(id=lp_id)
    data = {
        "token0": lp.token0,
        "token1": lp.token1,
        "tvl": df.iloc[-1].lp_price,
        "token_reserve0": df.iloc[-1].reserve0,
        "token_reserve1": df.iloc[-1].reserve1,
        "exchange": lp.exchange.name,
        "apy": [{"x": [], "y": []}, {"x": [], "y": []}],
        "il": [{"x": [], "y": []}, {"x": [], "y": []}]
    }
    for days_i, days in enumerate([7, 30]):
        start_date = end_date - timedelta(days=7)
        for day in range(1, days+1):
            _end_date = start_date + timedelta(days=day)
            reward_fee = get_lp_details_bw_dates(df, start_date, end_date)
            total_fee = fee*day + reward_fee
            data["apy"][days_i]["x"].append(int(datetime.strptime(_end_date.strftime("%Y-%m-%d"), "%Y-%m-%d").timestamp()))
            data["apy"][days_i]["y"].append(total_fee)
            data["il"][days_i]["x"].append(int(datetime.strptime(_end_date.strftime("%Y-%m-%d"), "%Y-%m-%d").timestamp()))
            data["il"][days_i]["y"].append(0.003)
    return data


def get_lp_details_bw_dates(df, start_date, end_date):
    start_row = df[df.index == start_date].iloc[0]
    end_row = df[df.index == end_date].iloc[0]
    reward_fee = (end_row.reward - start_row.reward) * end_row.reward_price * end_row.lp_supply * 100 / end_row.lp_price
    return reward_fee


def get_fee(lp_id):
    if lp_id == 1:
        fee = 2.09
    elif lp_id == 2:
        fee = 6.59
    elif lp_id == 3:
        fee = 1.86
    elif lp_id == 4:
        fee = 1.73
    else:
        fee = 2
    return fee / 365
