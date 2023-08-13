// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IdentityVerification {
    mapping(address => bool) public verifiedIdentities;

    function verifyIdentity() external {
        verifiedIdentities[msg.sender] = true;
    }
}
