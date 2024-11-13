Bitwise operators are used to perform bit-level operations on integer values. Here's a detailed list of all the bitwise operators, along with their properties:

### 1. **Bitwise AND (`&`)**
- **Description**: Compares each bit of the first operand to the corresponding bit of the second operand. If both bits are `1`, the resulting bit is set to `1`. Otherwise, it is set to `0`.
- **Example**: 
  - `5 & 3` (binary: `0101 & 0011`) results in `0001` (decimal: `1`).
- **Properties**:
  - **Commutative**: \( A & B = B & A \)
  - **Associative**: \( (A & B) & C = A & (B & C) \)
  - **Identity**: \( A & 0 = 0 \), \( A & 1 = A \)
  - **Idempotent**: \( A & A = A \)
  - **Absorbing element**: \( A & 0 = 0 \)
  - **Distributive over OR**: \( A & (B | C) = (A & B) | (A & C) \)

### 2. **Bitwise OR (`|`)**
- **Description**: Compares each bit of the first operand to the corresponding bit of the second operand. If either bit is `1`, the resulting bit is set to `1`. Otherwise, it is set to `0`.
- **Example**: 
  - `5 | 3` (binary: `0101 | 0011`) results in `0111` (decimal: `7`).
- **Properties**:
  - **Commutative**: \( A | B = B | A \)
  - **Associative**: \( (A | B) | C = A | (B | C) \)
  - **Identity**: \( A | 0 = A \)
  - **Idempotent**: \( A | A = A \)
  - **Absorbing element**: \( A | -1 = -1 \)
  - **Distributive over AND**: \( A | (B & C) = (A | B) & (A | C) \)

### 3. **Bitwise XOR (`^`)**
- **Description**: Compares each bit of the first operand to the corresponding bit of the second operand. The resulting bit is set to `1` if the bits are different, and `0` if they are the same.
- **Example**:
  - `5 ^ 3` (binary: `0101 ^ 0011`) results in `0110` (decimal: `6`).
- **Properties**:
  - **Commutative**: \( A ^ B = B ^ A \)
  - **Associative**: \( (A ^ B) ^ C = A ^ (B ^ C) \)
  - **Identity**: \( A ^ 0 = A \)
  - **Inverse**: \( A ^ A = 0 \)
  - **Self-inverse**: \( A ^ B ^ B = A \)
  - **Distributive over AND and OR**:
    - \( A ^ (B & C) = (A ^ B) & (A ^ C) \)
    - \( A ^ (B | C) = (A ^ B) | (A ^ C) \)

### 4. **Bitwise NOT (`~`)**
- **Description**: Inverts all the bits of the operand (i.e., changes `1` to `0` and `0` to `1`).
- **Example**: 
  - `~5` (binary: `~0101`) results in `1010` (in a signed 4-bit system, this would be `-6`).
- **Properties**:
  - **Involution**: \( ~~A = A \) (applying NOT twice returns the original value)
  - **Complement**: Converts a positive integer to its negative counterpart using two's complement representation.
  - **Relation with XOR**: \( ~A = A ^ -1 \)

### 5. **Bitwise Left Shift (`<<`)**
- **Description**: Shifts all bits in the operand to the left by the specified number of positions. Bits shifted out on the left are discarded, and `0`s are shifted in from the right.
- **Example**:
  - `5 << 2` (binary: `0101 << 2`) results in `10100` (decimal: `20`).
- **Properties**:
  - **Equivalent to multiplication by powers of 2**: \( A << n = A \times 2^n \)
  - **No overflow in Python**: Python integers have arbitrary precision, so shifting left won't cause overflow as it would in languages with fixed-width integers (e.g., C/C++).

### 6. **Bitwise Right Shift (`>>`)**
- **Description**: Shifts all bits in the operand to the right by the specified number of positions. For positive integers, bits shifted in from the left are `0`s (logical shift). For negative integers in languages with signed integers, bits shifted in from the left match the sign bit (arithmetic shift).
- **Example**:
  - `20 >> 2` (binary: `10100 >> 2`) results in `0101` (decimal: `5`).
- **Properties**:
  - **Equivalent to division by powers of 2**: \( A >> n = A \div 2^n \) (integer division)
  - **Sign extension for negative numbers**: Preserves the sign bit for signed integers (arithmetic shift).

### Summary of Bitwise Operator Properties:

| Operator | Commutative | Associative | Identity | Inverse | Idempotent | Distributive over Other Ops |
|----------|-------------|-------------|----------|---------|------------|-----------------------------|
| `&`      | Yes         | Yes         | `A & 1 = A` | No      | Yes        | Yes (`&` over `|`)         |
| `|`      | Yes         | Yes         | `A | 0 = A` | No      | Yes        | Yes (`|` over `&`)         |
| `^`      | Yes         | Yes         | `A ^ 0 = A` | Yes     | No         | Yes                         |
| `~`      | No          | No          | N/A        | Yes     | No         | No                          |
| `<<`     | No          | No          | N/A        | No      | No         | N/A                         |
| `>>`     | No          | No          | N/A        | No      | No         | N/A                         |

These operators are often used in low-level programming, optimization, encryption algorithms, and data compression techniques due to their efficiency in handling binary data.