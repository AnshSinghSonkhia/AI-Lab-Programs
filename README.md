# Artificial Intelligence Lab Programs

<code><img height="30" src="https://img.shields.io/badge/Python-111111?style=for-the-badge&logo=python&logoColor=39bcf7"></code>
<code><img height="30" src="https://img.shields.io/badge/Prolog-111111?style=for-the-badge&logo=prolog&logoColor=39bcf7"></code>

# Python - Lab

## Difference between List and Tuple

Here are the key differences between `lists` and `tuples` in Python:

1. **Mutability**:
   - Lists are mutable, meaning their elements can be modified after creation.
   - Tuples are immutable, meaning once they are created, their elements cannot be modified.

2. **Syntax**:
   - Lists are defined using square brackets `[ ]`.
   - Tuples are defined using parentheses `( )`.

3. **Usage**:
   - Lists are typically used to store collections of homogeneous items where the order and number of items may change.
   - Tuples are commonly used to store collections of heterogeneous items (items of different data types) where the order of items is important and should not change.

4. **Performance**:
   - Due to mutability, lists require more memory allocation and operations for modifications, making them slightly slower compared to tuples.
   - Tuples, being immutable, are more memory efficient and performant for operations that involve accessing elements.

5. **Methods**:
   - Lists have more built-in methods for manipulation, such as `append()`, `extend()`, `insert()`, `remove()`, `pop()`, etc.
   - Tuples have fewer built-in methods since they cannot be modified, but they do have methods like `count()` and `index()`.

6. **Iteration**:
   - Both lists and tuples support iteration using loops and comprehension constructs. However, since tuples are immutable, they are safer to iterate over in situations where the data should not be modified accidentally.

Remember that choosing between lists and tuples depends on the specific requirements of your program. If you need a collection that can be modified, use a list. If you need to ensure the integrity of your data or need to use it as keys in dictionaries, use a tuple.
