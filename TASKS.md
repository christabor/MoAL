## Long term engineering learning path aka “MOAL” - Mother of All Learning

Mostly taken from: https://www.quora.com/What-is-the-best-way-to-self-teach-the-skills-and-knowledge-gained-in-a-typical-computer-science-degree/answer/Sam-Park-1?srid=dDmF&share=1

**THIS SHOULD ALL BE DONE IN PYTHON, EXCEPT FOR SPECIFIC LANGUAGE GOALS!
Also: things that are math oriented, should still be done IN an actual language -- utilize tools like numpy, scipy to do different types of math.**

Some examples are taken and recreated from other sites. To learn, you should still manually
recreate each example, so you can get a better intuition and memorization of how it works and how to do it.

In some cases, direct programming makes little sense, since a given subject may be high level. However, to better understand and cement the idea, it's important to try and recreate it in code. For example, you can learn about memory, but to "grok" it, you could write a module that acts as if it was memory - with the same kind of properties.

**This should be considered a living document, that may grow in size as new details and fields of study are added**

## Strategy: "20 minutes a day"
Taken from: http://www.quora.com/What-small-lifestyle-changes-have-the-biggest-impact/answer/Evan-DeFilippis?srid=dDmF&share=1

# Specific tasks
_Note:_ *completed tasks will be ~~crossed out~~*

### Fundamentals

+ ~~Try building a larger OOP-style project involving multiple classes.~~
+ Become familiar with some basic data structures/algorithms:
 + Data structures
   + ~~Arrays~~
   + ~~Linked lists~~
   + ~~Binary Search Trees~~
    + Heaps
    + Hash table
    + Fractal Tree Index
    + Red-black trees
    + ~~AVL trees~~
    + Priority queues
   + Stack frames
   + ~~Stacks~~
   + Queues/Deques
   + Splay trees
   + Graph
   + Skip list
   + Trie
 + Sorting algorithms
   + Insertion sort
    + Merge sort
    + Quick sort
    + Radix sort
    + Bubble Sort
    + Selection Sort
    + Insertion Sort
    + Shell Sort
 + ~~Big O analysis~~
  + ~~O(1)~~
  + ~~O(logN)~~
  + ~~O(n)~~
  + ~~O(n logN)~~
  + ~~O(n^2)~~
  + ~~O(2^n)~~
  + ~~O(n!)~~
+ Discrete math:
 + Basic probability
 + Basic number theory
 + Set theory (notions of countably infinite vs. non-countably infinite)
 + Automata theory/finite state machines
+ Engineering
  + Testing
    + Test matrices
    + Testing libraries
  + Problem solving
    + Decomposition

### Algorithms

+ Greedy algorithms
+ Dynamic programming
+ Divide and conquer
+ Standard graph algorithms
 + Shortest path
 + Max flow
 + MST
 + Shortest Path Problems
 + Dijkstra’s Algorithm
 + Knight’s Tour Problem
 + The Word Ladder Problem
 + DFS/BFS
 + An Adjacency Matrix
 + An Adjacency List
 + Prim’s Spanning Tree Algorithm
 + Building the Word Ladder Graph
 + Topological Sorting
 + Strongly Connected Components

*Optional reading: Introduction to Algorithm Design by Jon Kleinberg and Eva Tardos, or Introduction to Algorithms CLRS (MIT).*

### Computer Organization

+ How a computer works
 + Starting with transistors
 + Logic gates
 + Data(types)
   + Hexadecimal
   + Octal
   + Binary
   + Ternary
   + N-ary
 + Math
  + Boolean logic
 + Bitwise operations
 + ALU
 + A basic CPU
 + Caches
 + Memory hierarchy
 + Virtual memory
 + Synchronization primitives
 + Assembly languages
  + ARM
  + MIPS
  + x86
  + 6502
 + Virtual memory
 + Memory mapped I/O

### Operating Systems

+ Concurrency
 + Futures/Promises
 + Semaphores
 + Primitives
  + Co-routines
  + Fibers
  + Green threads
 + Scheduling
 + Single reader multiple writer
 + Barrier
 + Producer / consumer
 + Dining philosophers
+ Memory management
+ Networking
 + Ethernet
 + IP/TCP
 + UDP
 + SSH
+ File systems
+ Security

### Advanced

+ More algorithms/data structures
 + Spectral graph theory
 + Linear programming/duality
+ Advanced data structures (ex. persistent data structures)
 + Approximation algorithms
+ Databases
  + Relational
    + Mysql
    + Postgresql
  + Key/value
    + Redis (doc + k/v)
  + Document
    + ElasticSearch
    + Solr
    + MongoDB
    + CouchDB
  + Cache
    + Memcached
  + Graph
    + Neo4j
  + WideColumn
    + HBase
    + BigTable
+ Apps/Services
  + Architecture
    + MVC/N-Tier
    + SOA
    + Microservices
    + Message queuing
      + RabbitMQ
      + ZeroMQ
    + HTTP Servers
      + Gunicorn
      + UWGSGI
    + FTP Server
      + Twisted FTP
    + UDP
      + Twisted UDP
    + Load balancing
      + NGINX
      + Apache
      + HAProxy
    + RESTful API
      + Full HATEOAS
  + Protocols
    + JSONRPC
    + XMLRPC
  + Caching
    + Varnish
+ Distributed Systems
  + CAP Theorem
  + Big Data
    + Hadoop file system
    + Hadoop MapReduce
    + PIG
    + ZooKeeper
    + Lucene
+ Machine learning
  + Supervised learning
    + Decision trees
    + Perceptrons
    + Support vector machines
    + K-means clustering
    + Bayesian probability
    + Neural networks
      + Recurrent neural networks
+ Robotics
+ Theory of Computation
+ (various) automata
+ Context-free languages
+ Complexity classes (P, NP, #P, BPP, PSPACE)
+ PCPs,
+ Circuit lower bounds
+ Arithmetic complexity
+ Quantum complexity
+ Communication complexity
+ Unique Games Conjecture and its relation to optimality of approximation algorithms
+ Syntactic sugar (format: Language - feature)
  + Python - yield
  + Python - decorator
  + Python - context manager
  + Python - variable packing/unpacking
+ Programming Paradigms:
 + Functional programming
    + Haskell
    + OCaml
    + Lisp
    + Clojure
 + Logic programming
    + Prolog
 + OOP
    + java
   + python
 + Array programming
   + J
 + Metaprogramming
 + Template metaprogramming
 + Automatic programming
 + Reactive programming
 + Dataflow programming
+ Theorem provers
+ Verified computation
+ Type systems
+ Concurrency languages
 + GO
 + Rust
+ Language based security
+ Software defined networking
+ Compilers:
 + Building one
+ Computer Graphics
+ Computational geometry
+ Scientific Computation
+ Cryptography and security
 + Diffie-Hellman
 + RSA
 + Zero-knowledge proofs

### Other resources / references

#### Requirements list for BCS
http://en.wikipedia.org/wiki/Bachelor_of_Computer_Science

#### Other resources
http://en.wikipedia.org/wiki/Analysis#Computer_science
http://en.wikipedia.org/wiki/Programming_paradigm
http://en.wikipedia.org/wiki/NoSQL
http://en.wikipedia.org/wiki/Evaluation_strategy
http://en.wikipedia.org/wiki/Machine_learning
http://www.fullstackpython.com/table-of-contents.html
http://interactivepython.org/
http://refactoring.com/catalog/
