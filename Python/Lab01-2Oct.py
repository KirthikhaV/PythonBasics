#Task 1
# Print the Hello world.
print("Hello world")
#Print the calculation of 23+45.
print(23+45)
#Print the calculation 2345.
print(2345)

#task 2
"""
Here is a table outlining the key differences between compilation and interpretation:

| Feature                     | Compilation                                       | Interpretation                                      |
|-----------------------------|------------------------------------------------   |--------------------------------------------------|
| Definition                  | Converts the entire source code into machine code | Translates and executes the source code line by line |
                                or an intermediate code before execution.           without generating an intermediate code.  
| Process                     | Separate compilation and execution phases.        | Simultaneous compilation and execution.              |
| Intermediate Code           | May generate an intermediate code.                | Typically doesn't generate an intermediate code.     |
| Execution Speed             | Generally faster, as the entire code is optimized | May be slower as interpretation happens line by line.|
                                before execution. 
| Memory Usage                | May require more memory during compilation.       | Typically uses less memory during execution.         |
| Debugging                   | Can be challenging due to the absence of          | Easier to debug as errors are reported in the
                                    line-by-line execution.                         order they are encountered.                          |
| Portability                 | Compiled code is specific to the target platform. | Generally more portable as it can adapt to different 
                                                                                    environments during execution.                       |
| Examples                    | C, C++, Java (to bytecode), Rust.                 | Python, JavaScript, Ruby.                            |
| Error Handling              | Errors are reported after the entire code is      | Errors are reported as soon as they are encountered 
                                compiled.                                           during execution.                                    |
| Examples of Implementations | GCC, Clang, Visual C++.                           | CPython (Python), V8 (JavaScript), Ruby MRI (Ruby).  |

"""