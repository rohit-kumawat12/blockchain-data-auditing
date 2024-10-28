from web3 import Web3
from solcx import compile_source

def deploy_contract(web3, contract_source_code, account):
    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol.popitem()
    contract = web3.eth.contract(
        abi=contract_interface[1]['abi'], bytecode=contract_interface[1]['bin']
    )
    tx_hash = contract.constructor().transact({'from': account})
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt.contractAddress
