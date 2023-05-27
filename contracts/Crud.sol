// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/*

CRUD:

 - Create
 - Read
 - Update
 - Delete

*/
contract Crud {

  struct User {
    uint id;
    string name;
  }
  // Array of users struct
  User[] public users;
  uint public nextId = 1;

  // Add an entry to the users array
  function create(string memory name) public {
    users.push(User(nextId, name));
    nextId++;
  }
  // Read an entry 
  function read(uint id) view public returns(uint, string memory) {
    uint i = find(id);
    return(users[i].id, users[i].name);
  }
  // Update an entry
  function update(uint id, string memory name) public {
    uint i = find(id);
    users[i].name = name;
  }
  // Delete an entry
  function destroy(uint id) public {
    uint i = find(id);
    delete users[i];
  }
  
  function find(uint id) view internal returns(uint) {
    for(uint i = 0; i < users.length; i++) {
      if(users[i].id == id) {
        return i;
      }
    }
    revert('User does not exist!');
  }
  // Length of  the users array
  function length() view public returns(uint) {
    return users.length;
  }

}