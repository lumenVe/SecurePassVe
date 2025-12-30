from __future__ import annotations
from typing import Protocol

class VaultRepository(Protocol):
    def vault_exists(self, user_id: str) -> bool:
        raise NotImplementedError
    
class InMemoryVaultRepository:
    def __init__(self) -> None:
        self.vault_user_ids: set[str] = set()
    
    def add_vault_for_user(self, user_id: str) -> None:
        self.vault_user_ids.add(user_id)
        
    def vault_exists(self, user_id: str) -> bool:
        return user_id in self.vault_user_ids