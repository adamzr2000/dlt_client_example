# Import the necessary classes and functions from the web3 library for interacting with the blockchain network.
from web3 import Web3, HTTPProvider, IPCProvider
from web3.contract import ConciseContract
from web3.providers.rpc import HTTPProvider
import json

# Create a connection to the ethereum node → instance of web3
web3= Web3(Web3.WebsocketProvider("ws://127.0.0.1:7545")) 

# Load the ABI of the smart contract from a JSON file
abi_path = "../build/contracts/"
with open(abi_path+"Crud.json") as c_json:
   contract_json = json.load(c_json)
contract_abi = contract_json["abi"]

# Contract address using the mnemonic "netcom;" on Ganache
contract_address = Web3.toChecksumAddress('0xDcfd198c762dB840Ca39Cd17f8396A1a14ee9A32')

# Create an instance of the contract by passing the ABI and the address of the deployed smart contract
my_contract = web3.eth.contract(abi=contract_abi, address=contract_address)

# List of accounts available on the connected Ethereum node (Ganache)
eth_address = web3.eth.accounts

# Address of the miner (node that adds a block to the blockchain)
coinbase = eth_address[0] 

if __name__ == "__main__":
        
    print("Accounts:", eth_address)
    print("\nEtherbase:", coinbase)
    print("\nContract address:", contract_address)

    while True:
        print("\n")
        print("+------------------------------+")
        print("|  1. Add user                 |")
        print("|  2. List users               |")
        print("|  3. Modify user              |")
        print("|  4. Delete user              |")
        print("|  5. Exit                     |")
        print("+------------------------------+")
        choice = input("Enter your choice (1-5): ")
        print("\n")

        if choice == "1":
            debug_txt = input("Enter the name of the new user: ")
            # Call the create function of the contract to add a new user
            tx_hash = my_contract.functions.create(debug_txt).transact({'from': eth_address[1]})
            print("\n(Transaction) : New user added")
        
        elif choice == "2":
            users_length = my_contract.functions.length().call()
            for i in range(users_length):
                user_id, user_name = my_contract.functions.users(i).call()
                print(f"User ID: {user_id}, User Name: {user_name}")


        elif choice == "3":
            id = input("Enter the ID of the user you want to modify: ")
            new_name = input("Enter the new name of the user: ")
            tx_hash = my_contract.functions.update(int(id), new_name).transact({'from': eth_address[1]})
            print("\n(Transaction) : User name modified")

        elif choice == "4":
            id = input("Enter the ID of the user you want to delete: ")
            tx_hash = my_contract.functions.destroy(int(id)).transact({'from': eth_address[1]})
            print("\n(Transaction) : User deleted")

        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")