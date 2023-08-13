const hre = require("hardhat");

async function main() {
  const IdentityVerification = await hre.ethers.getContractFactory("IdentityVerification");
  const identityVerification = await IdentityVerification.deploy();

  await identityVerification.deployed();

  console.log("IdentityVerification contract deployed to:", identityVerification.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
