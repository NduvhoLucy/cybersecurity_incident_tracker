## Storage Abstraction Layer (RepositoryFactory)

To decouple the application from storage-specific implementations, we introduced a **RepositoryFactory** class.

- The Factory Pattern returns the correct storage backend based on configuration.
- Currently, the Factory produces **In-Memory Repositories** (using Python dictionaries).
- In the future, it can easily return **Database-backed Repositories** without changing service logic.

### Why Factory over Dependency Injection?

- Factory Pattern centralizes creation logic inside a single class.
- Makes it easy to extend storage options (Memory, Database, FileSystem) by just updating the Factory.
- Avoids manual dependency wiring at every usage point.
- Keeps service classes clean and storage-agnostic.

Thus, the **RepositoryFactory** helps achieve **flexibility** and **scalability** in our application architecture.

