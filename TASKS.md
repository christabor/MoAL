# Tasks

## Fundamentals

+ [~~Try building a larger OOP-style project involving multiple classes.~~](fundamentals/oop_classes.py)
+ Become familiar with some basic data structures/algorithms:
  + Data structures
    + [~~Arrays~~](fundamentals/array_and_linked_lists.py)
      + Suffix arrays
      + Judy arrays
    + [~~Linked lists~~](fundamentals/arrays_and_linked_lists.py)
    + Doubly-connected edge list
    + Disjoint-set/union-find/merge-find ADT
    + Winged edge
    + Quad edge
    + [~~Heaps~~](fundamentals/heaps.py)
    + [~~Hash table~~](fundamentals/hashtable.py)
    + Bloom filters
    + [~~Stacks~~](fundamentals/stack.py)
      + [~~Stack frames~~](fundamentals/stack_frame.py)
    + [~~Queue~~](fundamentals/queues.py)
      + [~~Double-ended queue~~](fundamentals/queues.py)
      + [~~Priority queue~~](fundamentals/queues.py), ([stdlib](fundamentals/queues_stdlib.py))
    + Trees
      + BSP Tree
        + K-dimensional tree
      + Fractal tree index
      + Interval tree
      + [~~Binary search tree~~](fundamentals/binary_search_trees.py)
      + Binary indexed tree
      + [~~Splay tree~~](fundamentals/splay_trees.py)
      + vEB tree
      + Red-black tree
      + [~~AVL tree~~](fundamentals/avl_trees.py)
    + [~~Graph~~](fundamentals/graphs.py)
      + DAWG/DAFSA
    + Concurrent trie (Ctrie)
    + [~~Skip lists~~](fundamentals/skip_lists.py)
    + [~~Trie~~](fundamentals/trie.py)
      + Suffix tree
      + Hash array mapped tries (HAMT)
  + Sorting algorithms
    + [~~Insertion sort~~](fundamentals/sorting/insertion_sort.py)
    + [~~Merge sort~~](fundamentals/sorting/merge_sort.py)
    + [~~Quick sort~~](fundamentals/sorting/quick_sort.py)
    + Splay sort
    + Heap sort
    + Radix sort
      + MSD
      + Adaptive
      + MBM
      + Forward
    + [~~Bubble Sort~~](fundamentals/sorting/bubble_sort.py)
    + [~~Bogo Sort (anti-pattern)~~](fundamentals/sorting/bogo_sort.py)
    + Burst sort
    + [~~Selection Sort~~](fundamentals/sorting/selection_sort.py)
    + [~~Shell Sort~~](fundamentals/sorting/shell_sort.py)
 + Big O analysis
  + [~~O(1)~~](fundamentals/big_o.py)
  + [~~O(logN)~~](fundamentals/big_o.py)
  + [~~O(n)~~](fundamentals/big_o.py)
  + [~~O(n logN)~~](fundamentals/big_o.py)
  + [~~O(n^2)~~](fundamentals/big_o.py)
  + [~~O(2^n)~~](fundamentals/big_o.py)
  + [~~O(n!)~~](fundamentals/big_o.py)
+ Discrete math:
 + Basic probability
 + Basic number theory
 + [~~Set theory (notions of countably infinite vs. non-countably infinite)~~](math/set_theory.py)
 + Automata theory/finite state machines
 + Markov chain
+ Engineering
  + Testing
    + Test matrices
    + Testing libraries
  + Problem solving
    + Decomposition

## Algorithms

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

## Computer Organization

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

## Operating Systems

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

## Advanced

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
    + Decision tree
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
 + Nimrod
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

## Other resources / references

### Requirements list for BCS
http://en.wikipedia.org/wiki/Bachelor_of_Computer_Science

### Other resources
+ http://en.wikipedia.org/wiki/Analysis#Computer_science
+ http://en.wikipedia.org/wiki/Programming_paradigm
+ http://en.wikipedia.org/wiki/NoSQL
+ http://en.wikipedia.org/wiki/Evaluation_strategy
+ http://en.wikipedia.org/wiki/Machine_learning
+ http://www.fullstackpython.com/table-of-contents.html
+ http://interactivepython.org/
+ http://refactoring.com/catalog/

### Optional reading:
+ *Introduction to Algorithm Design* by Jon Kleinberg and Eva Tardos, or Introduction to Algorithms CLRS (MIT).

### Notes, Q/A, research
+ http://stackoverflow.com/questions/2487576/trie-vs-suffix-tree-vs-suffix-array
