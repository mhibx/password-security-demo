# Password Security Demo

A collection of small Python tools I built to understand the fundamentals of password security and authentication.

The project started as a hands-on exercise to explore what makes a password weak or strong, how passwords are represented as hashes, and why techniques such as salting are important when storing passwords.

Rather than relying only on theoretical explanations, I built small examples and tested the concepts directly.

---

## What I Practiced

The project covers several basic password security concepts:

- Weak password identification
- Password strength evaluation
- Password hashing
- Salted password hashing
- Basic authentication security concepts

The goal is not to build a production-ready password manager or authentication system, but to better understand the security principles behind password storage and password selection.

---

## Projects

### Weak Password Checker

A simple tool for identifying passwords that match common weak-password patterns.

The exercise demonstrates why passwords based on common words, predictable patterns, or easily guessable combinations should be avoided.

### Password Strength Checker

A small tool that evaluates password characteristics such as:

- Length
- Uppercase characters
- Lowercase characters
- Numbers
- Special characters

The purpose is to understand which characteristics contribute to a stronger password.

### Password Hashing

A demonstration of how a password can be transformed into a cryptographic hash rather than being stored directly as plaintext.

This project helped me understand the difference between a plaintext password and its hashed representation, as well as why hashing is commonly used as part of password storage.

### Salted Password Hashing

An extension of the hashing exercise that introduces a unique salt before hashing a password.

This demonstrates why simply hashing passwords is not enough and how salting helps make precomputed attacks such as rainbow-table attacks less effective.

---

## Example Workflow

The exercises follow a simple progression:

**Weak Password → Password Strength → Password Hashing → Salted Password Hashing**

This progression reflects how I approached the project: first understanding password selection, then looking at how passwords are evaluated, and finally exploring how they should be handled when stored.

---

## Technologies

- Python 3
- `hashlib`
- `os`
- `re`

The project intentionally uses lightweight Python modules so that the underlying concepts remain easy to understand.

---

## What I Learned

Working through these exercises helped me understand several important password security principles:

- Passwords should never be stored as plaintext.
- A cryptographic hash is not the same thing as encryption.
- Password strength is influenced by more than just character variety.
- Adding a unique salt changes the resulting hash even when the password is the same.
- Password storage needs to account for attacks against large collections of hashed credentials.

The project also reinforced the importance of understanding the underlying security mechanism rather than simply using a library without knowing what it is doing.

---

## Limitations

This repository is intentionally educational.

The implementations are simplified examples designed to demonstrate specific concepts. They should not be treated as a complete password-storage or authentication solution for production systems.

In real applications, password storage should use a password hashing algorithm specifically designed for this purpose, together with appropriate parameters and secure application architecture.

---

## Purpose

This project is part of my cybersecurity learning portfolio.

The main objective was to strengthen my understanding of authentication and password security through small, reproducible experiments rather than relying solely on theoretical study.

---

## Disclaimer

This project is intended for educational purposes and security learning.

The examples are simplified demonstrations of password security concepts and are not intended for use as production authentication or password-storage implementations.
