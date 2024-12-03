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


Let's break down each of your questions in detail.

### 1. **How does the concept of a reference differ in C++ and Rust, and how do these differ from a pointer in C?**

#### **C++ References:**
- A **reference** in C++ is an alias for an existing variable. Once a reference is assigned to a variable, it cannot be changed to refer to another variable. It must be initialized when declared.
- References are syntactically similar to pointers but do not require dereferencing (i.e., you use the variable as if it were a direct alias).
- References cannot be `NULL` and cannot be reassigned after initialization, making them safer and easier to use compared to pointers.
  ```cpp
  int a = 10;
  int &ref = a; // ref is now an alias for a
  ref = 20; // This changes the value of a to 20
  ```

#### **Rust References:**
- In **Rust**, references (`&T` for an immutable reference, `&mut T` for a mutable reference) allow you to refer to a value without taking ownership of it.
- Rust's references are more restrictive compared to C++:
  - **Borrow Checker**: Rust enforces strict borrowing rules at compile time to ensure memory safety. You can have multiple immutable references (`&T`) or a single mutable reference (`&mut T`) to a value, but not both simultaneously.
  - References in Rust are not nullable, eliminating the concept of `NULL` pointers.
  - Lifetimes (`'a`) are used to ensure references are valid for a certain scope, which prevents dangling references.
  ```rust
  let x = 5;
  let r = &x; // Immutable reference
  let mut y = 10;
  let mr = &mut y; // Mutable reference
  ```

#### **C Pointers:**
- A **pointer** in C is a variable that stores the memory address of another variable.
- Pointers are highly flexible but also prone to errors:
  - They can be `NULL`, leading to potential segmentation faults if dereferenced without checking.
  - They can point to any type of data, and you can perform arithmetic on them (e.g., pointer increment).
  - Pointers do not have the same safety guarantees as references in C++ or Rust, meaning issues like dangling pointers, buffer overflows, and memory leaks are more common.
  ```c
  int a = 10;
  int *ptr = &a; // ptr points to the address of a
  *ptr = 20; // This changes the value of a to 20
  ```

#### **Key Differences:**
| Feature            | C++ References | Rust References | C Pointers          |
|--------------------|----------------|-----------------|---------------------|
| Nullability        | No             | No              | Yes                |
| Reassignable       | No             | No              | Yes                |
| Requires Dereferencing | No         | No              | Yes                |
| Memory Safety      | Somewhat       | High (Compile-time) | Low              |
| Compile-time Checks | Minimal       | Extensive       | None               |

---

### 2. **C `struct`s vs. C++ Classes and Why C is Not OOP**

#### **C `struct`s:**
- In **C**, `struct`s are used to group variables (called members) under a single name. They do not support **methods**, **inheritance**, or **polymorphism**.
- C `struct`s only contain data; they do not have member functions, constructors, destructors, or access specifiers (`public`, `private`, etc.).
  ```c
  struct Person {
      char name[50];
      int age;
  };
  ```

#### **C++ Classes:**
- In **C++**, `struct`s and `classes` are very similar but differ in their default access specifiers:
  - `struct`: Members are `public` by default.
  - `class`: Members are `private` by default.
- C++ `classes` support **object-oriented programming** features such as:
  - **Encapsulation** (using access specifiers)
  - **Inheritance** (base and derived classes)
  - **Polymorphism** (using virtual functions)
  ```cpp
  class Person {
  private:
      std::string name;
      int age;
  public:
      void setName(std::string n) { name = n; }
      std::string getName() { return name; }
  };
  ```

#### **Why C is Not Considered OOP:**
- **C** is considered a **procedural language** because it does not natively support the concepts of **encapsulation**, **inheritance**, or **polymorphism**, which are key to Object-Oriented Programming (OOP).
- `struct`s in C are just collections of data members, not entities with behaviors (i.e., methods).
- There are no features for defining methods within `struct`s or for establishing relationships like inheritance between data types.

---

### 3. **Can C use references, or is that only in C++? Can C++ use both references and pointers?**

- **C does not support references** as a language feature. It only uses pointers for indirection.
  ```c
  void increment(int *a) {
      (*a)++;
  }
  ```
  - The above C function uses pointers to modify the value at the address passed in.

- **C++ supports both references and pointers**.
  - References are generally used when you want to pass objects by reference but with safer syntax and semantics.
  - Pointers are more flexible but also riskier, useful when you need features like dynamic memory allocation, array manipulation, or when interfacing with low-level system components.

  ```cpp
  void increment(int &a) { // Reference in C++
      a++;
  }

  void increment(int *a) { // Pointer in C++
      (*a)++;
  }
  ```

---

### 4. **Is there a difference between how `const` is used in C versus C++?**

- **In C**:
  - `const` is primarily used to indicate that a variable's value cannot be modified after initialization.
  - You can have `const` pointers, which means the pointer itself or the data it points to (or both) can be `const`.
  - `const int *ptr` means the value pointed to cannot be changed, but the pointer itself can point to a different address.
  - `int *const ptr` means the pointer cannot point to another address, but the value at that address can be modified.
  ```c
  const int a = 10; // a is read-only
  ```

- **In C++**:
  - `const` behaves similarly to C but is more versatile due to object-oriented features.
  - You can have `const` member functions in classes, which promise not to modify the object's state.
    ```cpp
    class MyClass {
    public:
        void show() const { // Cannot modify any member variables
            std::cout << "Show" << std::endl;
        }
    };
    ```
  - `const` can also be used with references, templates, and `constexpr` for compile-time constants.
  - C++ introduces `const_cast` to cast away the `const`ness of variables, which is not available in C.

| Feature                          | C                   | C++                          |
|----------------------------------|---------------------|------------------------------|
| Read-only variables              | Yes                 | Yes                          |
| `const` pointers                 | Yes                 | Yes                          |
| `const` member functions         | No                  | Yes                          |
| `constexpr` (compile-time const) | No                  | Yes (since C++11)            |
| `const_cast`                     | No                  | Yes                          |

These nuanced differences highlight the evolution from C to C++, where C++ builds on C's features with enhanced capabilities like references, object-oriented programming, and stricter type safety.