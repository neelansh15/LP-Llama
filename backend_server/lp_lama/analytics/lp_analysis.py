from datetime import timedelta, datetime

from django.utils import timezone

from lp_lama.analytics.storage.il_computer import calculate_il
from lp_lama.analytics.storage.store_lp_rewards import LpRewardStore
from lp_lama.models import Lp


def get_lp_details(lp_id):
    lp_reward_store = LpRewardStore(lp_id)
    df = lp_reward_store.get_df()
    end_date = timezone.now().date() - timedelta(days=1)

    lp = Lp.objects.get(id=lp_id)
    data = {
        "address": lp.address,
        "chain_id": lp.exchange.chain_id,
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
        start_date = end_date - timedelta(days=days)
        start_row = df[df.index == start_date].iloc[0]
        for day in range(1, days):
            _end_date = start_date + timedelta(days=day)
            end_row = df[df.index == _end_date].iloc[0]
            reward_fee = get_lp_details_bw_dates(start_row, end_row)
            total_fee = reward_fee
            data["apy"][days_i]["x"].append(int(datetime.strptime(_end_date.strftime("%Y-%m-%d"), "%Y-%m-%d").timestamp()))
            data["apy"][days_i]["y"].append(total_fee)
            data["il"][days_i]["x"].append(int(datetime.strptime(_end_date.strftime("%Y-%m-%d"), "%Y-%m-%d").timestamp()))
            imp_loss = calculate_il(start_row.lp_token0_price, start_row.lp_token1_price, end_row.lp_token0_price, end_row.lp_token1_price)
            data["il"][days_i]["y"].append(imp_loss)
    return data


def get_lp_details_bw_dates(start_row, end_row):
    reward_fee = (end_row.reward - start_row.reward) * end_row.reward_price * end_row.lp_supply * 100 / end_row.lp_price
    return reward_fee
