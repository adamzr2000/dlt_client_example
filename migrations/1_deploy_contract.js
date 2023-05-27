const AdvancedStorage = artifacts.require('AdvancedStorage.sol');
const Hero = artifacts.require('Hero.sol');
const Crud = artifacts.require('Crud.sol');

module.exports = function (deployer) {
    //deployer.deploy(AdvancedStorage);
    //deployer.deploy(Hero);
    deployer.deploy(Crud);

};