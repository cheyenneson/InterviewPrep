Here are 20 detailed C/C++ technical interview questions, along with their answers, that you might encounter in a software engineering interview:

### 1. **What are the main differences between C and C++?**
   - **C** is a procedural programming language, whereas **C++** is a multi-paradigm language (supports procedural, object-oriented, and generic programming).
   - **C** does not support classes and objects, but **C++** supports both, enabling encapsulation, inheritance, and polymorphism.
   - **C++** introduces features like function overloading, templates, exception handling, and the Standard Template Library (**STL**), which are not present in **C**.
   - **C** uses `malloc()` and `free()` for dynamic memory management, while **C++** uses the `new` and `delete` operators.

### 2. **What is a pointer, and how is it different from a reference in C++?**
   - A **pointer** is a variable that stores the memory address of another variable. It can be reassigned to point to different addresses and can be `NULL`.
   - A **reference** is an alias for an existing variable. Once initialized, it cannot be changed to refer to another variable and cannot be `NULL`.
   ```cpp
   int a = 5;
   int *ptr = &a; // Pointer
   int &ref = a;  // Reference
   ```

### 3. **Explain the concept of `const` correctness in C++.**
   - `const` correctness ensures that objects or variables declared as `const` cannot be modified after initialization.
   - It can be used with variables, pointers, member functions, and function parameters to indicate immutability.
   ```cpp
   void print(const std::string &str) {
       // str cannot be modified inside this function.
   }
   ```

### 4. **What is a virtual function in C++?**
   - A **virtual function** is a member function in the base class that can be overridden in derived classes. It enables **runtime polymorphism**.
   ```cpp
   class Base {
   public:
       virtual void show() { std::cout << "Base\n"; }
   };
   class Derived : public Base {
   public:
       void show() override { std::cout << "Derived\n"; }
   };
   ```

### 5. **What is a pure virtual function?**
   - A **pure virtual function** is a function with no definition in the base class and is declared by assigning `0` to it. It makes the class an **abstract class**.
   ```cpp
   class AbstractClass {
   public:
       virtual void display() = 0; // Pure virtual function
   };
   ```

### 6. **What are the different types of inheritance in C++?**
   - **Single Inheritance:** One base class and one derived class.
   - **Multiple Inheritance:** A derived class inherits from multiple base classes.
   - **Multilevel Inheritance:** A derived class is inherited from another derived class.
   - **Hierarchical Inheritance:** Multiple derived classes inherit from a single base class.
   - **Hybrid Inheritance:** Combination of more than one type of inheritance.

### 7. **What is the `this` pointer in C++?**
   - The `this` pointer is an implicit pointer available in non-static member functions, pointing to the object invoking the function.
   ```cpp
   class MyClass {
   public:
       void show() { std::cout << "Address: " << this << '\n'; }
   };
   ```

### 8. **Explain the concept of function overloading and operator overloading.**
   - **Function Overloading:** Multiple functions can have the same name but different parameter lists (number or type of parameters).
   - **Operator Overloading:** Allows custom implementation of operators for user-defined types.
   ```cpp
   class Complex {
   public:
       Complex operator+(const Complex &c);
   };
   ```

### 9. **What is a copy constructor in C++? When is it called?**
   - A **copy constructor** is a special constructor used to create a new object as a copy of an existing object.
   ```cpp
   MyClass(const MyClass &obj);
   ```
   - It is called when:
     - An object is initialized from another object of the same class.
     - An object is passed by value to a function.
     - An object is returned by value from a function.

### 10. **What is the difference between shallow copy and deep copy?**
   - **Shallow Copy:** Copies the values of data members as they are, including pointers (copies addresses, not the data pointed to).
   - **Deep Copy:** Copies the actual data pointed to by the pointers, not just the addresses.
   ```cpp
   MyClass(const MyClass &obj) {
       data = new int;
       *data = *(obj.data);
   }
   ```

### 11. **What is a dangling pointer? How can it be avoided?**
   - A **dangling pointer** is a pointer that points to a memory location that has been freed or deleted.
   - To avoid it:
     - Set the pointer to `NULL` after deleting it.
     - Use smart pointers like `std::unique_ptr` or `std::shared_ptr`.

### 12. **What is RAII (Resource Acquisition Is Initialization)?**
   - **RAII** is a programming idiom where resources are tied to object lifetime, ensuring proper resource release.
   - For example, using a class with a destructor to manage file handles or dynamic memory ensures that resources are released when the object goes out of scope.

### 13. **Explain the differences between `new`/`delete` and `malloc()`/`free()`.**
   - **new/delete** are operators in C++ that handle object initialization and call constructors/destructors.
   - **malloc()/free()** are functions in C that only allocate and deallocate raw memory without invoking constructors or destructors.

### 14. **What is the difference between `struct` and `class` in C++?**
   - **struct** has default public access for members, while **class** has default private access.
   - Both support inheritance, polymorphism, and other OOP features.

### 15. **What are the different types of polymorphism in C++?**
   - **Compile-time Polymorphism:** Achieved through function overloading, operator overloading, and templates.
   - **Runtime Polymorphism:** Achieved through virtual functions.

### 16. **What are smart pointers in C++?**
   - Smart pointers manage memory automatically, ensuring proper cleanup:
     - **`std::unique_ptr`** - Ownership is unique; no two pointers can own the same resource.
     - **`std::shared_ptr`** - Shared ownership; reference counting is used.
     - **`std::weak_ptr`** - Used to break reference cycles with `shared_ptr`.

### 17. **What is the difference between `extern` and `static` keywords?**
   - **`extern`** declares a global variable or function in another file.
   - **`static`** limits the visibility of a variable or function to its translation unit.

### 18. **What is a segmentation fault?**
   - A **segmentation fault** occurs when a program attempts to access a memory location that it is not allowed to access (e.g., dereferencing a `NULL` or uninitialized pointer).

### 19. **Explain the term "memory leak." How can you prevent it?**
   - A **memory leak** occurs when allocated memory is not properly deallocated, causing a program to consume more memory over time.
   - Use **smart pointers** or manually ensure every `new` has a corresponding `delete`.

### 20. **What are templates in C++?**
   - **Templates** enable writing generic code that works with any data type.
   - They support **function templates** and **class templates**.
   ```cpp
   template <typename T>
   T add(T a, T b) { return a + b; }
   ``` 

These questions cover a wide range of topics in C/C++ and are commonly asked in software engineering interviews.