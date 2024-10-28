# Blockchain Data Auditing and Arbitration System

This project is a decentralized data auditing and arbitration system for network storage, leveraging blockchain technology. It ensures data integrity and offers a fair dispute resolution mechanism without needing third-party auditors. The project is divided into modules that handle blockchain interactions, user-side data handling, server-side storage management, and automated dispute arbitration.

## Features

- **Data Integrity Verification**: The system allows users to verify the integrity of outsourced data with cryptographic proofs stored on the blockchain.
- **Decentralized Arbitration**: A smart contract-based arbitration mechanism resolves disputes over data possession.
- **No Third-Party Auditor Required**: Uses blockchain’s immutability to achieve transparency and security.
- **Scalable Design**: Modular file structure for ease of testing, updates, and extension.

## File Structure

```
blockchain_data_auditing/
│
├── blockchain/
│   ├── contract_deployment.py        # Deploys smart contracts
│   ├── setup_smart_contract.sol      # Setup phase smart contract
│   ├── arbitration_smart_contract.sol # Arbitration phase smart contract
│   └── utils.py                      # Utility functions for blockchain interaction
│
├── server/
│   ├── storage_provider.py           # Service provider logic
│   ├── data_blocks_manager.py        # Data block management
│   ├── verification_manager.py       # Proof generation and integrity verification
│
├── user/
│   ├── user_client.py                # User interface for data handling
│   ├── data_integrity_checker.py     # Data integrity and verification
│   └── challenge_nonce_generator.py  # Challenge nonce generation
│
├── network/
│   └── blockchain_connection.py      # Blockchain connection logic
│
└── tests/
    ├── test_setup_phase.py           # Tests for setup phase
    ├── test_verification_phase.py    # Tests for verification phase
    └── test_arbitration_phase.py     # Tests for arbitration phase

```

## Setup and Installation

### Prerequisites

- Python 3.8+
- Node.js and npm (for Solidity and Web3 interactions)
- `web3.py` for blockchain interactions
- Solidity Compiler (`solc`)
- Ganache or a similar blockchain emulator for testing

### Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/blockchain_data_auditing.git
   cd blockchain_data_auditing
   ```


2. **Install required Python packages**:

```

pip install -r requirements.txt

```

3. **Compile and Deploy Smart Contracts**:

- Use the contract_deployment.py script in the blockchain folder to deploy the smart contracts.
- Adjust the contract addresses in utils.py after deployment.

4. Run Blockchain Emulator (e.g., Ganache) and connect to the local blockchain.

## Usage
### Upload Data:
The user uploads a data block to the storage provider, which generates and stores metadata on the blockchain.

###  Verify Data Integrity:
The user issues a challenge nonce to verify data integrity. The storage provider responds with a cryptographic proof, which the user verifies against the blockchain metadata.

### Arbitration:
In case of a dispute, the user can request arbitration. The smart contract verifies the data and decides the outcome.

## Running Tests
Navigate to the tests folder and run the tests to verify each phase of the system.
```
python -m unittest discover
```
- Setup Phase: Tests if data hash recording on the blockchain functions correctly.
- Verification Phase: Tests proof generation and integrity verification.
- Arbitration Phase: Tests the smart contract-based dispute resolution.

## Technologies Used
- Solidity: For writing smart contracts.
- Python: For the main codebase and interactions.
- Web3.py: For Ethereum blockchain interactions.
- Ganache: Local Ethereum blockchain for testing.