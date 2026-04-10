"""
Shared pytest configuration for headless (CI-safe) pygame testing.
Sets dummy SDL drivers so no real display or audio hardware is required.
"""
import os

# Must be set BEFORE pygame is imported anywhere in the test session
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

