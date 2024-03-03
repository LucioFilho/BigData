**Distributed Computing**
    └── **Distributed Computing in Big Data**
        └── **Resources Integration**: 
            └── Distributed computing integrates resources across a network, making resource location transparent to users. 
                └── Users access resources via a resource manager without concern for the resource's physical location.
            └── **Key Systems**: 
                └── Focuses on two widely used distributed computing systems in the big data ecosystem: 
                    └── **MapReduce** and **Spark**. 
                    └── Additionally, it introduces the application of distributed computing concepts to GPU└──based architectures.
    └── **MapReduce Paradigm**
        └── **Programming Model**: 
            └── Introduced by Google in 2004, supports parallel computing on large data volumes.
        └── **Cluster Utilization**: 
            └── Employs clusters of computers and uses non-specialized hardware.
        └── **Map and Reduce Functions**: 
            └── Central programming methods or functions, leading to global adoption, including open-source implementation like Hadoop by Yahoo.
        └── **Efficiency in Processing**: 
            └── Ideal for calculations that can be structured as combinations of Map() and Reduce() operations.
                └── Suitable for parallelizable tasks without iterative processing needs.
    └── **Apache Spark: n-Memory Distributed Processing**
        └── **Enhanced Performance**: 
            └── Addresses Hadoop's limitations by keeping data operations in memory, significantly boosting performance for iterative computations essential in machine learning algorithms.
        └── **Rich Operations Set**: 
            └── Extends beyond MapReduce limitations to support additional operations like joins, groups, filters, etc., through APIs available in Java, Scala, and Python.
    └── **Apache Hadoop: Distributed File System and MapReduce Framework**
        └── **Hadoop Distributed File System (HDFS)**: 
            └── A scalable, fault-tolerant storage system designed to store large datasets across clusters of commodity hardware. It achieves reliability by replicating data across multiple nodes.
        └── **High Scalability**: 
            └── Scales data storage across hundreds or thousands of servers.
        └── **Fault Tolerance**: 
            └── Automatically replicates data blocks across multiple nodes to ensure data availability even in the case of node failure.
        └── **Large Block Size**: 
            └── Utilizes larger block sizes compared to traditional file systems to optimize the storage and processing of large datasets.
        └── **Write-Once-Read-Many Model**: 
            └── Optimized for scenarios where large datasets are typically written once and read multiple times for analysis.
        └── **Data Locality Optimization**: 
            └── Processes data on or near the storage assets to reduce network congestion and increase system throughput.
    └── **MapReduce Programming Model**: 
        └── A framework for efficiently processing vast amounts of data in parallel across a Hadoop cluster. 
        └── It simplifies data processing across distributed servers by abstracting the complexity of parallelization, fault tolerance, data distribution, and load balancing.
        └── **Map Function**: 
            └── Processes input data in parallel, transforming it into a set of intermediate key/value pairs.
        └── **Reduce Function**: 
            └── Aggregates the intermediate data tuples based on the keys and reduces them to a smaller set of tuples as the final output.
        └── **Fault Tolerance**: 
            └── Automatically handles failures in the cluster by re-executing failed tasks.
        └── **Job Scheduling and Monitoring**: 
            └── Efficiently schedules jobs and monitors their progress across the cluster.
            └── Synergy between HDFS and the MapReduce framework, enabling Hadoop to process large datasets efficiently, making it a foundational technology for big data analytics and processing.
    └── **Hadoop** and **Spark Comparison**: 
        └── Both share a common purpose of big data processing but differ in their approach and efficiency. 
        └── Spark is known for faster in-memory data processing.
        └── Hadoop's MapReduce is more suited for disk-based processing.
    └── **Resilient Distributed Dataset (RDD)**: 
        └── The core abstraction in Spark that represents an immutable distributed collection of objects. 
        └── RDDs can be created through operations on data in storage or by transforming existing RDDs. 
        └── Designed to be fault-tolerant through lineage information.
    └── **GPU Computing: Simplicity and High Parallelization**
        └── **GPU Usage**: 
            └── Highlights the role of GPUs for their simplicity and high parallelization capabilities, making them suitable for certain types of big data tasks that can benefit from GPU acceleration.
        └── **Many-Core Architectures**: 
            └── Utilize a large number of cores (processors) for parallel operations on data.
        └── **SIMD (Single Instruction, Multiple Data)**: 
            └── Technique for achieving high data parallelism
                └── Essential for performance improvements in GPU-based applications.
    └── **Components for Enhanced Distributed Computing**
        └── **Fault Tolerance**: 
            └── Critical aspect ensuring that computations can continue in case of node failures.
        └── **Resource Manager Role**: 
            └── Manages job queues, allowing multiple users and groups to utilize a shared infrastructure like a computing cluster.