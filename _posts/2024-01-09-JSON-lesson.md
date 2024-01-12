---
toc: true
comments: true
layout: post
title: JSON Concepts
description: Important Info on JSON
type: hacks
courses: { compsci: {week: 16} }
---

## JSON (JS Object Notation)
>- a text-based data format inspired by js object literal syntax
>- Easy for humans to read and write
>- Key value pairs are the fundamental building blocks where data is stored as pairs of keys and values 
<br>

{"name": "Alice", "age": 25, "isStudent": true}

<br>

>- It suppports strings, numbers, booleans, arrays, objects, and null
>- Objects: Enclosed in curly braces {}, represent a collection of key-value pairs

<br>

{"person": {"name": "Bob", "age": 30}}

<br>

>- Arrays: Ordered list of values enclosed in square brackets []

<br>

{"fruits": ["apple", "banana", "orange"]}

<br>

>- JSON is commonly used to represent structured data, such as user information

<br>

{
  "user": {
    "name": "Eve",
    "age": 28,
    "email": "eve@email.com"
  }
}

>- API (Application Programming Interface): 
- APIs enable different software systems to communicate. JSON is commonly used for data exchange in API interactions.
- HTTP Requests: APIs often use HTTP requests (GET, POST, etc.) to send and receive data.
- Response Format: APIs typically respond with JSON-formatted data.

<br>

{
  "status": "success",
  "data": {
  }
}

<br>