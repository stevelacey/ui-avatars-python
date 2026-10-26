"""Deterministic avatar URLs: Gravatar or Libravatar photos with a colorful initials fallback."""

from ui_avatars.generator import Avatars, avatars
from ui_avatars.mixins import AvatarMixin
from ui_avatars.shortcuts import avatar_url, is_local

__all__ = ["AvatarMixin", "Avatars", "avatar_url", "avatars", "is_local"]
