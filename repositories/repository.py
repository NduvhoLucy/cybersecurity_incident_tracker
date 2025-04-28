from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(Generic[T, ID]):
    def save(self, entity: T) -> None:
        """Create or update an entity."""
        raise NotImplementedError()

    def find_by_id(self, id: ID) -> Optional[T]:
        """Find an entity by its ID."""
        raise NotImplementedError()

    def find_all(self) -> List[T]:
        """Return all entities."""
        raise NotImplementedError()

    def delete(self, id: ID) -> None:
        """Delete an entity by its ID."""
        raise NotImplementedError()
