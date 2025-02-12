import requests
import json
from esc_wallet.serializer import WalletSerializer

def create_wallet():
    try:
        url = "http://127.0.0.1:8000/wallet/create"
        response = requests.post(url)
        wallet = WalletSerializer(data=response.json())
        wallet.is_valid(raise_exception=True)
        wallet.save()
        return wallet
    except Exception as e:
        return str(e)
