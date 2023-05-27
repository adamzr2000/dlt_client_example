# Description
This repo contains a simple Python menu to interact with a smart contract. In this example, the smart contract (Crud.sol) implements basic CRUD operations (Create, Read, Update, Delete) for a user struct.

To test the code, we are going to create a local blockchain network (Ethereum), deploy the Crud.sol smart contract in that network, and interact with it using the web3.py library.

## Ethereum Smart Contracts
*A smart contract is a self-executing agreement that is encoded on a blockchain platform. It contains predefined rules and conditions that automatically execute and enforce transactions or actions when specific conditions are met. Smart contracts eliminate the need for intermediaries and ensure transparency, security, and immutability of the agreement. They are typically used in decentralized applications (DApps) and enable trustless and efficient interactions between parties without relying on a central authority*

[More information about ethereum and smart contracts](https://www.quicknode.com/guides/ethereum-development/smart-contracts/how-to-write-an-ethereum-smart-contract-using-solidity/)

## Installation
In order to deploy and interact with a smart contract you need to install the following tools:

- nodejs: [How to Install Node.js on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04)
- Truffle:
```
npm install -g truffle
```

*Truffle is a development framework for Ethereum-based blockchain applications. It provides a suite of tools that allows developers to write, test, and deploy smart contracts on the Ethereum network*

- Ganache: 
```
npm install -g ganache-cli
```

*Ganache is a personal blockchain for Ethereum development that allows developers to create a local Ethereum network for testing and development purposes. Developers can create multiple accounts with pre-funded Ether and use them to interact with their smart contracts, test different scenarios, and debug their code.*

- web3.py:
```
pip install web3
```

*Web3 is a library to interact with a smart contract on the ethereum blockchain*

## Compile & Deploy the Smart Contract to the Blockchain Network

1. Start Ganache server on this url: **https://localhost:7545**
```
ganache-cli --host 127.0.0.1 --port 7545 --mnemonic "netcom;"
```

*The menomonic is used to always have the same ethereum addresses for testing*

2. Compile & Deploy the smart contract:
```
truffle migrate
```   

## Other useful commands:
- Compile the smart contract:
```
truffle compile
```
- Test the smart contract:
```
truffle test
```

## Interact with the smart contract using web3.py library
```
cd python_code
python3 app.py
```
Simple menu in python that allows calling the main functions of the smart contract:
 - Create
 - Read
 - Update
 - Delete


