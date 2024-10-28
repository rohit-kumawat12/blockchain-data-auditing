// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SetupContract {
    mapping(bytes32 => bytes32) public integrityMetadata;

    function recordDataHash(bytes32 dataHash, bytes32 metadata) public {
        integrityMetadata[dataHash] = metadata;
    }

    function getMetadata(bytes32 dataHash) public view returns (bytes32) {
        return integrityMetadata[dataHash];
    }
}