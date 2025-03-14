import argparse
from ankr import AnkrAdvancedAPI

# Initialize Ankr API Client
API_KEY = "your_api_key_here"
api_client = AnkrAdvancedAPI(api_key=API_KEY)

def get_account_balance(wallet_address, blockchain):
    """Fetch account balance for a given wallet."""
    try:
        request = {"walletAddress": wallet_address, "blockchain": blockchain}
        response = api_client.get_account_balance(request)
        return list(response) if response else "No balance found."
    except Exception as e:
        return f"Error fetching balance: {str(e)}"

def get_token_price(token_symbol):
    """Fetch token price."""
    try:
        request = {"symbol": token_symbol}
        response = api_client.get_token_price(request)
        return response if response else "No price data found."
    except Exception as e:
        return f"Error fetching token price: {str(e)}"

def get_transactions(wallet_address, blockchain):
    """Fetch transactions for a given wallet."""
    try:
        request = {"walletAddress": wallet_address, "blockchain": blockchain}
        response = api_client.get_transactions_by_address(request)
        return list(response) if response else "No transactions found."
    except Exception as e:
        return f"Error fetching transactions: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Crypto CLI Bot")
    parser.add_argument("command", choices=["balance", "price", "transactions"], help="Choose a command to execute")
    parser.add_argument("--wallet", type=str, help="Wallet address")
    parser.add_argument("--token", type=str, help="Token symbol")
    parser.add_argument("--blockchain", type=str, default="eth", help="Blockchain name (default: eth)")

    args = parser.parse_args()

    if args.command == "balance":
        if not args.wallet:
            print("Wallet address is required for balance lookup.")
        else:
            result = get_account_balance(args.wallet, args.blockchain)
            print(result)

    elif args.command == "price":
        if not args.token:
            print("Token symbol is required for price lookup.")
        else:
            result = get_token_price(args.token)
            print(result)

    elif args.command == "transactions":
        if not args.wallet:
            print("Wallet address is required for transactions lookup.")
        else:
            result = get_transactions(args.wallet, args.blockchain)
            print(result)

if __name__ == "__main__":
    main()
