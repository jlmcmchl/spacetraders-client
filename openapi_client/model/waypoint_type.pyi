# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.     # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class WaypointType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of waypoint.
    """
    
    @schemas.classproperty
    def PLANET(cls):
        return cls("PLANET")
    
    @schemas.classproperty
    def GAS_GIANT(cls):
        return cls("GAS_GIANT")
    
    @schemas.classproperty
    def MOON(cls):
        return cls("MOON")
    
    @schemas.classproperty
    def ORBITAL_STATION(cls):
        return cls("ORBITAL_STATION")
    
    @schemas.classproperty
    def JUMP_GATE(cls):
        return cls("JUMP_GATE")
    
    @schemas.classproperty
    def ASTEROID_FIELD(cls):
        return cls("ASTEROID_FIELD")
    
    @schemas.classproperty
    def NEBULA(cls):
        return cls("NEBULA")
    
    @schemas.classproperty
    def DEBRIS_FIELD(cls):
        return cls("DEBRIS_FIELD")
    
    @schemas.classproperty
    def GRAVITY_WELL(cls):
        return cls("GRAVITY_WELL")
