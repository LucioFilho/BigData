**Resource Management Systems**
                ***Apache Mesos and YARN***
                ***These resource management systems play a crucial role in distributed computing by efficiently managing resources across a cluster, thus enabling scalable and flexible big data processing.***
    └── **Apache Mesos**
        └── **Purpose**: 
            └── Simplifies running applications across a shared pool of servers.
        └── **Concept**: 
            └── Acts as a layer of abstraction between servers and resources, offering a way to execute applications without concern for the underlying server infrastructure.
        └── **Functioning**: 
            └── Utilizes a single master node (with possible inactive replicas) to manage resource requests across the cluster, with the rest being slave nodes responsible for executing tasks from execution environments (e.g., Spark, Hadoop).
        └── **Master Node Role**: 
            └── Manages and tracks job execution, allocating tasks to slave nodes which report their status back to the master.
        └── **Website**: [Apache Mesos](http://mesos.apache.org)
    **YARN** 
                ***Yet Another Resource Negotiator***
    └── **Objective**: 
        └── Separates the two main functions of the JobTracker into independent services or daemons for resource management and job scheduling/monitoring.
    └── **Components**:
        └── **ResourceManager (RM)**: 
            └── Global manager of resources.
        └── **ApplicationMaster (AM)**: 
            └── Specific to each application, handling task scheduling and monitoring.
        └── **Functionality**: 
            └── Allows for the implementation of multiple data processing applications to perform a wide range of analyses concurrently.
        └── **Architecture**: 
            └── The ResourceManager, along with each node's NodeManager (slave), forms the operational environment, managing resources among applications while the ApplicationMaster negotiates resources for task execution.
    └── **Website**: [YARN](http://bit.ly/2btcahe)

