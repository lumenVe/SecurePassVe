from __future__ import annotations

from securepassve_backend.vault.repository import InMemoryVaultRepository, VaultRepository

_vault_repository = InMemoryVaultRepository()

def get_vault_repository() -> VaultRepository:
    return _vault_repository