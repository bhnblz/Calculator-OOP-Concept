# Description
A Python program that will use the OOP concept to develop a simple calculator in which users will be prompted to select whatever operations they require.

## How to run the code
To run this program, follow this instruction
    
1. The program will ask the user to input an operation.
2. The user will be asked again to input two integers or numbers.
3. The answer will be displayed.
4. After that, the program will ask the user if they want to solve another calculation; if yes, then the user will be asked again to input operations and numbers, but if no, then the program will exit.
5. If by any chance the user inputs the wrong operation, the program will display "Error: Invalid operation" and then ask again for another operation.
6. If the user inputs an invalid value, then the program will display "Error: Invalid input" and ask again for the operation and a new input value.
7. Furthermore, if the user chooses to perform a division operation and inputs a 0 value as the second integer, the program will display "Error: Cannot divide by zero" and will ask again for the new operation and integer value.

## How the program looks like
Command interface where all the methods for inputs, such as operations, integers, and answers, are stored.

![interface](https://github.com/bhnblz/Calculator-OOP-Concept/assets/129713527/e323cb1b-91bc-4fbb-9f3c-0e4a3be21016)

Calculator file, where all the methods for calculations that need to be performed are stored.

![calc](https://github.com/bhnblz/Calculator-OOP-Concept/assets/129713527/1018705a-078a-4e97-acc3-714b3db94464)

In this main file (simple_calculator), all the methods in the other files are called, and in this file, the output will be displayed.

![main](https://github.com/bhnblz/Calculator-OOP-Concept/assets/129713527/37d99ea4-3514-4d58-8f25-d9cdcec8810b)
