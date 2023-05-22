from django.shortcuts import render
from web3 import Web3


def home(request):
    return render(request, 'index.html')


def fetch_balance(request):
    if request.method == 'POST':
        ethereum_address = request.POST['ethereum_address']

        # Connect to the Ethereum network using Web3
        web3 = Web3(Web3.HTTPProvider(
            'https://mainnet.infura.io/v3/57a0bbe72ea74a20982fb7857b26a54c'))

        try:
            # Fetch the balance
            balance = web3.eth.get_balance(ethereum_address)

            # # Fetch the recent transactions
            transactions = web3.eth.get_transaction_by_address(
                ethereum_address)

            # Create sample transaction records

            context = {
                'balance': balance,
                # Display only the first 5 transactions
                'transactions': transactions[:5]
            }

            return render(request, 'index.html', context)

        except Exception as e:
            error_message = str(e)
            context = {
                'error': error_message
            }

            return render(request, 'index.html', context)
