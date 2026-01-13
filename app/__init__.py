"""
Application package initialization.

This module provides dynamic router discovery and loading.
"""

import importlib
from pathlib import Path

from fastapi import APIRouter


def get_available_domain_routers() -> list[APIRouter]:
    """
    dynamically import routers from available domain modules.
    only imports domains that exist in the domains directory.
    """
    routers = []
    domains_path = Path(__file__).parent / "domain"

    if not domains_path.exists():
        return routers

    # get all directories in the domains folder
    for domain_dir in domains_path.iterdir():
        if not domain_dir.is_dir():
            continue

        # skip __pycache__ and other special directories
        if domain_dir.name.startswith("_"):
            continue

        # try to import the router from this domain
        try:
            domain_module = importlib.import_module(f"app.domains.{domain_dir.name}")
            if hasattr(domain_module, "router"):
                routers.append(domain_module.router)
        except ImportError:
            # domain exists but can't be imported - this is fine
            # it might not be available to this developer
            pass

    return routers


__all__ = ["get_available_domain_routers"]
