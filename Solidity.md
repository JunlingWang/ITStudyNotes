Solidity is a language for smart contract apps on Ehereum.
# IDE
Online IDE Remix:
[remix.ethereum.org](http://remix.ethereum.org/) (Chrome 打开更友好)
## Remix
### Create new file
Left hand side column/browser/Click small + to create a new file
### Find a plugin
Left hand side column/Plugin manager/search  
for example, search  
"Solidity Compiler" to find the compiler,  
"Deploy&run transaction" to run the code in a virtual machine,  

# Pragmas
Pragmas in Solidity are used to specify certain conditions under which the source file can or cannot run.  
The version pragma specifies what versions of Solidity a source file can work on.  
## Example:
> pragma solidity ^0.4.0; // This means the file can not be compiled with compilers earlier than 0.4.0 or later than 0.5.0  
> pragma solidity >=0.4.0 <0.6.0; // This means the file can not be compiled with compilers earlier than 0.4.0 or later than 0.6.0  
## Define a range of versions

# Types
int and uint (signed integer and unsigned integer)  
int (signed) 可正可负  
uint (unsigned) 只能是正数

# Comments
// This is an inline comment.

/*  
And  
this is a multi-line comment.  
*/  

# Errors
> TypeError: Data location must be "memory" for return parameter in function, but none was given  

Solution: add the keyword memory after the data type

Before:  
> string _value  

After:  
> string memory _value
