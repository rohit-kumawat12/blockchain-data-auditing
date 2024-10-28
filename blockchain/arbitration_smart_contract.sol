// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ArbitrationContract {
    mapping(bytes32 => address) public arbitrationRequests;
    address public judge;

    constructor() {
        judge = msg.sender;
    }

    function requestArbitration(bytes32 challengeHash) public {
        arbitrationRequests[challengeHash] = msg.sender;
    }

    function resolveDispute(bytes32 challengeHash, bytes32 proof) public view returns (bool) {
        require(msg.sender == judge, "Only the judge can resolve disputes.");
        return true; // Simplified resolution
    }
}
