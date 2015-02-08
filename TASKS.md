# Introduction

_Note:_ *completed tasks will be ~~crossed out with a [link](#)~~*. Tasks are generally structured to be individual and atomic, but many build off of each other and are imported as new modules. Each file is formatted to have classes/definitions and then examples below in each file.

## Goals

The primary goal of this project is to synthesize an extremely large set of concepts and ideas into crucial components, allowing one to learn a typically unfathomable breadth of topics in the field, doing so in a shorter amount of time. The trade off of **depth** is acceptable as it stresses basic competencies across all aspects, **which can later be translated into more detailed understanding**.

# Tasks

## Data structures
+ [~~Arrays~~](data_structures/array_and_linked_lists.py)
  + Suffix arrays
  + Judy arrays
+ [~~Linked lists~~](data_structures/array_and_linked_lists.py)
+ Doubly-connected edge list
+ Disjoint-set/union-find/merge-find ADT
+ Winged edge
+ Quad edge
+ [~~Heaps~~](data_structures/heaps.py)
+ [~~Hash table~~](data_structures/hashtable.py)
+ Bloom filters
+ [~~Stacks~~](data_structures/stack.py)
  + [~~Stack frames~~](data_structures/stack_frame.py)
+ [~~Queue~~](data_structures/queues.py)
  + [~~Double-ended queue~~](data_structures/queues.py)
  + [~~Priority queue~~](data_structures/queues.py)
    + [~~Using stdlib~~](data_structures/queues_stdlib.py)
+ Trees
  + BSP Tree
    + K-dimensional tree
  + Fractal tree index
  + Interval tree
  + [~~Binary search tree~~](data_structures/binary_search_trees.py)
  + Binary indexed tree
  + [~~Splay tree~~](data_structures/splay_trees.py)
  + vEB tree
  + Red-black tree
  + [~~AVL tree~~](data_structures/avl_trees.py)
+ [~~Graph~~](data_structures/graphs.py)
  + DAWG/DAFSA
+ Concurrent trie (Ctrie)
+ [~~Skip lists~~](data_structures/skip_lists.py)
+ [~~Trie~~](data_structures/trie.py)
  + Suffix tree
  + Hash array mapped tries (HAMT)

## Engineering / Software Development

+ Requirements analysis
+ Debugging
+ Development
  + Methodologies
    + Test driven (TDD)
      + Creating test matrices
      + Testing libraries
        + Nose
    + Behavior driven (BDD)
    + Model driven (MDD)
    + Feature driven (FDD)
    + Domain driven (DDD)
+ Testing
  + Black box
    + Decision table testing
    + All-pairs testing
    + State transition analysis
    + Equivalence partitioning
    + Boundary value analysis
    + Cause–effect graph
    + Error guessing
  + White box
    + API testing
    + Code coverage
    + Fault injection
    + Mutation testing
    + Static testing
  + Gray box
    + TBD
+ Deployment
+ Formal verification
  + Theorem provers
  + Verified computation
  + Hoare logic
  + Process-calculus
+ Refactoring
  + Martin Fowler refactoring.com patterns
+ Problem solving
  + Decomposition

## Mathematics

+ Performance analysis
  + Asymptotic notation
    + Big O
      + [~~O(1)~~](data_structures/big_o.py)
      + [~~O(logN)~~](data_structures/big_o.py)
      + [~~O(n)~~](data_structures/big_o.py)
      + [~~O(n logN)~~](data_structures/big_o.py)
      + [~~O(n^2)~~](data_structures/big_o.py)
      + [~~O(2^n)~~](data_structures/big_o.py)
      + [~~O(n!)~~](data_structures/big_o.py)
+ Discrete math:
  + [~~Basic probability~~](math/probability.py)
  + [~~Basic number theory~~](math/number_theory.py)
  + [~~Set theory (notions of countably infinite vs. non-countably infinite)~~](math/set_theory.py)

## Algorithms

+ String search algorithms
  + Knuth-Morris-Pratt
  + Boyer-Moore-Horspool
  + Apostolico-Giancarlo
  + Aho-Corasick multi-pattern
  + Rabin-Karp multi-pattern
+ Sorting algorithms
  + [~~Insertion sort~~](algorithms/sorting/insertion_sort.py)
  + [~~Merge sort~~](algorithms/sorting/merge_sort.py)
  + [~~Quick sort~~](algorithms/sorting/quick_sort.py)
  + Splay sort
  + Heap sort
  + Radix sort
    + MSD
    + Adaptive
    + MBM
    + Forward
  + [~~Bubble Sort~~](algorithms/sorting/bubble_sort.py)
  + [~~Bogo Sort (anti-pattern)~~](algorithms/sorting/bogo_sort.py)
  + Burst sort
  + [~~Selection Sort~~](algorithms/sorting/selection_sort.py)
  + [~~Shell Sort~~](algorithms/sorting/shell_sort.py)
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

+ Transistors
+ Logic gates
+ Data (types)
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
+ Memory
  + Memory hierarchy
  + Virtual memory
  + Memory mapped I/O
+ Synchronization primitives

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
+ File systems
+ Security

## Networking

+ Ethernet
+ Protocols
  + Bluetooth
  + Fibre channel
  + TCP/IP
  + RTPS
  + SSH
  + UDP
  + FTP/sFTP
  + SMTP
  + Telnet
  + HTTP/HTTPS
  + SSL
  + TLS
  + POP
  + E6
  + NTP
  + PPP
  + NNTP
  + IMAP
  + Bitcoin
  + Custom (make one!)

## Advanced - to be categorized!

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
        + Boltzmann machine
        + Hopfield network
        + Elman network
        + Jordan network
        + Echo state network
        + Long short term memory network
        + Bi-directional RNN
        + Continuous-time RNN
        + Hierarchical RNN
        + Recurrent multilayer perceptron
        + Second Order Recurrent Neural Network
        + Pollack’s sequential cascaded networks
        + Neural Turing Machines
        + Bidirectional Associative Memory (BAM)
+ Robotics

## Theory of Computation

+ Automata theory
  + Continuous spatial automata
  + Cellular automata
    + Reversible
    + Totalistic
    + Von Neumann cellular automaton
    + Nobili cellular automata
  + Abstract machine
    + [~~Turing machine~~](automata_theory/turing_machine.py)
    + Register machine
      + [~~Counter machine~~](automata_theory/counter_machine.py)
      + Pointer machine
      + Random-access stored-program machine
      + Random access machine
  + Finite State Machines (FSM)
    + Markov chain
    + Regular expressions
+ Context-free languages
+ Complexity classes (P, NP, #P, BPP, PSPACE)
+ PCPs
+ Circuit lower bounds
+ Arithmetic complexity
+ Quantum complexity
+ Communication complexity
+ Unique Games Conjecture and its relation to optimality of approximation algorithms

## Programming Paradigms / Features

+ Interesting language features / syntactic sugar (format: Language - feature)
  + Python - yield
    + recursive yield
  + Python - decorator
  + Python - context manager (with)
  + Python - variable packing/unpacking
  + Python - index slicing
  + Python - comprehensions
  + Rust - de-structuring
  + Rust - pattern matching
  + Haskell - pattern matching
  + Haskell - monads
  + Haskell - guards
  + Haskell - comprehensions
+ Programming Paradigms:
  + Functional
    + Languages:
      + Haskell
      + OCaml
      + Lisp
      + Clojure
    + Features
      + Parametric polymorphism
  + Logic
    + Prolog
  + Object-oriented
    + Features
      + [~~Class hierarchy~~](data_structures/oop_classes.py)
      + [~~Static, class, and abstract methods~~](data_structures/oop_classes.py)
      + Overloading
      + Polymorphism
        + Single dispatch
        + Dynamic dispatch
        + Multiple dispatch
        + Static binding
  + Array programming
    + J
  + Metaprogramming
  + Template metaprogramming
  + Automatic
  + Reactive
  + Dataflow
  + Concurrent
    + Languages
      + GO
      + Rust
      + Nimrod
      + Mozart
  + Assembly
    + ARM
    + MIPS
    + x86
    + 6502

## Type theory

+ Type systems
  + Type safety
  + Type checking
      + Dynamic
      + Static
  + Inferred
  + Manifest
  + Nominal
  + Structural
  + Dependent
  + Duck
  + Gradual
  + Latent
  + Sub-structural
  + Uniqueness
  + Strong
  + weak
+ Lambda calculus

## Uncategorized [WIP]

+ Language based security
+ Software defined networking
+ Compilers
  + Building one
+ Computer Graphics
+ Computational geometry
+ Scientific computation
+ Cryptography
  + Diffie-Hellman
  + RSA
  + Zero-knowledge proofs
  + Ciphers
    + Historical
      + Substitution
        + ROT13
      + Transposition
        + Rail fence
    + Modern
      + Key type
        + Symmetric
        + Asymmetric
      + Input type
        + Block
        + Stream

## Other resources / references

### Requirements list for BCS
http://en.wikipedia.org/wiki/Bachelor_of_Computer_Science

### Other resources

*Wikipedia*
+ http://en.wikipedia.org/wiki/Analysis#Computer_science
+ http://en.wikipedia.org/wiki/Programming_paradigm
+ http://en.wikipedia.org/wiki/NoSQL
+ http://en.wikipedia.org/wiki/Evaluation_strategy
+ http://en.wikipedia.org/wiki/Machine_learning
+ http://en.wikipedia.org/wiki/Recurrent_neural_network
+ http://en.wikipedia.org/wiki/Register_machine
+ http://en.wikipedia.org/wiki/Cellular_automaton
+ http://en.wikipedia.org/wiki/Lists_of_network_protocols
+ http://en.wikipedia.org/wiki/Communications_protocol
+ http://en.wikipedia.org/wiki/Software_development_process
+ http://en.wikipedia.org/wiki/Software_testing#Testing_methods
+ http://en.wikipedia.org/wiki/Cipher
+ http://en.wikipedia.org/wiki/Type_theory

*Misc*
+ http://www.fullstackpython.com/table-of-contents.html
+ http://interactivepython.org/
+ http://refactoring.com/catalog/

### Optional reading:
+ *Introduction to Algorithm Design* by Jon Kleinberg and Eva Tardos, or Introduction to Algorithms CLRS (MIT).

### Notes, Q/A, research
+ http://stackoverflow.com/questions/2487576/trie-vs-suffix-tree-vs-suffix-array
