# Python Class Inheritance Assignment 
![GitHub Actions](https://github.com/The-School-of-AI/epai-s22-ram/actions/workflows/python-app/badge.svg)

## Overview
This project demonstrates object-oriented programming concepts in Python, specifically focusing on inheritance patterns, multiple inheritance, and the use of `__slots__`. The project implements various classes representing academic roles (Student, Professor, Employee) with a common base class (Person).

## Features
- Single inheritance hierarchy with `Person` as base class
- Multiple inheritance demonstration with `StudentProfessor`
- Use of `__slots__` for memory optimization in `Location` class
- Comprehensive test suite using pytest
- Automated testing with GitHub Actions

## Class Structure
- `Person`: Base class with basic personal information
- `Student`: Inherits from Person, adds grade information
- `Professor`: Inherits from Person, adds course information
- `Employee`: Inherits from Person, adds department information
- `StudentProfessor`: Multiple inheritance example
- `Location`: Demonstrates `__slots__` usage

## Requirements
- Python 3.10+
- pytest

Structure of the project:

```
assignment.py
test_classes.py
```
