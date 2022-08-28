import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from lp_lama.analytics.storage.store_timestamp_to_blocks import BlockTimestamp

logger = logging.getLogger(__name__)


@api_view(['GET'])
def store_date_to_block(request):
    chain_id = int(request.query_params['chain_id'])
    logger.info(f"In store_date_to_block: {chain_id=}")
    BlockTimestamp(chain_id).store_date_to_block()
    return Response(status=status.HTTP_200_OK)
