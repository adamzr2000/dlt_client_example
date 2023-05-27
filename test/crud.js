const Crud = artifacts.require('Crud.sol');

contract('Crud', () => {
    let crud = null;
    before(async () => {
        crud = await Crud.deployed();
    });    

    it('Should create a new user', async() => {
        await crud.create('Frank');
        const user = await crud.read(1);
        assert(user[0].toNumber() === 1);
        assert(user[1] === 'Frank');
    });   

    it('Should update an user', async() => {
        await crud.update(1,'Adam');
        const user = await crud.read(1);
        assert(user[0].toNumber() === 1);
        assert(user[1] === 'Adam');
    });  
    // Test ERRORS
    it('Should NOT update a non-existing user', async() => {
        try {
            await crud.update(2,'Maria'); // Not exists
        } catch (e) {
            assert(e.message.includes('User does not exist!'));

            return;
        }
        assert(false);
    });      

    it('Should delete an user', async() => {
        await crud.destroy(1);
        try {
            await crud.read(1);
        } catch (e) {
            assert(e.message.includes('User does not exist!'));

            return;
        }
        assert(false);
    });
    
    it('Should NOT delete a non-existing user', async() => {
        try {
            await crud.destroy(10);
        } catch (e) {
            assert(e.message.includes('User does not exist!'));

            return;
        }
        assert(false);
    });     

});