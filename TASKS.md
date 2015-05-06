# Introduction

####*...An autodidacts dream*

**This should be considered a living document. It will grow in size, becoming better organized as new details and fields of study are integrated**

_Note:_ *completed tasks are [linked](#)*. Tasks are generally structured to be individual and atomic, but many build off of each other and are imported as new modules. Each file is formatted to have classes/definitions and then examples below. Each task and child task/category is designed to be as true to the hierarchy of understanding as possible; duplicate labels are thus removed for child elements, so that relationships are derived by simply mentally "traversing the tree", to build out the specific name.

# Tasks

## Data structures / types

+ Persistent
  + Partial
      + Fat node
      + Path copying
      + Fat / path combination
  + Full
  + Confluent
+ Retroactive
  + Partial
  + Full
+ [Abstract data types](data_structures/abstract/)
  + [Arrays](data_structures/abstract/array_and_linked_lists.py)
  + [Container](data_structures/abstract/container.py)
  + [Map / Associative array / Dictionary](data_structures/abstract/map.py)
  + [Multi-map](data_structures/abstract/map.py)
  + [List](data_structures/abstract/list.py)
  + [Set](data_structures/abstract/set.py)
    + [Static](data_structures/abstract/set.py)
    + [Dynamic](data_structures/abstract/set.py)
  + [Multi-set / Bag](data_structures/abstract/set.py)
  + [Queue](data_structures/abstract/queues.py)
    + [Double-ended queue](data_structures/abstract/queues.py)
    + [Priority queue](data_structures/abstract/queues.py)
      + [Using stdlib](data_structures/abstract/queues_stdlib.py)
  + [Stacks](data_structures/abstract/stack.py)
    + [Stack frames](data_structures/abstract/stack_frame.py)
  + [String](data_structures/abstract/string_adt.py)
  + [Tree](data_structures/abstract/tree.py)
  + [Stream](data_structures/abstract/stream.py)
  + [Graph](data_structures/graphs/graphs.py)
+ Linear
  + [Arrays](data_structures/abstract/array_and_linked_lists.py)
    + [Overloaded arrays](helpers/adts.py)
    + [Suffix arrays](data_structures/linear/array/suffix_arrays.py)
      + Compressed suffix array
    + [Bi-directional map](data_structures/abstract/map.py)
    + [Bit](computer_organization/data_types.py)
    + [Bit field](computer_organization/bit_field.py)
    + Bit Array
      + Bitboard
      + Bitmap
    + Circular buffer
    + Control table
    + Image
    + Dynamic
    + Gap buffer
    + Hashed array tree
    + Heightmap
    + Lookup table
    + Matrix
    + Parallel
    + Sorted
    + Sparse
    + Sparse matrix
    + Iliffe vector
    + Variable-length
  + Lists
    + Doubly linked
    + Array list
    + [Linked](data_structures/abstract/array_and_linked_lists.py)
      + [Association list](data_structures/abstract/array_and_linked_lists.py)
    + Self-organizing
    + [Skip lists](data_structures/linear/lists/skip_lists.py)
    + Unrolled linked
    + VList
    + Xor linked
    + Zipper
    + Doubly connected edge
    + Difference
    + Free
+ Hashes
  + Bloom filter
  + Count-Min sketch
  + Distributed hash table
  + Double Hashing
  + Dynamic perfect hash table
  + Hash array mapped trie (HAMT)
  + Hash list
  + [Hash table](data_structures/hashes/hashtable.py)
  + Hash tree
  + Hash trie
  + Koorde
  + Prefix hash tree
  + Rolling hash
  + MinHash
  + Quotient filter
+ Trees
  + Binary
    + AA
    + [AVL](data_structures/trees/avl_trees.py)
    + [Binary search](data_structures/trees/binary_search_trees.py)
      * Randomized binary search
      * Self-balancing binary search
    + [Binary](data_structures/trees/binary_trees.py)
    + [Cartesian](data_structures/trees/cartesian_trees.py)
    + Order statistic
    + Pagoda
    + Red-black
    + Rope
    + Scapegoat
    + [Splay](data_structures/trees/splay_trees.py)
    + T-tree
    + Tango
    + Threaded binary
    + Top
    + [Treap](data_structures/trees/cartesian_trees.py)
    + Weight-balanced
    + Binary data structure
    + Stern–Brocot (mathematical)
  + B
    + B
    + B+
    + B*
    + B sharp
    + Dancing
    + 2-3
    + 2-3-4
    + Queap
    + Fusion
    + Bx
    + AList
  + [Heaps](data_structures/trees/heaps.py)
    + Binary
    + Weak
    + Binomial
    + Fibonacci
      + AF
    + Leonardo
    + 2-3
    + Soft
    + Pairing
    + Leftist
    + Beap
    + Skew
    + Ternary
    + D-ary
    + Brodal queue
  + Fractal
  + Interval tree
  + Binary indexed tree
  + vEB tree
  + Red-black tree
  + [Trie](data_structures/trees/trie.py)
    + Radix tree
    + [Suffix tree](data_structures/trees/suffix_tree.py)
      + [Generalized](data_structures/trees/suffix_tree.py)
      + Ukkonen's
      + McCreight's
    + FM-index
    + B-trie
    + Judy array
    + X-fast
    + Y-fast
    + Concurrent trie (Ctrie)
  + Space-partitioning
    + Segment
    + Interval
    + Range
    + Bin
    + Kd-tree
    + Implicit kd-tree
    + Min/max kd-tree
    + Adaptive k-d
    + Quad
    + Oc
    + Linear oc
    + Z-order
    + UB
    + R
    + R+
    + R*
    + Hilbert R
    + X
    + Metric
    + Cover
    + M
    + VP
    + BK
    + Bounding interval hierarchy
    + BSP
      + K-dimensional tree
    + Rapidly exploring random
  + Multiway
    + Ternary
    + K-ary
    + And–or
    + (a,b)
    + Link/cut
    + SPQR
    + Spaghetti stack
    + Disjoint-set / union-find / merge-find ADT
    + Fusion
    + Enfilade
    + Exponential
    + Fenwick
    + Van Emde Boas
    + Rose
  + Application specific
    + Abstract syntax
    + Parse
    + Decision
    + Alternating decision
    + Minimax
    + Expectiminimax
    + Finger
    + Bounding volume hierarchy
    + Expression
    + Log-structured merge
    + AHO tree (for AHO algorithm)
+ [Graph](data_structures/graphs/graphs.py)
  + [Adjacency list](data_structures/graphs/adjacency_list.py)
  + [Adjacency matrix](data_structures/graphs/adjacency_matrix.py)
  + [Incidence matrix](data_structures/graphs/incidence_matrix.py)
  + Graph-structured stack
  + Scene
  + Binary decision diagram
  + Zero-suppressed decision diagram
  + And-inverter
  + [Directed](data_structures/graphs/graphs.py)
    + DAWG/DAFSA
      + Sparse
      + Compacted
    + [Acyclic](data_structures/graphs/graphs.py)
      + Propositional
  + Multigraph
  + Hypergraph
+ Other
  + Lightmap
  + Winged edge
  + Quad-edge
  + Routing table
  + Symbol table

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
      + Model transformation
    + Feature driven (FDD)
    + Domain driven (DDD)
+ Design Patterns
  + /TBD/
+ Testing
  + Black box
    + Decision table testing
    + All-pairs testing
    + State transition analysis
    + Equivalence partitioning
    + Boundary value analysis
    + Cause-effect graph
    + Error guessing
  + White box
    + API testing
    + Code coverage
    + Fault injection
    + Mutation testing
    + Static analysis
      + Shape analysis
      + Effect systems
      + Control-flow graph (CFG)
      + Model checking
        + TuLiP
      + Static program analysis
        + Pylint
      + Data-flow analysis
      + Hoare logic
      + Type checking
      + Type inference
      + Symbolic simulation
      + Symbolic execution
      + Abstract interpretation
        + Sound
        + Unsound
  + Gray box
    + /TBD/
+ Deployment
+ Formal verification
  + Theorem provers
    + Automated
  + Verified computation
  + Process-calculus
+ Refactoring
  + Martin Fowler refactoring.com patterns
+ Problem solving
  + Decomposition

## Mathematics

+ Quantity
  + Numbers
    + [Natural](maths/numbers/basic.py)
      + [Transfinite](maths/set_theory.py)
    + [Integers](maths/numbers/basic.py)
    + [Rational](maths/numbers/basic.py)
    + [Irrational](maths/numbers/basic.py)
    + [Real](maths/numbers/basic.py)
    + Imaginary
    + Complex
    + Quaternions
    + Octonions
    + [Cardinals](maths/set_theory.py)
+ Structure
  + [Combinatorics](maths/combinatorics/basic.py)
  + [Number theory](maths/number_theory.py)
  + Group theory
  + Category theory
  + Graph theory
    + Spectral graph theory
    + Euler graph
    + Hamiltonian graph
  + Order theory
  + Representation theory
  + Algebra
+ Space
  + Geometry
  + Trigonometry
  + Differential geometry
  + Topology
  + Fractal geometry
  + Measure theory
+ Change
  + Calculus
  + Vector calculus
  + Differential equations
  + Dynamical systems
  + Chaos theory
  + Complex analysis
+ Applied
  + Computational
    + Geometry
    + Mathematical physics
    + Fluid dynamics
    + Numerical analysis
      + Asymptotic notation
        + [Big O](maths/big_o.py)
          + [O(1)](maths/big_o.py)
          + [O(logN)](maths/big_o.py)
          + [O(n)](maths/big_o.py)
          + [O(n logN)](maths/big_o.py)
          + [O(n^2)](maths/big_o.py)
          + [O(2^n)](maths/big_o.py)
          + [O(n!)](maths/big_o.py)
    + Optimization
      + Memoization
      + Strength reduction
      + Caching
      + Linear programming
        + Augmented form
        + Duality
    + Probability theory
    + Statistics
      + [Probability](maths/probability.py)
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
    + Modeling
      + Finance
      + Biology
      + Chemistry
      + Economics
+ Discrete
  + Game theory
  + Control theory
  + Decision theory
  + Utility theory
  + Social choice theory
  + Logic
    + [Set theory](maths/set_theory.py)
      + Axiomatic
      + Combinatorial
      + Descriptive
      + Fuzzy
      + Inner model
      + Large cardinal
      + Determinacy
      + Forcing
      + Cardinal invariants
      + Set-theoretic topology
    + Model theory
      + Classical
      + Applied to groups and fields
      + Geometric
      + Finite
      + Infinite
    + Recursion theory / Computability theory
      + Lambda calculus
    + Proof theory
      + Hilbert system
    + First-order
    + Predicate
    + Computational
    + Modal
    + Algebraic

## Algorithms

+ String search
  + Knuth-Morris-Pratt
  + Boyer-Moore-Horspool
  + Apostolico-Giancarlo
  + Aho-Corasick multi-pattern
  + Rabin-Karp multi-pattern
+ Coding theory
  + String edit
    + [Hamming distance](algorithms/coding_theory/hamming_distance.py)
    + [Levenshtein distance](algorithms/coding_theory/levenshtein_distance.py)
      + Damerau–Levenshtein distance
    + Hamming weight
    + Jaro–Winkler distance
    + Lee distance
    + Hirschberg's
    + MostFreqKDistance
    + Needleman–Wunsch
    + Wagner–Fischer
    + Smith–Waterman
    + MinHash
    + Bitap
    + Longest common subsequence
      + Hunt–McIlroy
    + Longest common substring
    + Longest palindromic substring
+ Mutual exclusion management
  + Szymanski's
  + Taubenfeld's black-white bakery
  + Lamport's bakery
  + Peterson's
  + Dekker's
+ Distributed Networking
  + Koorde
  + Chord
+ Parsing/Grammars
  + Cocke–Younger–Kasami
  + Inside–outside
  + Forward–backward
  + Viterbi
  + Earley
  + Conditional Inside
+ Number series generation/discovery
  + Spigot
  + Sieve of Eratosthenese
+ Multiplication
  + Gauss's complex
  + Karatsuba
  + Schonhage-Strassen
  + Toom-Cook
  + Fourier transform
+ Sorting
  + [Insertion sort](algorithms/sorting/insertion_sort.py)
  + [Merge sort](algorithms/sorting/merge_sort.py)
  + [Quick sort](algorithms/sorting/quick_sort.py)
  + Splay sort
  + Heap sort
  + Radix sort
    + MSD
    + Adaptive
    + MBM
    + Forward
  + [Bubble Sort](algorithms/sorting/bubble_sort.py)
  + [Bogo Sort (anti-pattern)](algorithms/sorting/bogo_sort.py)
  + Burst sort
  + [Selection Sort](algorithms/sorting/selection_sort.py)
  + [Shell Sort](algorithms/sorting/shell_sort.py)
+ Approximation
+ Greedy
+ Dynamic programming
+ Divide & conquer
+ Time series analysis
  + Dynamic time warping
+ Geometry
  + Manhattan distance
  + Euclidean distance
+ Graph traversal
  + Shortest Path Problems
  + Dijkstra's Algorithm
  + Knight's Tour Problem
  + The Word Ladder Problem
  + DFS / BFS
  + Prim's Spanning Tree Algorithm
  + Building the Word Ladder Graph
  + Topological Sorting
  + Strongly Connected Components

## Computer Organization

+ Transistors
+ Logic gates
+ [Data-types & representation](computer_organization/data_types.py)
  + [Bit](computer_organization/data_types.py)
  + [Nibble](computer_organization/data_types.py)
  + [Byte](computer_organization/data_types.py)
  + [Octet](computer_organization/data_types.py)
  + [*byte](computer_organization/data_types.py)
  + [Two's complement](computer_organization/one_twos_complement.py)
  + [Ones' complement](computer_organization/one_twos_complement.py)
+ [Numerical encoding](computer_organization/numerical_encoding_basic.py)
  + [N-ary](computer_organization/positional.py)
    + [Binary](computer_organization/numerical_encoding_basic.py)
       + [Binary coded decimal (BCD)](computer_organization/bcd.py)
        + [8421](computer_organization/bcd.py)
        + 4221
        + 7421
        + [excess-3](computer_organization/bcd.py)
        + Telephony (TCBD)
    + Bi-Quinary
    + [Ternary](computer_organization/positional.py)
      + Balanced ternary
    + [Quaternary](computer_organization/positional.py)
    + [Quinary](computer_organization/positional.py)
    + [Senary](computer_organization/positional.py)
    + [Septenary](computer_organization/positional.py)
    + [Octal](computer_organization/numerical_encoding_basic.py)
    + [Nonary](computer_organization/positional.py)
    + [Decimal](computer_organization/numerical_encoding_basic.py)
    + [Undecimal](computer_organization/positional.py)
    + [Duodecimal](computer_organization/positional.py)
    + [Tridecimal](computer_organization/positional.py)
    + [Tetradecimal](computer_organization/positional.py)
    + [Pentadecimal](computer_organization/positional.py)
    + [[Hexadecimal](computer_organization/positional.py)](computer_organization/numerical_encoding_basic.py)
    + [Octodecimal](computer_organization/positional.py)
    + [Vigesimal](computer_organization/positional.py)
    + [Tetravigesimal](computer_organization/positional.py)
    + [Pentavigesimal](computer_organization/positional.py)
    + [Hexavigesimal](computer_organization/positional.py)
    + [Septemvigesimal](computer_organization/positional.py)
    + [Trigesimal](computer_organization/positional.py)
    + [Duotrigesimal](computer_organization/positional.py)
    + [Hexatrigesimal](computer_organization/positional.py)
    + [Sexagesimal](computer_organization/positional.py)
    + [Duosexagesimal](computer_organization/positional.py)
    + [Tetrasexagesimal](computer_organization/positional.py)
    + [Pentaoctagesimal](computer_organization/positional.py)
    + [Centovigesimal](computer_organization/positional.py)
    + [Duocentoquadragesimal](computer_organization/positional.py)
    + [Trecentosexagesimal](computer_organization/positional.py)
    + [Custom](computer_organization/positional.py)
  + Complex
    + Quater-Imaginary base
    + Twindragon
  + Non-integer bases
    + Golden ratio
    + Euler
    + Pi-ary
    + Sqrt 2
    + 12th root of two
  + Redundant binary representation (RBR)
  + Quote notation
  + Fibonacci coding
  + Skew binary
  + Ostrowski numeration
  + Negative
    + Negabinary
    + Negadecimal
    + Negaternary
    + Negafibonacci
  + Mixed radix
    + Factoradic
  + Bijective
    + base-10
    + base-26
  + 1-adic bijective (tally)
  + Johnson code
  + Gray code
    + n-ary
    + Balanced
    + Binary-reflected (BRGC)
    + Monotonic
    + Beckett–Gray
    + Snake-in-the-box
    + Single-track
+ Math
  + [Endianness (byte ordering)](computer_organization/endianness.py)
  + [Binary](computer_organization/data_types.py)
    + [Addition](computer_organization/data_types.py)
    + [Subtraction](computer_organization/data_types.py)
    + [Multiplication](computer_organization/data_types.py)
    + [Division](computer_organization/data_types.py)
    + Square root
    + [Bitwise operations](computer_organization/bitwise_operations.py)
      + [XOR](computer_organization/bitwise_operations.py)
      + [OR](computer_organization/bitwise_operations.py)
      + [AND](computer_organization/bitwise_operations.py)
      + [NOT](computer_organization/bitwise_operations.py)
      + [Shifts](computer_organization/bitwise_operations.py)
        + [Arithmetical](computer_organization/bitwise_operations.py)
        + [Logical](computer_organization/bitwise_operations.py)
        + [Rotate no carry](computer_organization/bitwise_operations.py)
        + [Rotate through carry](computer_organization/bitwise_operations.py)
  + [Bit field](computer_organization/bit_field.py)
  + [Flag field](computer_organization/bit_field.py)
  + [Bit Masking](computer_organization/bitwise_operations.py)
+ Memory
  + Memory hierarchy
  + Virtual memory
  + Memory mapped I/O
+ Synchronization primitives

## Operating Systems

+ Concurrency
  + Multi-tasking
    + Dining philosophers
    + Race condition
    + Futures / Promises
    + Deadlock
    + Lock
    + Barrier
    + Single reader multiple writer
    + Turnstile
    + Mutual exclusion (mutex)
    + Starvation
    + Priority inversion
    + Semaphores
  + Primitives
    + Process
    + Threads
      + Kernel
      + Green
      + POSIX
      + Models
        + Kernel level (1:1)
        + User level (N:1)
        + Hybrid (M:N)
    + Co-routines [language]
    + Fibers [system]
  + Schedulers
  + Producer / consumer
+ Memory management
+ File systems
+ Security
  + Protection ring
  + Supervisor
  + Hypervisor
  + Language based
+ System on a chip (SoC)

## Networking

+ Ethernet
+ Protocols
  + RPC
    + JSONRPC
    + XMLRPC
  + Bluetooth
  + Fibre channel
  + TCP / IP
  + RTPS
  + SSH
  + UDP
    + Twisted UDP
  + FTP/sFTP
    + Twisted FTP
  + SMTP
  + Telnet
  + HTTP/HTTPS
    + HTTP Servers
      + G-Unicorn
      + uWSGI
  + SSL
  + TLS
  + POP
  + E6
  + NTP
  + PPP
  + NNTP
  + IMAP
  + Bitcoin
  + Recursive network architecture (RNA)
  + Custom (make one!)
+ Load balancing
  + NGINX
  + Apache
  + HAProxy
+ Administration
  + Software defined

## Data Storage / Transmission

+ Storage
  + Databases
    + Relational
      + MySql
      + PostgreSql
    + Key/value
      + Redis (doc + k/v)
    + Document
      + ElasticSearch
      + Solr
      + MongoDB
      + CouchDB
    + Cache
      + MemCached
    + Graph
      + Neo4j
    + WideColumn
      + HBase
      + BigTable
    + Data structures
      + Inverted Index
+ Serialization
  + Apache Avro
  + CSV
  + JSON
  + MessagePack
  + Protocol Buffers
  + S-expressions
  + YAML
  + Custom (make one!)
+ Modeling
  + SPICE
  + CMMI
  + Data model
  + ER model
  + Function model
  + Information model
  + Meta modeling
  + Object model
  + Systems model
  + View model
+ Transformation
  + Migration
  + Conversion
  + Metadata
    + Descriptive
    + Structural

## Systems Engineering

+ Architecture
  + Model driven (MDA)
  + MVC / N-Tier
  + SOA
    + Micro-services
  + RESTful API
    + Basic
    + HATEOAS
  + API design
    + Fluent interface
+ Parallel Computing
+ Distributed Computing
  + Peer-to-Peer (P2P)
    + Structured
    + Unstructured
  + CAP Theorem
  + "Big Data" processing
    + Hadoop file system
    + Hadoop MapReduce
    + PIG
    + ZooKeeper
      + Kazoo
    + Lucene
+ Message queuing
  + RabbitMQ
  + ZeroMQ
+ Performance
  + Caching
    + Varnish

## Artifical Intelligence

+ Machine learning
  + Supervised learning
    + Decision tree
    + Perceptrons
    + Support vector machines
    + K-means clustering
    + Bayesian probability
    + Neural networks
      + Recurrent (RNNs)
        + Boltzmann machine
        + Hopfield
        + Elman
        + Jordan
        + Echo state
        + Long short term memory
        + Bi-directional
        + Continuous-time
        + Hierarchical
        + Recurrent multilayer Perceptron
        + Second order
        + Pollack's sequential cascaded
        + Neural turing machines
        + Bidirectional associative memory (BAM)

## Robotics & Electronics

+ Arduino
+ Raspberry Pi
+ HDLs
  + Analog
  + Digital circuit
    + Verilog

## Graphics

+ /TBD/

## Theory of Computation

+ Automata theory
  + Continuous spatial automata
  + Cellular automata
    + Reversible
    + Totalistic
    + Von Neumann universal constructor
    + Nobili
  + Abstract machine
    + Pushdown automata
      + Generalized
    + [Turing machine](automata_theory/turing_machine.py)
      + [Universal](automata_theory/universal_turing_machine.py)
      + [Decider / Total](automata_theory/turing_machine.py)
      + Alternating
      + Quantum
      + Non-deterministic
      + Read-only
      + Read-only right moving s
      + Probabilistic
      + Multi-tape
      + Multi-track
    + Stack machine
    + Register machine / Wang-b machine
      + [Pointer](automata_theory/pointer_machine.py)
        + [Schonhage Storage Modification](automata_theory/pointer_machine.py)
        + [Kolmogorov-Uspenskii](automata_theory/pointer_machine.py)
        + Knuth's Linking Automaton
        + Atomistic Pure-LISP (APLM)
        + Atomistic Full-LISP (AFLM)
        + General atomistic
        + Jone's I Language 1
        + Jone's I Language 2
      + [Counter](automata_theory/counter_machine.py)
        + [SheperdsonSturgis](automata_theory/counter_machine.py)
        + [Minsky](automata_theory/counter_machine.py)
        + Program
        + [Abacus](automata_theory/counter_machine.py)
        + Lambek
        + Successor
        + SuccessorRAM
        + ElgotRobinsonRASP
      + Random-access stored-program
      + Random access
      + Cell probe
  + Finite State Machines (FSM)
    + Transducers
    + Acceptors
    + Classifiers
    + Sequencers
    + Markov chain
    + Regular expressions
    + Richards controller
    + Moore
    + Mealy
    + Levenshtein automaton
+ Computational complexity
  + Classes
    + P
    + NP
    + #P
    + BPP
    + PSPACE
+ PCPs
+ Circuit lower bounds
+ Arithmetic complexity
+ Quantum complexity
+ Communication complexity
+ Unique Games Conjecture and its relation to optimality of approximation algorithms

## Languages

+ Interesting language features / syntactic sugar (format: Language - feature)
  + Python - generator
    + recursive
    + expression
  + Python - decorator
  + Python - context manager (with)
  + [Python - variable packing/unpacking](languages/features/python/packing_unpacking.py)
  + Python - index slicing
  + Python - comprehensions
  + Rust - de-structuring
  + Rust - pattern matching
  + Haskell - pattern matching
  + Haskell - monads
  + Haskell - guards
  + Haskell - comprehensions
+ Evaluation strategies
  + Eager
  + Lazy
  + Partial
  + Remote
  + Short-circuit
+ Formal language theory
  + Modeling language
    + Algebraic
    + Behavioral
    + Discipline-Specific
    + Domain-specific
    + Framework-specific
    + Object-oriented
    + reality
    + Others
    + Dyck language
  + Formal grammars
    + Link
    + Tree-adjoining
    + Recursive
    + Regular
    + Analytic
    + Context-sensitive
    + [Context-free](languages/formal_language_theory/grammars/context_free.py)
      + Stochastic
      + [Attribute](languages/formal_language_theory/grammars/attribute_context_free.py)
      + Adaptive
        + Recursive (RAGs)
        + Dynamic Template Translators
        + Christiansen
        + Wegbreit
        + Dynamic
        + Meta-S calculus
        + Imperative
        + Declarative
        + Hybrid / Time-space
      + [Ambiguous](languages/formal_language_theory/grammars/context_free.py)
      + [Backus-Naur Form (BFN)](languages/formal_language_theory/grammars/backus_naur.py)
        + Extended
+ Paradigms
  + Functional
    + Languages
      + Haskell
      + OCaml
      + Lisp
      + Clojure
    + Features
      + Parametric polymorphism
  + Logic
    + Abductive
    + Answer set
    + Constraint
    + Functional
    + Inductive
    + Prolog
  + Object-oriented
    + Features
      + [Class hierarchy](languages/paradigms/oop_classes.py)
      + [Static, class, & abstract methods](languages/paradigms/oop_classes.py)
        + Abstract Base Classes
      + Overloading
      + Polymorphism
        + Single dispatch
        + Dynamic dispatch
        + Multiple dispatch
        + Static binding
  + Array programming
    + J
  + Meta-programming
    + Languages
      + Racket
  + Template meta-programming
  + Automatic
    + Program synthesis
  + Dataflow
    + Flow based
    + Cell-oriented
    + Ractive
    + Hartmann pipeline
  + Stream processing
  + Concurrent
    + Languages
      + GO
      + Rust
      + Nimrod
      + Mozart
  + Domain Specific (DSL)
    + Metalinguistic abstraction
    + Embeddable
    + Macros
      + Hygienic
      + Anaphoric
      + Text Substitution
        + Sublime plugin
    + Templating language (make one!)

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

## Program Execution

+ Emulator
  + Binary translation
  + Hardware
  + In-circuit
  + Server
  + Terminal
  + Network
  + Instruction set
  + Video game console
  + Semulation
  + Logic simulation
+ Processing units
  + CPU
    + Architectures
      + Very long instruction word (VLIW)
      + Complex instruction set computing (CISC)
      + Fetch
      + Decode
      + Execute
  + Control unit
  + ALU
  + AGU
  + APU
  + Vector processor
  + Field Programmable Gate Array (FPGA)
  + Microprocessor
    + Reduced instruction set computing (RISC)
+ Runtime system
  + Specific runtimes
    + Android Runtime (ART)
    + crt0
    + Common Language Runtime (CLR)
    + Dalvik
    + Java virtual machine (JVM)
+ Runtime library
+ Executable
+ Compilation
  + Assembler
  + Linker
  + Compile farm
    + GCC Compile farm
+ Compiler
  + Software
    + Semantics encoding
    + Meta-compilation
    + Source-to-source (transpiler)
    + Binary recompiler
    + One pass
    + Multi pass
    + Front end
    + Back end
    + Implementations
      + PL/0
      + Psyco
      + Cython
      + PyPy
      + GCC
      + Clang
    + Custom (make one!)
    + Symbol table
    + Abstract Syntax Tree (AST)
    + Abstract semantic graph
    + Components
      + Parser
        + Top down
            + LL(1)
            + LL(k)
              + Simple
              + Look-Ahead / LALR
        + Bottom up
          + Backtracking
          + Shift-reduce
        + Recursive descent
      + Lexer
        + Tokenizer
        + Lexical grammar generation
        + Scanner
        + Evaluator
        + Lexer generator
+ Interpreter
  + Bytecode interpreters
  + Abstract Syntax Tree interpreters
  + Just-in-time compilation
  + Self-interpreter
+ Virtual machine
  + Process
  + System
  + Dynamic recompilation
  + Hardware-assisted virtualization
  + p-code machine
+ Source code
+ Object code
+ Bytecode
+ Machine code
  + Opcode
  + Assembly language
    + Assembler concept
    + Languages
      + ARM
      + MIPS
      + x86
      + 6502

## Other resources / references

### Requirements list for BCS
wikipedia.org/wiki/Bachelor_of_Computer_Science

### Other resources

*Wikipedia*
+ wikipedia.org/wiki/List_of_important_publications_in_computer_science
+ wikipedia.org/wiki/Analysis#Computer_science
+ wikipedia.org/wiki/Central_processing_unit
+ wikipedia.org/wiki/System_on_a_chip
+ wikipedia.org/wiki/Programming_paradigm
+ wikipedia.org/wiki/List_of_algorithms
+ wikipedia.org/wiki/NoSQL
+ wikipedia.org/wiki/Evaluation_strategy
+ wikipedia.org/wiki/Machine_learning
+ wikipedia.org/wiki/Recurrent_neural_network
+ wikipedia.org/wiki/Register_machine
+ wikipedia.org/wiki/Cellular_automaton
+ wikipedia.org/wiki/Turing_machine
+ wikipedia.org/wiki/Static_program_analysis
+ wikipedia.org/wiki/Lists_of_network_protocols
+ wikipedia.org/wiki/Communications_protocol
+ wikipedia.org/wiki/Software_development_process
+ wikipedia.org/wiki/Software_testing#Testing_methods
+ wikipedia.org/wiki/Cipher
+ wikipedia.org/wiki/Type_theory
+ wikipedia.org/wiki/Remote_procedure_call
+ wikipedia.org/wiki/Inter-process_communication
+ wikipedia.org/wiki/Performance_engineering
+ wikipedia.org/wiki/Persistent_data_structure
+ wikipedia.org/wiki/Software_design_pattern
+ wikipedia.org/wiki/Category:Formal_languages
+ wikipedia.org/wiki/Retroactive_data_structures
+ wikipedia.org/wiki/Linear_programming
+ wikipedia.org/wiki/Modeling_language
+ wikipedia.org/wiki/Formal_grammar#The_Chomsky_hierarchy
+ wikipedia.org/wiki/LL_parser
+ wikipedia.org/wiki/List_of_programming_languages_by_type#Machine_languages
+ wikipedia.org/wiki/Comparison_of_data_serialization_formats
+ wikipedia.org/wiki/Thread_(computing)#Processes.2C_kernel_threads.2C_user_threads.2C_and_fibers
+ wikipedia.org/wiki/List_of_compilers
+ wikipedia.org/wiki/Logic#Types_of_logic
+ wikipedia.org/wiki/Discrete_mathematics
+ wikipedia.org/wiki/Hardware_description_language
+ wikipedia.org/wiki/Symbol_table
+ wikipedia.org/wiki/Mathematics#Fields_of_mathematics
+ wikipedia.org/wiki/Lexical_analysis
+ wikipedia.org/wiki/Mathematical_logic
  + wikipedia.org/wiki/Set_theory#Areas_of_study
  + wikipedia.org/wiki/Proof_theory
  + wikipedia.org/wiki/Computability_theory#Areas_of_research
  + wikipedia.org/wiki/Model_theory
+ wikipedia.org/wiki/List_of_data_structures
+ wikipedia.org/wiki/List_of_numeral_systems
  + wikipedia.org/wiki/Factorial_number_system
  + wikipedia.org/wiki/Gray_code
  + wikipedia.org/wiki/Bitwise_operation
+ wikipedia.org/wiki/Coding_theory

*Misc*
+ fullstackpython.com/table-of-contents.html
+ interactivepython.org/
+ refactoring.com/catalog/
+ anandology.com/python-practice-book

### Optional reading:
+ *Introduction to Algorithm Design* - Jon Kleinberg and Eva Tardos
+ *Introduction to Algorithms CLRS (MIT)*
+ *Purely functional data structures* - Chris Okasaki
+ *The Language of Machines: An Introduction to Computability and Formal Languages* - Robert W. Floyd, Richard Beigel

### Notes, Q/A, research
+ stackoverflow.com/questions/2487576/trie-vs-suffix-tree-vs-suffix-array
+ research.microsoft.com/en-us/um/people/gurevich/Opera/78.pdf
+ symbolicanalysis.wordpress.com/category/other-methodologies/turing-machine-and-related-automata/
+ github.com/boyers/theorem_prover
+ symbolicanalysis.wordpress.com/2009/12/15/propositional-directed-acyclic-graph-pdag-vs-aho/
+ quora.com/What-is-the-difference-between-Top-Down-parsing-and-Bottom-up-parsing-in-programming-languages
